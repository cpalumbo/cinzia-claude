#!/usr/bin/env python3
"""
Aprovo Lead Scraper for Barcelona Dental Clinics
Real version that scrapes actual clinic websites.
"""

import csv
import json
import re
import time
from datetime import date
from typing import Dict, List, Optional
from urllib.parse import urlparse, urljoin, quote_plus
import requests
from bs4 import BeautifulSoup


class RealClinicScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        })
        self.clinics = []
        self.seen_websites = set()
        self.seen_phones = set()

    def search_web(self, query: str, num_results: int = 20) -> List[str]:
        """
        Search the web for clinic websites.
        Returns list of URLs.
        """
        print(f"  Searching web for: {query}")
        urls = []

        # Use DuckDuckGo HTML search (no API key needed)
        try:
            search_url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
            response = self.session.get(search_url, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # DuckDuckGo results are in links with class 'result__a'
                for link in soup.find_all('a', class_='result__a', limit=num_results):
                    href = link.get('href')
                    if href and href.startswith('http'):
                        urls.append(href)

            time.sleep(2)  # Rate limiting
        except Exception as e:
            print(f"    Search error: {e}")

        return urls

    def extract_contact_info(self, soup: BeautifulSoup, url: str) -> Dict:
        """Extract phone and email from webpage."""
        text = soup.get_text()
        html = str(soup)

        contact = {
            'phone': '',
            'email': ''
        }

        # Spanish phone pattern: +34 XXX XXX XXX or 9XX XXX XXX
        phone_patterns = [
            r'\+34\s*\d{3}\s*\d{3}\s*\d{3}',
            r'9\d{2}\s*\d{3}\s*\d{3}',
            r'\(\+34\)\s*\d{3}\s*\d{3}\s*\d{3}',
        ]
        for pattern in phone_patterns:
            match = re.search(pattern, text)
            if match:
                contact['phone'] = match.group().strip()
                break

        # Email
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, html)
        if emails:
            # Filter out common false positives
            valid_emails = [
                e for e in emails
                if 'example.com' not in e.lower()
                and 'sentry' not in e.lower()
                and 'wixpress' not in e.lower()
                and 'schemas.org' not in e.lower()
            ]
            if valid_emails:
                contact['email'] = valid_emails[0]

        return contact

    def scrape_website(self, url: str) -> Optional[Dict]:
        """Scrape clinic website for all data and ICP signals."""

        try:
            print(f"    Scraping: {url}")
            response = self.session.get(url, timeout=15)

            if response.status_code != 200:
                print(f"    Failed: HTTP {response.status_code}")
                return None

            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text().lower()
            html = str(soup).lower()

            # Extract clinic name (from title or h1)
            clinic_name = ''
            title_tag = soup.find('title')
            if title_tag:
                clinic_name = title_tag.get_text().strip()
            if not clinic_name:
                h1 = soup.find('h1')
                if h1:
                    clinic_name = h1.get_text().strip()
            if not clinic_name:
                clinic_name = urlparse(url).netloc

            # Extract contact info
            contact = self.extract_contact_info(soup, url)

            # Initialize clinic data
            clinic = {
                'clinic_name': clinic_name[:100],  # Limit length
                'website_url': url,
                'city': 'Barcelona',
                'phone': contact['phone'],
                'email': contact['email'],
                'google_rating': 0,
                'google_review_count': 0,
                'instagram_handle': '',
                'instagram_followers': 0,
                'has_online_booking': False,
                'has_whatsapp': False,
                'has_financing': False,
                'mentions_implants': False,
                'mentions_invisalign': False,
                'mentions_carillas': False,
                'has_gallery': False,
                'website_quality': 'modern',
                'multi_location': False,
                'icp_score': 0,
                'notes': ''
            }

            # Website quality check
            if soup.find('meta', {'name': 'viewport'}):
                clinic['website_quality'] = 'modern'
            else:
                # Check for old indicators
                if '<table' in html and '<font' in html:
                    clinic['website_quality'] = 'dated'
                elif 'wordpress' in html or 'wix' in html:
                    clinic['website_quality'] = 'modern'
                else:
                    clinic['website_quality'] = 'modern'

            # Online booking
            booking_keywords = [
                'reserva online', 'pedir cita', 'book online',
                'agendar cita', 'calendly', 'doctolib', 'agenda tu cita',
                'solicitar cita', 'cita previa'
            ]
            if any(kw in text for kw in booking_keywords):
                clinic['has_online_booking'] = True

            # WhatsApp
            if 'whatsapp' in text or 'wa.me' in html or 'api.whatsapp.com' in html:
                clinic['has_whatsapp'] = True

            # Financing
            financing_keywords = [
                'financiación', 'financiacion', 'financiamos',
                'cuotas', 'pago aplazado', 'financiar', 'pago a plazos'
            ]
            if any(kw in text for kw in financing_keywords):
                clinic['has_financing'] = True

            # High-ticket treatments
            if 'implante' in text:
                clinic['mentions_implants'] = True

            if 'invisalign' in text or 'ortodoncia invisible' in text or 'alineadores' in text:
                clinic['mentions_invisalign'] = True

            if 'carilla' in text or 'estética dental' in text or 'estetica dental' in text:
                clinic['mentions_carillas'] = True

            # Gallery
            gallery_keywords = [
                'antes y después', 'antes y despues', 'antes-después',
                'galería', 'galeria', 'casos', 'resultados'
            ]
            if any(kw in text for kw in gallery_keywords):
                clinic['has_gallery'] = True

            # Multi-location
            location_keywords = [
                'nuestras clínicas', 'nuestras clinicas',
                'otras ubicaciones', 'centros', 'sedes'
            ]
            if any(kw in text for kw in location_keywords):
                clinic['multi_location'] = True

            # Find Instagram handle
            instagram_pattern = r'instagram\.com/([a-zA-Z0-9._]+)'
            instagram_match = re.search(instagram_pattern, html)
            if instagram_match:
                clinic['instagram_handle'] = '@' + instagram_match.group(1)

            # Notes
            clinic['notes'] = f"Scraped: {date.today()}"

            return clinic

        except Exception as e:
            print(f"    Error: {e}")
            return None

    def calculate_icp_score(self, clinic: Dict) -> int:
        """Calculate ICP score based on scoring model."""
        score = 0

        # Digital Savviness
        if clinic.get('website_quality') == 'modern':
            score += 10
        elif clinic.get('website_quality') == 'dated':
            score -= 20
        elif clinic.get('website_quality') == 'none':
            score -= 50

        if clinic.get('has_online_booking'):
            score += 15

        if clinic.get('instagram_followers', 0) > 1000:
            score += 10
        elif clinic.get('instagram_handle'):
            score += 5  # Has Instagram even if followers unknown

        if clinic.get('has_whatsapp'):
            score += 5

        if clinic.get('google_review_count', 0) > 50:
            score += 5

        # High-Ticket Focus
        if clinic.get('mentions_implants'):
            score += 10
        if clinic.get('mentions_invisalign'):
            score += 15
        if clinic.get('mentions_carillas'):
            score += 10
        if clinic.get('has_gallery'):
            score += 5
        if clinic.get('has_financing'):
            score += 10

        # Bonus
        if clinic.get('multi_location'):
            score += 10

        # Penalties
        if not clinic.get('website_url'):
            score -= 50
        if not any([
            clinic.get('mentions_implants'),
            clinic.get('mentions_invisalign'),
            clinic.get('mentions_carillas')
        ]):
            score -= 20

        return max(0, score)

    def deduplicate_clinic(self, website: str, phone: str) -> bool:
        """Check if clinic is duplicate."""
        if website:
            domain = urlparse(website).netloc.replace('www.', '')
            if domain in self.seen_websites:
                return True
            self.seen_websites.add(domain)

        if phone:
            clean_phone = re.sub(r'[\s\(\)\+\-]', '', phone)
            if clean_phone in self.seen_phones:
                return True
            self.seen_phones.add(clean_phone)

        return False

    def run(self, queries: List[str], target_count: int = 200, min_score: int = 60) -> List[Dict]:
        """Main scraping workflow."""
        print("=" * 70)
        print("Aprovo Lead Scraper - Barcelona Dental Clinics")
        print("=" * 70)

        # Step 1: Search for clinic websites
        print(f"\n[Step 1] Searching for dental clinic websites...")
        all_urls = set()

        for query in queries:
            urls = self.search_web(query, num_results=50)
            all_urls.update(urls)
            print(f"    Found {len(urls)} URLs for '{query}'")

            if len(all_urls) >= target_count:
                break

        print(f"  Total unique URLs: {len(all_urls)}")

        # Step 2: Scrape each website
        print(f"\n[Step 2] Scraping websites...")
        processed = 0

        for url in list(all_urls)[:target_count]:
            # Filter: must be Spanish domain or contain Barcelona
            if not any(tld in url for tld in ['.es', '.cat', 'barcelona']):
                continue

            # Skip large DSO chains
            skip_domains = ['sanitas', 'vitaldent', 'impress']
            if any(d in url.lower() for d in skip_domains):
                print(f"    Skipping DSO chain: {url}")
                continue

            clinic = self.scrape_website(url)

            if clinic:
                # Deduplicate
                if self.deduplicate_clinic(clinic['website_url'], clinic['phone']):
                    print(f"    Duplicate - skipping")
                    continue

                # Calculate score
                clinic['icp_score'] = self.calculate_icp_score(clinic)
                self.clinics.append(clinic)

                print(f"    ✓ {clinic['clinic_name'][:50]} - Score: {clinic['icp_score']}")
                processed += 1

            time.sleep(3)  # Rate limiting

            if processed >= target_count:
                break

        # Step 3: Filter by minimum score
        print(f"\n[Step 3] Filtering qualified leads (score >= {min_score})...")
        qualified = [c for c in self.clinics if c['icp_score'] >= min_score]
        qualified.sort(key=lambda x: x['icp_score'], reverse=True)

        print(f"  Qualified leads: {len(qualified)} / {len(self.clinics)}")

        return qualified

    def save_to_csv(self, clinics: List[Dict], filename: str):
        """Save clinics to CSV file."""
        fieldnames = [
            'clinic_name', 'website_url', 'city', 'phone', 'email',
            'google_rating', 'google_review_count', 'instagram_handle',
            'instagram_followers', 'has_online_booking', 'has_whatsapp',
            'has_financing', 'mentions_implants', 'mentions_invisalign',
            'mentions_carillas', 'has_gallery', 'website_quality',
            'multi_location', 'icp_score', 'notes'
        ]

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(clinics)

        print(f"\n✓ CSV saved: {filename}")

    def print_summary(self, qualified: List[Dict]):
        """Print summary report."""
        print("\n" + "=" * 70)
        print("SUMMARY REPORT")
        print("=" * 70)
        print(f"Total clinics scraped: {len(self.clinics)}")
        print(f"Qualified leads (60+): {len(qualified)}")

        if qualified:
            avg_score = sum(c['icp_score'] for c in qualified) / len(qualified)
            print(f"Average ICP score: {avg_score:.1f}")

            print(f"\nTop 10 Highest-Scoring Leads:")
            print("-" * 70)
            for i, clinic in enumerate(qualified[:10], 1):
                print(f"{i}. {clinic['clinic_name'][:50]}")
                print(f"   Score: {clinic['icp_score']} | {clinic['website_url']}")
                signals = []
                if clinic['has_online_booking']:
                    signals.append('Online Booking')
                if clinic['mentions_invisalign']:
                    signals.append('Invisalign')
                if clinic['mentions_implants']:
                    signals.append('Implants')
                if clinic['has_whatsapp']:
                    signals.append('WhatsApp')
                print(f"   Signals: {', '.join(signals)}")
                print()


def main():
    scraper = RealClinicScraper()

    # Search queries for Barcelona dental clinics
    queries = [
        "clínica dental estética Barcelona",
        "implantes dentales Barcelona",
        "invisalign Barcelona",
        "ortodoncia invisible Barcelona",
        "carillas dentales Barcelona",
        "clínica dental Barcelona Invisalign",
    ]

    # Run scraper
    print(f"Target: 100-200 qualified leads (score 60+)")
    print(f"Will scrape up to 200 clinics to find qualified leads\n")

    qualified_leads = scraper.run(
        queries=queries,
        target_count=200,
        min_score=60
    )

    # Save results
    output_file = f"aprovo_leads_barcelona_{date.today()}.csv"
    scraper.save_to_csv(qualified_leads, output_file)

    # Print summary
    scraper.print_summary(qualified_leads)

    # Save full list (including non-qualified) for reference
    if scraper.clinics:
        full_output = f"aprovo_leads_barcelona_full_{date.today()}.csv"
        scraper.save_to_csv(scraper.clinics, full_output)
        print(f"\n✓ Full list (all scores) saved: {full_output}")


if __name__ == "__main__":
    main()
