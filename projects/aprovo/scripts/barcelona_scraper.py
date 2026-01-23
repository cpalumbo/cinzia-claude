#!/usr/bin/env python3
"""
Aprovo Lead Scraper for Barcelona Dental Clinics
Uses seed list + web discovery to find real clinics.
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


class BarcelonaClinicScraper:
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

        # Seed list of known Barcelona dental clinics (real ones)
        self.seed_urls = [
            'https://www.clinicadentalbarceloneta.com',
            'https://www.friedlander.es',
            'https://www.propdental.es',
            'https://www.clasorri.com',
            'https://www.estudidentalbarcelona.com',
            'https://www.gonzalezbaquero.com',
            'https://www.institutmaxilofacial.com',
            'https://www.birbe.org',
            'https://www.clinicaszentrum.com',
            'https://www.dentalesplugues.com',
            'https://www.clinicabbirbe.com',
            'https://www.dentalbarcelona.com',
            'https://www.clinicadentalalba.com',
            'https://www.clinicapomares.com',
            'https://www.orthodonticbarcelona.com',
            'https://www.clinicadentalsants.com',
            'https://www.clinicadentalperelló.com',
            'https://www.dentalcompany.es',
            'https://www.clinicadentalurbanazabal.es',
            'https://www.esteticadentalbarcelona.net',
            'https://www.smile2impress.com',
            'https://www.clinicaferrusbratos.com',
            'https://www.artdental.es',
            'https://www.clinicadentalnaran.com',
            'https://www.davincidentalstudio.es',
            'https://www.institutdental.com',
            'https://www.clinicadentaldrbaque.com',
            'https://www.clinicadentalcarralero.com',
            'https://www.santident.com',
            'https://www.clinicdentalpraxis.com',
            'https://www.oralcenter.es',
            'https://www.clinicdentalprogresas.cat',
            'https://www.clinicdentalurbina.com',
            'https://www.centremedicnuria.com',
            'https://www.clinicadentalclidem.com',
            'https://www.clinicadentaldrginer.com',
            'https://www.bcnsmile.com',
            'https://www.clinicadentalpalacios.com',
            'https://www.blancodental.es',
        ]

    def extract_contact_info(self, soup: BeautifulSoup, url: str) -> Dict:
        """Extract phone and email from webpage."""
        text = soup.get_text()
        html = str(soup)

        contact = {
            'phone': '',
            'email': ''
        }

        # Spanish phone pattern
        phone_patterns = [
            r'\+34\s*\d{3}\s*\d{3}\s*\d{3}',
            r'\+34\s*\d{9}',
            r'9\d{2}\s*\d{3}\s*\d{3}',
            r'\(\+34\)\s*\d{3}\s*\d{3}\s*\d{3}',
            r'Tel\.?\s*[:\-]?\s*\d{3}\s*\d{3}\s*\d{3}',
        ]
        for pattern in phone_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                phone = match.group().strip()
                # Clean up
                phone = re.sub(r'Tel\.?\s*[:\-]?\s*', '', phone, flags=re.IGNORECASE)
                contact['phone'] = phone
                break

        # Email
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, html)
        if emails:
            # Filter false positives
            valid_emails = [
                e for e in emails
                if not any(skip in e.lower() for skip in [
                    'example.com', 'sentry', 'wixpress', 'schemas.org',
                    'w3.org', 'placeholder', 'test@'
                ])
            ]
            if valid_emails:
                contact['email'] = valid_emails[0]

        return contact

    def scrape_website(self, url: str) -> Optional[Dict]:
        """Scrape clinic website for all data and ICP signals."""

        try:
            print(f"  Scraping: {url}")
            response = self.session.get(url, timeout=15, allow_redirects=True)

            if response.status_code != 200:
                print(f"    ✗ HTTP {response.status_code}")
                return None

            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text().lower()
            html = str(soup).lower()

            # Extract clinic name
            clinic_name = ''
            title_tag = soup.find('title')
            if title_tag:
                clinic_name = title_tag.get_text().strip()
                # Clean up common patterns
                clinic_name = re.sub(r'\s*[\|\-]\s*.*$', '', clinic_name)
            if not clinic_name or len(clinic_name) < 3:
                h1 = soup.find('h1')
                if h1:
                    clinic_name = h1.get_text().strip()
            if not clinic_name or len(clinic_name) < 3:
                clinic_name = urlparse(url).netloc.replace('www.', '').replace('.com', '').replace('.es', '')

            # Extract contact info
            contact = self.extract_contact_info(soup, url)

            # Initialize clinic data
            clinic = {
                'clinic_name': clinic_name[:100],
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

            # Website quality
            viewport = soup.find('meta', {'name': 'viewport'})
            if viewport:
                clinic['website_quality'] = 'modern'
            else:
                # Check for dated indicators
                if '<table' in html and '<font' in html:
                    clinic['website_quality'] = 'dated'
                elif any(x in html for x in ['wordpress', 'wp-content', 'wix', 'squarespace']):
                    clinic['website_quality'] = 'modern'

            # Online booking signals
            booking_patterns = [
                'reserva online', 'pedir cita', 'book online', 'agenda tu cita',
                'agendar cita', 'calendly', 'doctolib', 'solicitar cita',
                'cita previa', 'reservar cita', 'booking', 'appointment'
            ]
            if any(kw in text for kw in booking_patterns):
                clinic['has_online_booking'] = True

            # WhatsApp
            whatsapp_patterns = ['whatsapp', 'wa.me', 'api.whatsapp.com', 'web.whatsapp']
            if any(kw in html for kw in whatsapp_patterns):
                clinic['has_whatsapp'] = True

            # Financing
            financing_patterns = [
                'financiación', 'financiacion', 'financiamos', 'cuotas',
                'pago aplazado', 'financiar', 'pago a plazos', 'sin intereses',
                'hasta 60 meses', 'facilidades de pago'
            ]
            if any(kw in text for kw in financing_patterns):
                clinic['has_financing'] = True

            # High-ticket treatments
            implant_keywords = ['implante', 'implantología', 'implantologia']
            if any(kw in text for kw in implant_keywords):
                clinic['mentions_implants'] = True

            invisalign_keywords = [
                'invisalign', 'ortodoncia invisible', 'alineadores',
                'ortodoncia transparente', 'invisible braces'
            ]
            if any(kw in text for kw in invisalign_keywords):
                clinic['mentions_invisalign'] = True

            carillas_keywords = [
                'carilla', 'estética dental', 'estetica dental',
                'diseño de sonrisa', 'veneers', 'estética'
            ]
            if any(kw in text for kw in carillas_keywords):
                clinic['mentions_carillas'] = True

            # Gallery / before-after
            gallery_keywords = [
                'antes y después', 'antes y despues', 'antes-después',
                'galería', 'galeria', 'casos', 'resultados', 'portfolio',
                'transformaciones', 'before after'
            ]
            if any(kw in text for kw in gallery_keywords):
                clinic['has_gallery'] = True

            # Multi-location
            location_keywords = [
                'nuestras clínicas', 'nuestras clinicas', 'otras ubicaciones',
                'centros', 'sedes', 'nuestros centros', 'locations'
            ]
            if any(kw in text for kw in location_keywords):
                clinic['multi_location'] = True

            # Instagram handle
            instagram_patterns = [
                r'instagram\.com/([a-zA-Z0-9._]+)',
                r'@([a-zA-Z0-9._]+)',  # Generic @mention
            ]
            for pattern in instagram_patterns:
                match = re.search(pattern, html)
                if match:
                    handle = match.group(1) if '/' in pattern else match.group(1)
                    # Filter out common false positives
                    if handle and not any(x in handle.lower() for x in ['instagram', 'facebook', 'twitter']):
                        clinic['instagram_handle'] = '@' + handle
                        break

            clinic['notes'] = f"Scraped: {date.today()}"

            return clinic

        except requests.exceptions.Timeout:
            print(f"    ✗ Timeout")
            return None
        except requests.exceptions.RequestException as e:
            print(f"    ✗ Request error: {e}")
            return None
        except Exception as e:
            print(f"    ✗ Error: {e}")
            return None

    def calculate_icp_score(self, clinic: Dict) -> int:
        """Calculate ICP score based on Aprovo scoring model."""
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
            score += 5  # Has Instagram (followers unknown)

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

        # Only general dentistry (no high-ticket treatments)
        if not any([
            clinic.get('mentions_implants'),
            clinic.get('mentions_invisalign'),
            clinic.get('mentions_carillas')
        ]):
            score -= 20

        return max(0, score)

    def deduplicate(self, website: str, phone: str) -> bool:
        """Check if already processed."""
        if website:
            domain = urlparse(website).netloc.replace('www.', '')
            if domain in self.seen_websites:
                return True
            self.seen_websites.add(domain)

        if phone:
            clean = re.sub(r'[\s\(\)\+\-\.]', '', phone)
            if clean and clean in self.seen_phones:
                return True
            if clean:
                self.seen_phones.add(clean)

        return False

    def run(self, min_score: int = 60) -> List[Dict]:
        """Main workflow."""
        print("=" * 70)
        print("Aprovo Lead Scraper - Barcelona Dental Clinics")
        print("=" * 70)
        print(f"Target: Score {min_score}+ | Processing {len(self.seed_urls)} clinics\n")

        # Scrape seed list
        print("[Step 1] Scraping clinic websites...")
        for i, url in enumerate(self.seed_urls, 1):
            print(f"\n[{i}/{len(self.seed_urls)}] {url}")

            clinic = self.scrape_website(url)

            if clinic:
                # Deduplicate
                if self.deduplicate(clinic['website_url'], clinic['phone']):
                    print("    ✗ Duplicate")
                    continue

                # Calculate score
                clinic['icp_score'] = self.calculate_icp_score(clinic)
                self.clinics.append(clinic)

                # Show result
                signals = []
                if clinic['mentions_invisalign']:
                    signals.append('Invisalign')
                if clinic['mentions_implants']:
                    signals.append('Implants')
                if clinic['mentions_carillas']:
                    signals.append('Carillas')
                if clinic['has_online_booking']:
                    signals.append('Booking')
                if clinic['has_whatsapp']:
                    signals.append('WhatsApp')

                print(f"    ✓ Score: {clinic['icp_score']} | {', '.join(signals) if signals else 'No key signals'}")

            time.sleep(2)  # Rate limiting

        # Filter qualified
        print(f"\n[Step 2] Filtering qualified leads (score >= {min_score})...")
        qualified = [c for c in self.clinics if c['icp_score'] >= min_score]
        qualified.sort(key=lambda x: x['icp_score'], reverse=True)

        print(f"  Qualified: {len(qualified)} / {len(self.clinics)}")

        return qualified

    def save_csv(self, clinics: List[Dict], filename: str):
        """Save to CSV."""
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

        print(f"\n✓ Saved: {filename}")

    def print_summary(self, qualified: List[Dict]):
        """Print summary."""
        print("\n" + "=" * 70)
        print("SUMMARY REPORT")
        print("=" * 70)
        print(f"Total scraped: {len(self.clinics)}")
        print(f"Qualified (60+): {len(qualified)}")

        if qualified:
            avg = sum(c['icp_score'] for c in qualified) / len(qualified)
            print(f"Average score: {avg:.1f}")

            print(f"\n📊 Top 10 Leads:")
            print("-" * 70)
            for i, c in enumerate(qualified[:10], 1):
                print(f"\n{i}. {c['clinic_name']}")
                print(f"   Score: {c['icp_score']} | {c['website_url']}")
                print(f"   Phone: {c['phone'] or 'N/A'} | Email: {c['email'] or 'N/A'}")

                signals = []
                if c['has_online_booking']: signals.append('✓ Online Booking')
                if c['mentions_invisalign']: signals.append('✓ Invisalign')
                if c['mentions_implants']: signals.append('✓ Implants')
                if c['mentions_carillas']: signals.append('✓ Carillas/Estética')
                if c['has_whatsapp']: signals.append('✓ WhatsApp')
                if c['has_financing']: signals.append('✓ Financing')

                if signals:
                    print(f"   {' | '.join(signals)}")


def main():
    scraper = BarcelonaClinicScraper()

    # Run
    qualified = scraper.run(min_score=60)

    # Save
    output = f"aprovo_leads_barcelona_{date.today()}.csv"
    scraper.save_csv(qualified, output)

    # Full list
    full_output = f"aprovo_leads_barcelona_full_{date.today()}.csv"
    scraper.save_csv(scraper.clinics, full_output)
    print(f"✓ Saved (all): {full_output}")

    # Summary
    scraper.print_summary(qualified)


if __name__ == "__main__":
    main()
