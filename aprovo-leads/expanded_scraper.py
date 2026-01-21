#!/usr/bin/env python3
"""
Aprovo Lead Scraper - Expanded Barcelona List
Includes larger list of real Barcelona dental clinics.
"""

import csv
import json
import re
import time
from datetime import date
from typing import Dict, List, Optional
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


class ExpandedBarcelonaScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        })
        self.session.verify = False  # Handle SSL issues
        requests.packages.urllib3.disable_warnings()  # Suppress SSL warnings

        self.clinics = []
        self.seen_websites = set()
        self.seen_phones = set()

        # Expanded list of Barcelona dental clinics
        self.seed_urls = [
            # Previously scraped (keep working ones)
            'https://www.propdental.es',
            'https://www.clinicadentalbarceloneta.com',
            'https://www.estudidentalbarcelona.com',
            'https://www.birbe.org',
            'https://www.dentalcompany.es',
            'https://www.clinicaferrusbratos.com',
            'https://www.artdental.es',
            'https://www.clinicadentalcarralero.com',
            'https://www.santident.com',

            # Additional Barcelona clinics
            'https://www.dentalmedicbrusi.com',
            'https://www.dentaladvisor.es',
            'https://www.masdental.com',
            'https://www.clinicdentalcornella.com',
            'https://www.dentalimplantbarcelona.com',
            'https://www.dentalsarrialaplana.com',
            'https://www.barceloneta-dental.com',
            'https://www.dentistaenbadalona.com',
            'https://www.clinicdentalsomriures.cat',
            'https://www.detistabarcelona.com',
            'https://www.clinicadentalmartinezsimon.com',
            'https://www.dentalbcn.com',
            'https://www.clinicdentalparaire.com',
            'https://www.servidentistabarcelona.com',
            'https://www.centromedicodental.com',
            'https://www.dentalemporda.com',
            'https://www.clinicadentalcarolina.es',
            'https://www.dentalasturias.com',
            'https://www.clinicdentaldrvelazquez.com',
            'https://www.clinicadentalrubi.com',
            'https://www.dentalperez.es',
            'https://www.clinicdentalelprat.com',
            'https://www.clinicadentalsabadell.com',
            'https://www.dentalterrassa.com',
            'https://www.clinicdentalvic.com',
            'https://www.cliniquedentalereiki.com',
            'https://www.aparatosdentalbarcelona.com',
            'https://www.odontologiabarcelona.com',
            'https://www.dentistagracia.com',
            'https://www.dentistaeixample.com',
            'https://www.clinicadentalgotico.com',
            'https://www.dentalborn.com',
            'https://www.clinicdentalpoblenou.com',
            'https://www.dentistahorta.com',
            'https://www.clinicadentalnoubarris.com',
            'https://www.dentalsantandreu.com',
            'https://www.clinicadentallesarts.com',
            'https://www.dentalsantsmontjuic.com',
            'https://www.clinicadentalsarria.com',
            'https://www.dentistagracia.barcelona',
            'https://www.odontosalut.com',
            'https://www.clinicaunidental.com',
            'https://www.clinicadentaldrarobertson.com',
            'https://www.bracesdentistbarcelona.com',
            'https://www.totaldentalbarcelona.com',
            'https://www.asisa.es/dental',
            'https://www.imqsalud.es/dental',
            'https://www.dentyred.es/clinicas-barcelona',

            # Known Invisalign providers in Barcelona area
            'https://www.drsimarro.com',
            'https://www.ortodoncia-friedlander.com',
            'https://www.clinicabadal.com',
            'https://www.institutortodoncic.com',
            'https://www.ortodoncia-barcelona.com',
            'https://www.clinicadentalnovadental.es',
            'https://www.idealdentalbarcelona.com',
            'https://www.ilerdent.com',
            'https://www.centredentalvilardell.com',
            'https://www.dentalmaresme.com',
        ]

    def extract_contact_info(self, soup: BeautifulSoup, url: str) -> Dict:
        """Extract phone and email."""
        text = soup.get_text()
        html = str(soup)

        contact = {'phone': '', 'email': ''}

        # Phone patterns
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
                phone = re.sub(r'Tel\.?\s*[:\-]?\s*', '', phone, flags=re.IGNORECASE)
                contact['phone'] = phone
                break

        # Email
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, html)
        if emails:
            valid_emails = [
                e for e in emails
                if not any(skip in e.lower() for skip in [
                    'example.', 'sentry', 'wixpress', 'schemas.org',
                    'w3.org', 'placeholder', 'test@'
                ])
            ]
            if valid_emails:
                contact['email'] = valid_emails[0]

        return contact

    def scrape_website(self, url: str) -> Optional[Dict]:
        """Scrape clinic website."""
        try:
            print(f"  {url}")
            response = self.session.get(url, timeout=15, allow_redirects=True)

            if response.status_code != 200:
                print(f"    ✗ HTTP {response.status_code}")
                return None

            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text().lower()
            html = str(soup).lower()

            # Extract name
            clinic_name = ''
            title = soup.find('title')
            if title:
                clinic_name = title.get_text().strip()
                clinic_name = re.sub(r'\s*[\|\-]\s*.*$', '', clinic_name)
            if not clinic_name or len(clinic_name) < 3:
                h1 = soup.find('h1')
                if h1:
                    clinic_name = h1.get_text().strip()
            if not clinic_name or len(clinic_name) < 3:
                clinic_name = urlparse(url).netloc.replace('www.', '').split('.')[0]

            # Contact
            contact = self.extract_contact_info(soup, url)

            # Initialize
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

            # Quality
            viewport = soup.find('meta', {'name': 'viewport'})
            if viewport:
                clinic['website_quality'] = 'modern'
            elif '<table' in html and '<font' in html:
                clinic['website_quality'] = 'dated'

            # Signals
            booking_kw = ['reserva online', 'pedir cita', 'book online', 'agenda tu cita',
                          'agendar cita', 'calendly', 'doctolib', 'solicitar cita', 'cita previa']
            if any(kw in text for kw in booking_kw):
                clinic['has_online_booking'] = True

            if any(kw in html for kw in ['whatsapp', 'wa.me', 'api.whatsapp']):
                clinic['has_whatsapp'] = True

            financing_kw = ['financiación', 'financiacion', 'financiamos', 'cuotas',
                            'pago aplazado', 'pago a plazos', 'sin intereses']
            if any(kw in text for kw in financing_kw):
                clinic['has_financing'] = True

            if 'implante' in text or 'implantología' in text:
                clinic['mentions_implants'] = True

            if any(kw in text for kw in ['invisalign', 'ortodoncia invisible', 'alineadores']):
                clinic['mentions_invisalign'] = True

            if any(kw in text for kw in ['carilla', 'estética dental', 'estetica dental', 'diseño de sonrisa']):
                clinic['mentions_carillas'] = True

            if any(kw in text for kw in ['antes y después', 'antes y despues', 'galería', 'galeria', 'casos']):
                clinic['has_gallery'] = True

            if any(kw in text for kw in ['nuestras clínicas', 'nuestras clinicas', 'otros centros', 'sedes']):
                clinic['multi_location'] = True

            # Instagram
            ig_match = re.search(r'instagram\.com/([a-zA-Z0-9._]+)', html)
            if ig_match:
                handle = ig_match.group(1)
                if handle and not any(x in handle.lower() for x in ['instagram', 'facebook', 'twitter']):
                    clinic['instagram_handle'] = '@' + handle

            clinic['notes'] = f"Scraped: {date.today()}"
            return clinic

        except Exception as e:
            print(f"    ✗ {str(e)[:60]}")
            return None

    def calculate_icp_score(self, clinic: Dict) -> int:
        """Calculate ICP score."""
        score = 0

        # Digital Savviness
        if clinic.get('website_quality') == 'modern':
            score += 10
        elif clinic.get('website_quality') == 'dated':
            score -= 20

        if clinic.get('has_online_booking'):
            score += 15
        if clinic.get('instagram_followers', 0) > 1000:
            score += 10
        elif clinic.get('instagram_handle'):
            score += 5
        if clinic.get('has_whatsapp'):
            score += 5
        if clinic.get('google_review_count', 0) > 50:
            score += 5

        # High-Ticket
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
        if not any([clinic.get('mentions_implants'), clinic.get('mentions_invisalign'), clinic.get('mentions_carillas')]):
            score -= 20

        return max(0, score)

    def deduplicate(self, website: str, phone: str) -> bool:
        """Check duplicates."""
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
        print("Aprovo Lead Scraper - Barcelona (Expanded)")
        print("=" * 70)
        print(f"Processing {len(self.seed_urls)} clinics | Target score: {min_score}+\n")

        for i, url in enumerate(self.seed_urls, 1):
            print(f"[{i}/{len(self.seed_urls)}]", end=" ")

            clinic = self.scrape_website(url)

            if clinic:
                if self.deduplicate(clinic['website_url'], clinic['phone']):
                    print("    ✗ Duplicate")
                    continue

                clinic['icp_score'] = self.calculate_icp_score(clinic)
                self.clinics.append(clinic)

                signals = []
                if clinic['mentions_invisalign']:
                    signals.append('Invisalign')
                if clinic['mentions_implants']:
                    signals.append('Implants')
                if clinic['has_online_booking']:
                    signals.append('Booking')
                if clinic['has_whatsapp']:
                    signals.append('WA')

                status = '✓' if clinic['icp_score'] >= min_score else '•'
                print(f"    {status} Score:{clinic['icp_score']:3d} | {', '.join(signals) if signals else 'No signals'}")

            time.sleep(1.5)  # Rate limit

        # Filter
        qualified = [c for c in self.clinics if c['icp_score'] >= min_score]
        qualified.sort(key=lambda x: x['icp_score'], reverse=True)

        print(f"\n✓ Qualified: {len(qualified)} / {len(self.clinics)}")
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

    def print_summary(self, qualified: List[Dict]):
        """Print summary."""
        print("\n" + "=" * 70)
        print("FINAL SUMMARY")
        print("=" * 70)
        print(f"Total scraped: {len(self.clinics)}")
        print(f"Qualified (60+): {len(qualified)}")

        if qualified:
            avg = sum(c['icp_score'] for c in qualified) / len(qualified)
            print(f"Average score: {avg:.1f}")

            # Score distribution
            score_ranges = {'60-69': 0, '70-79': 0, '80-89': 0, '90+': 0}
            for c in qualified:
                if c['icp_score'] >= 90:
                    score_ranges['90+'] += 1
                elif c['icp_score'] >= 80:
                    score_ranges['80-89'] += 1
                elif c['icp_score'] >= 70:
                    score_ranges['70-79'] += 1
                else:
                    score_ranges['60-69'] += 1

            print(f"\nScore Distribution:")
            for range_name, count in score_ranges.items():
                print(f"  {range_name}: {count}")

            print(f"\nTop 10 Leads:")
            print("-" * 70)
            for i, c in enumerate(qualified[:10], 1):
                print(f"\n{i}. {c['clinic_name'][:55]}")
                print(f"   Score: {c['icp_score']} | {c['website_url']}")
                print(f"   Phone: {c['phone'] or 'N/A'} | Email: {c['email'] or 'N/A'}")

                signals = []
                if c['has_online_booking']: signals.append('Booking')
                if c['mentions_invisalign']: signals.append('Invisalign')
                if c['mentions_implants']: signals.append('Implants')
                if c['mentions_carillas']: signals.append('Carillas')
                if c['has_whatsapp']: signals.append('WhatsApp')
                if c['has_financing']: signals.append('Financing')

                if signals:
                    print(f"   {' | '.join(signals)}")


def main():
    scraper = ExpandedBarcelonaScraper()

    # Run
    qualified = scraper.run(min_score=60)

    # Save
    output = f"aprovo_leads_barcelona_{date.today()}.csv"
    scraper.save_csv(qualified, output)
    print(f"\n✓ Saved qualified leads: {output}")

    full_output = f"aprovo_leads_barcelona_full_{date.today()}.csv"
    scraper.save_csv(scraper.clinics, full_output)
    print(f"✓ Saved all clinics: {full_output}")

    # Summary
    scraper.print_summary(qualified)


if __name__ == "__main__":
    main()
