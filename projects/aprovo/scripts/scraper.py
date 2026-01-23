#!/usr/bin/env python3
"""
Aprovo Lead Scraper for Barcelona Dental Clinics
Finds and scores clinics based on ICP criteria.
"""

import csv
import json
import re
import time
from datetime import date
from typing import Dict, List, Optional
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup


class ClinicScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.clinics = []
        self.seen_websites = set()
        self.seen_phones = set()

    def search_google_maps_clinics(self, query: str, location: str = "Barcelona") -> List[Dict]:
        """
        Simulates Google Maps search results.
        In production, this would use Google Places API or scraping.
        For now, we'll return a sample structure and focus on known Barcelona clinics.
        """
        # Sample clinics to get started - in production this would scrape Google Maps
        sample_clinics = [
            {
                'name': 'Clínica Dental Barcelona',
                'address': 'Passeig de Gràcia, Barcelona',
                'phone': '+34 933 123 456',
                'website': 'https://www.clinicadentalbarcelona.com',
                'google_rating': 4.7,
                'google_review_count': 234
            },
            {
                'name': 'Barcelona Dental Studio',
                'address': 'Carrer de Balmes, Barcelona',
                'phone': '+34 934 567 890',
                'website': 'https://www.barcelonadentalstudio.com',
                'google_rating': 4.8,
                'google_review_count': 156
            },
            {
                'name': 'Estética Dental Barcelona',
                'address': 'Ronda de la Universitat, Barcelona',
                'phone': '+34 933 987 654',
                'website': 'https://www.esteticadentalbarcelona.es',
                'google_rating': 4.6,
                'google_review_count': 89
            }
        ]
        return sample_clinics

    def scrape_website(self, url: str) -> Dict:
        """Scrape clinic website for ICP signals."""
        signals = {
            'has_online_booking': False,
            'has_whatsapp': False,
            'has_financing': False,
            'mentions_implants': False,
            'mentions_invisalign': False,
            'mentions_carillas': False,
            'has_gallery': False,
            'website_quality': 'none',
            'multi_location': False,
            'email': ''
        }

        if not url:
            return signals

        try:
            response = self.session.get(url, timeout=10)
            if response.status_code != 200:
                return signals

            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text().lower()
            html = str(soup).lower()

            # Website quality check
            # Modern indicators: responsive meta tags, modern CSS frameworks
            if soup.find('meta', {'name': 'viewport'}):
                signals['website_quality'] = 'modern'
            else:
                # Check for old-school indicators
                if 'table' in html and 'font' in html:
                    signals['website_quality'] = 'dated'
                else:
                    signals['website_quality'] = 'modern'

            # Online booking
            booking_keywords = ['reserva online', 'pedir cita', 'book online', 'agendar cita', 'calendly', 'doctolib']
            if any(kw in text for kw in booking_keywords):
                signals['has_online_booking'] = True

            # WhatsApp
            if 'whatsapp' in text or 'wa.me' in html:
                signals['has_whatsapp'] = True

            # Financing
            financing_keywords = ['financiación', 'financiacion', 'financiamos', 'cuotas', 'pago aplazado']
            if any(kw in text for kw in financing_keywords):
                signals['has_financing'] = True

            # High-ticket treatments
            if 'implante' in text:
                signals['mentions_implants'] = True
            if 'invisalign' in text or 'ortodoncia invisible' in text:
                signals['mentions_invisalign'] = True
            if 'carilla' in text or 'estética dental' in text or 'estetica dental' in text:
                signals['mentions_carillas'] = True

            # Gallery
            gallery_keywords = ['antes y después', 'antes y despues', 'galería', 'galeria', 'casos']
            if any(kw in text for kw in gallery_keywords):
                signals['has_gallery'] = True

            # Multi-location
            location_keywords = ['nuestras clínicas', 'nuestras clinicas', 'otras ubicaciones', 'locations']
            if any(kw in text for kw in location_keywords):
                signals['multi_location'] = True

            # Email extraction
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            emails = re.findall(email_pattern, html)
            if emails:
                # Filter out common false positives
                valid_emails = [e for e in emails if 'example.com' not in e and 'sentry' not in e]
                if valid_emails:
                    signals['email'] = valid_emails[0]

        except Exception as e:
            print(f"Error scraping {url}: {e}")

        return signals

    def check_instagram(self, clinic_name: str) -> Dict:
        """Check Instagram for the clinic."""
        # This would require Instagram API or scraping
        # For now, return placeholder structure
        return {
            'instagram_handle': '',
            'instagram_followers': 0
        }

    def calculate_icp_score(self, clinic_data: Dict) -> int:
        """Calculate ICP score based on scoring model."""
        score = 0

        # Digital Savviness
        if clinic_data.get('website_quality') == 'modern':
            score += 10
        elif clinic_data.get('website_quality') == 'dated':
            score -= 20
        elif clinic_data.get('website_quality') == 'none':
            score -= 50

        if clinic_data.get('has_online_booking'):
            score += 15
        if clinic_data.get('instagram_followers', 0) > 1000:
            score += 10
        # Instagram weekly posts would add +5 (need to check posting frequency)
        if clinic_data.get('has_whatsapp'):
            score += 5
        if clinic_data.get('google_review_count', 0) > 50:
            score += 5

        # High-Ticket Focus
        if clinic_data.get('mentions_implants'):
            score += 10
        if clinic_data.get('mentions_invisalign'):
            score += 15
        if clinic_data.get('mentions_carillas'):
            score += 10
        if clinic_data.get('has_gallery'):
            score += 5
        if clinic_data.get('has_financing'):
            score += 10

        # Bonus
        if clinic_data.get('multi_location'):
            score += 10

        # Penalties
        if not clinic_data.get('website_url'):
            score -= 50
        if not any([
            clinic_data.get('mentions_implants'),
            clinic_data.get('mentions_invisalign'),
            clinic_data.get('mentions_carillas')
        ]):
            # Only general dentistry
            score -= 20

        return max(0, score)  # Don't go below 0

    def deduplicate_clinic(self, website: str, phone: str) -> bool:
        """Check if clinic is duplicate based on website or phone."""
        if website:
            domain = urlparse(website).netloc
            if domain in self.seen_websites:
                return True
            self.seen_websites.add(domain)

        if phone:
            clean_phone = re.sub(r'\s+', '', phone)
            if clean_phone in self.seen_phones:
                return True
            self.seen_phones.add(clean_phone)

        return False

    def scrape_and_score_clinic(self, raw_clinic: Dict) -> Optional[Dict]:
        """Process a single clinic: scrape website, check socials, calculate score."""

        # Deduplicate
        if self.deduplicate_clinic(raw_clinic.get('website', ''), raw_clinic.get('phone', '')):
            return None

        print(f"Processing: {raw_clinic['name']}")

        # Initialize clinic data
        clinic = {
            'clinic_name': raw_clinic['name'],
            'website_url': raw_clinic.get('website', ''),
            'city': 'Barcelona',
            'phone': raw_clinic.get('phone', ''),
            'email': '',
            'google_rating': raw_clinic.get('google_rating', 0),
            'google_review_count': raw_clinic.get('google_review_count', 0),
            'instagram_handle': '',
            'instagram_followers': 0,
            'has_online_booking': False,
            'has_whatsapp': False,
            'has_financing': False,
            'mentions_implants': False,
            'mentions_invisalign': False,
            'mentions_carillas': False,
            'has_gallery': False,
            'website_quality': 'none',
            'multi_location': False,
            'icp_score': 0,
            'notes': ''
        }

        # Scrape website
        if clinic['website_url']:
            website_signals = self.scrape_website(clinic['website_url'])
            clinic.update(website_signals)
        else:
            clinic['notes'] = 'No website found'

        # Check Instagram
        instagram_data = self.check_instagram(clinic['clinic_name'])
        clinic.update(instagram_data)

        # Calculate ICP score
        clinic['icp_score'] = self.calculate_icp_score(clinic)

        # Add processing timestamp to notes
        if clinic['notes']:
            clinic['notes'] += f" | Scraped: {date.today()}"
        else:
            clinic['notes'] = f"Scraped: {date.today()}"

        return clinic

    def run(self, queries: List[str], min_score: int = 60) -> List[Dict]:
        """Main scraping workflow."""
        print("=" * 60)
        print("Aprovo Lead Scraper - Barcelona Dental Clinics")
        print("=" * 60)

        # Step 1: Build raw list
        print("\n[Step 1] Building raw clinic list from multiple sources...")
        raw_clinics = []

        for query in queries:
            print(f"  Searching: {query}")
            results = self.search_google_maps_clinics(query)
            raw_clinics.extend(results)
            time.sleep(1)  # Rate limiting

        print(f"  Found {len(raw_clinics)} raw clinics")

        # Step 2: Scrape and score each clinic
        print("\n[Step 2] Scraping and scoring clinics...")
        for raw_clinic in raw_clinics:
            clinic = self.scrape_and_score_clinic(raw_clinic)
            if clinic:
                self.clinics.append(clinic)
                print(f"  ✓ {clinic['clinic_name']} - Score: {clinic['icp_score']}")
            time.sleep(2)  # Rate limiting

        # Step 3: Filter by minimum score
        print(f"\n[Step 3] Filtering by minimum score ({min_score}+)...")
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

        print(f"\n✓ Saved to: {filename}")


def main():
    scraper = ClinicScraper()

    # Search queries
    queries = [
        "clínica dental estética Barcelona",
        "implantes dentales Barcelona",
        "invisalign Barcelona",
        "ortodoncia invisible Barcelona"
    ]

    # Run scraper
    qualified_leads = scraper.run(queries, min_score=60)

    # Save results
    output_file = f"aprovo_leads_barcelona_{date.today()}.csv"
    scraper.save_to_csv(qualified_leads, output_file)

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)
    print(f"Total clinics scraped: {len(scraper.clinics)}")
    print(f"Qualified leads (60+): {len(qualified_leads)}")
    print(f"\nTop 10 Highest-Scoring Leads:")
    print("-" * 60)
    for i, clinic in enumerate(qualified_leads[:10], 1):
        print(f"{i}. {clinic['clinic_name']} - Score: {clinic['icp_score']}")
        print(f"   {clinic['website_url']}")
        print()


if __name__ == "__main__":
    main()
