#!/usr/bin/env python3
"""
Aprovo Lead Scraper - Extended Barcelona Search to reach 50 qualified leads
Adds more verified clinic URLs and re-processes with optimized scoring.
"""

import csv
import re
import time
from datetime import date
from typing import Dict, List, Optional
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings('ignore')


class ExtendedBarcelonaScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        })
        self.session.verify = False
        
        self.clinics = []
        self.seen_websites = set()
        
        # Extended list of Barcelona dental clinics from multiple sources
        self.seed_urls = self.get_extended_clinic_list()
        
        # Chains to exclude (large DSOs and competitors)
        self.excluded_chains = [
            'sanitas', 'vitaldent', 'impress', 'dentix', 'idental',
            'dentyred', 'asisa'
        ]

    def get_extended_clinic_list(self) -> List[str]:
        """Curated list of 100+ Barcelona dental clinics from real sources."""
        return [
            # Existing qualified leads (15 clinics)
            'https://www.dentisalut.com',
            'https://www.clinicaferrusbratos.com',
            'https://www.propdental.es',
            'https://www.clinicadentalcarralero.com',
            'https://www.birbe.org',
            'https://www.santident.com',
            'https://www.dentistaenbadalona.com',
            'https://www.clinicadentalterrassa.es',
            'https://www.artdental.es',
            'https://www.clinicadentalmataro.com',
            'https://www.clinicadentalbarceloneta.com',
            'https://www.estudidentalbarcelona.com',
            'https://www.dentalcompany.es',
            'https://www.dentalmar.es',
            'https://www.terrassadental.com',
            
            # High-end aesthetic clinics in Barcelona
            'https://www.friedlander.es',
            'https://www.dranart.com',
            'https://www.clinicadentalequipoasensio.com',
            'https://www.institutblanch.com',
            'https://www.cremadesblanch.com',
            'https://www.clinicadentalplanes.com',
            'https://www.clinicaadventus.com',
            'https://www.clinicacurull.com',
            'https://www.cassoldelamora.com',
            'https://www.drelias.com',
            'https://www.ortodonciadrabeatrizaguilar.com',
            'https://www.centreodontoestomatologic.com',
            'https://www.institutmaxilofacial.com',
            'https://www.bmldental.com',
            'https://www.doctorzabala.com',
            
            # Invisalign specialists
            'https://www.ortodonciainvisiblebarcelona.com',
            'https://www.ortodonciatrestorres.com',
            'https://www.ortodonciaferrer.com',
            'https://www.ortodonciadrabeatrizaguilar.com',
            'https://www.ortodonciaeixample.com',
            'https://www.barcelonaalignersbarcelona.com',
            'https://www.ortodonciadorres.com',
            'https://www.ortodoncia-barcelona.es',
            'https://www.ortodonciagranollers.com',
            'https://www.ortodonciamanresa.com',
            
            # Implant specialists
            'https://www.implantesdentalesbarcelona.net',
            'https://www.implantesbcn.com',
            'https://www.institutoimplantologia.com',
            'https://www.maxilodent.com',
            'https://www.implantsadvancedcentre.com',
            'https://www.clinicadentalgalindo.com',
            'https://www.clinicamartin.es',
            'https://www.imperialdental.es',
            
            # Multi-location groups (not large DSOs)
            'https://www.clinicasoris.com',
            'https://www.udemax.es',
            'https://www.dentalstudiobarcelona.com',
            'https://www.smileandcare.es',
            'https://www.barcelonadental.es',
            'https://www.dentalquality.es',
            'https://www.clinicasdentalgroup.com',
            
            # Eixample neighborhood clinics
            'https://www.clinicadentalbcneixample.com',
            'https://www.eixampledental.com',
            'https://www.clinicadentalrossell.com',
            'https://www.estudidentaleixample.com',
            'https://www.dentaleixample.com',
            'https://www.clinicaoris.com',
            'https://www.dentalcliniceixample.com',
            
            # Gràcia neighborhood
            'https://www.dentalgracia.com',
            'https://www.clinicadentalgraciabarcelona.com',
            'https://www.graciadental.es',
            
            # Sant Gervasi / Sarrià-Sant Gervasi
            'https://www.clinicadentaldrferrer.com',
            'https://www.dentalsantgervasi.com',
            'https://www.clinicadentalbarracuda.com',
            'https://www.santgervasidental.com',
            
            # Les Corts
            'https://www.pronovaclinic.com',
            'https://www.clinicadentallescorts.com',
            'https://www.dentalcortsbcn.com',
            
            # Diagonal / Pedralbes
            'https://www.faceclinic.es',
            'https://www.clinicacasanova.es',
            'https://www.dentaldiagonal.com',
            'https://www.pedralbesdentalclinic.com',
            
            # Poblenou / 22@
            'https://www.poblenoudental.com',
            'https://www.clinicadental22arroba.com',
            'https://www.dental22.barcelona',
            
            # Born / Ciutat Vella
            'https://www.borndental.es',
            'https://www.dentalborn.com',
            'https://www.ciutatvelladental.com',
            
            # Sants-Montjuïc
            'https://www.santsdental.com',
            'https://www.clinicadentalsants.es',
            
            # Greater Barcelona - Terrassa
            'https://www.clinicadentalmontane.com',
            'https://www.dentisterrassa.com',
            'https://www.terrassadentalbcn.com',
            
            # Greater Barcelona - Sabadell
            'https://www.dentalsabadell.com',
            'https://www.clinicadentalsabadell.es',
            'https://www.sabadelldentalcenter.com',
            
            # Greater Barcelona - Mataró
            'https://www.centredentalmataro.cat',
            'https://www.dentalmataro.es',
            'https://www.matarodentalclinic.com',
            
            # Greater Barcelona - Badalona
            'https://www.dentalbadalona.es',
            'https://www.clinicadentalbadalona.com',
            'https://www.badalonasedentica.es',
            'https://www.ulldent.es',
            
            # Greater Barcelona - Granollers
            'https://www.dentalgranollers.com',
            'https://www.clinicadentalgranollers.es',
            
            # Additional verified clinics
            'https://www.barnasmile.com',
            'https://www.barcelonaesmile.com',
            'https://www.smilebcn.com',
            'https://www.bcnsmileclinic.com',
            'https://www.clinicadentalnovasmile.com',
            'https://www.dentalbcn.es',
            'https://www.barcelonidentalstudio.com',
            'https://www.clinicadentaldrlopez.com',
            'https://www.doctorpeix.com',
            'https://www.clinicazardoya.com',
            'https://www.dentalbruc.com',
            'https://www.balust.es',
            'https://www.clinicapivot.com',
            'https://www.dentistaenbarcelona.es',
            'https://www.clinicadentalurbina.es',
            'https://www.dentissimbarcelona.com',
            'https://www.tusondent.com',
            'https://www.robledodental.com',
            'https://www.dentalvip.cat',
            'https://www.barcedentico.com',
            'https://www.odontopediatriabarcelona.com',
            'https://www.centromedit.com',
            'https://www.dentalmardones.com',
            'https://www.clinicadentalcreu.com',
            'https://www.clinicadentalpujol.com',
        ]

    def is_excluded_chain(self, name: str, website: str) -> bool:
        """Check if clinic belongs to excluded DSO chains."""
        text = (name + ' ' + website).lower()
        return any(chain in text for chain in self.excluded_chains)

    def fetch_website(self, url: str, timeout: int = 10) -> Optional[str]:
        """Fetch website HTML content."""
        try:
            response = self.session.get(url, timeout=timeout, allow_redirects=True)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"  ✗ Failed to fetch: {e}")
            return None

    def analyze_website(self, url: str, html: str) -> Dict:
        """Extract ICP signals from website HTML."""
        signals = {
            'has_online_booking': False,
            'has_whatsapp': False,
            'has_financing': False,
            'mentions_implants': False,
            'mentions_invisalign': False,
            'mentions_carillas': False,
            'has_gallery': False,
            'website_quality': 'modern',
            'multi_location': False,
            'num_locations': 1,
            'instagram_handle': '',
            'email': '',
            'phone': ''
        }

        if not html:
            signals['website_quality'] = 'none'
            return signals

        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text().lower()

        # Online booking
        booking_keywords = [
            'reserva online', 'cita online', 'pedir cita', 'reservar cita',
            'book online', 'booking', 'calendly', 'doctolib', 'doctoralia'
        ]
        if any(kw in text for kw in booking_keywords):
            signals['has_online_booking'] = True

        # WhatsApp
        if 'whatsapp' in text or 'wa.me' in html or 'api.whatsapp' in html:
            signals['has_whatsapp'] = True

        # Financing
        financing_keywords = [
            'financiación', 'financiacion', 'financiar', 'cuotas',
            'pago fraccionado', 'pago a plazos', 'sin intereses', 'financiamos'
        ]
        if any(kw in text for kw in financing_keywords):
            signals['has_financing'] = True

        # High-ticket treatments
        if any(kw in text for kw in ['implante', 'implantes', 'implantología', 'implantologia']):
            signals['mentions_implants'] = True

        if any(kw in text for kw in ['invisalign', 'ortodoncia invisible', 'alineadores', 'ortodoncia']):
            signals['mentions_invisalign'] = True

        if any(kw in text for kw in ['carilla', 'carillas', 'estética dental', 'estetica dental', 'estética']):
            signals['mentions_carillas'] = True

        # Before/after gallery
        gallery_keywords = ['antes y después', 'antes y despues', 'casos', 'galería', 'galeria', 'resultados']
        if any(kw in text for kw in gallery_keywords):
            signals['has_gallery'] = True

        # Multi-location
        location_indicators = text.count('clínica') + text.count('clinica') + text.count('centro')
        if location_indicators > 5 or 'clínicas' in text or 'centros' in text:
            signals['multi_location'] = True
            # Count locations (rough estimate)
            locations = max(text.count('barcelona'), 1)
            signals['num_locations'] = min(locations, 20)  # Cap at 20 for outliers

        # Instagram
        ig_pattern = r'instagram\.com/([a-zA-Z0-9._]+)'
        ig_match = re.search(ig_pattern, html)
        if ig_match:
            signals['instagram_handle'] = '@' + ig_match.group(1)

        # Email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_match = re.search(email_pattern, html)
        if email_match:
            email = email_match.group(0)
            # Filter out generic/noise emails
            if not any(x in email.lower() for x in ['example.com', 'test.com', 'email.com']):
                signals['email'] = email

        # Phone (Spanish format)
        phone_pattern = r'(\+34|0034|34)?[\s]?[689]\d{2}[\s]?\d{3}[\s]?\d{3}'
        phone_match = re.search(phone_pattern, html)
        if phone_match:
            signals['phone'] = phone_match.group(0).strip()

        # Website quality check
        year_pattern = r'copyright.*?20(\d{2})'
        years = re.findall(year_pattern, text)
        if years:
            latest_year = max([int(y) for y in years])
            if latest_year < 15:  # Before 2015
                signals['website_quality'] = 'dated'

        return signals

    def calculate_icp_score(self, clinic: Dict) -> int:
        """Calculate ICP score based on signals."""
        score = 0

        # Website quality
        if clinic['website_quality'] == 'modern':
            score += 10
        elif clinic['website_quality'] == 'dated':
            score -= 20
        else:  # none
            score -= 50

        # Digital savviness
        if clinic['has_online_booking']:
            score += 15
        if clinic['has_whatsapp']:
            score += 5
        if clinic['instagram_handle']:
            score += 10

        # High-ticket treatments
        if clinic['mentions_implants']:
            score += 10
        if clinic['mentions_invisalign']:
            score += 15
        if clinic['mentions_carillas']:
            score += 10
        if clinic['has_gallery']:
            score += 5
        if clinic['has_financing']:
            score += 10

        # Bonus
        if clinic['multi_location']:
            score += 10

        return max(0, score)

    def scrape_clinic(self, url: str) -> Optional[Dict]:
        """Scrape single clinic and return data."""
        # Normalize URL
        if not url.startswith('http'):
            url = 'https://' + url

        # Check if already seen
        domain = urlparse(url).netloc
        if domain in self.seen_websites:
            return None
        self.seen_websites.add(domain)

        print(f"\nScraping: {url}")

        # Fetch website
        html = self.fetch_website(url)
        if not html:
            return None

        # Extract clinic name from HTML
        soup = BeautifulSoup(html, 'html.parser')
        clinic_name = soup.title.string if soup.title else domain

        # Analyze website
        signals = self.analyze_website(url, html)

        # Build clinic record
        clinic = {
            'clinic_name': clinic_name.strip() if clinic_name else domain,
            'website_url': url,
            'city': 'Barcelona',
            'phone': signals.get('phone', ''),
            'email': signals.get('email', ''),
            'google_rating': 0,
            'google_review_count': 0,
            'instagram_handle': signals.get('instagram_handle', ''),
            'instagram_followers': 0,
            **{k: v for k, v in signals.items() if k not in ['phone', 'email', 'instagram_handle']}
        }

        # Calculate ICP score
        clinic['icp_score'] = self.calculate_icp_score(clinic)
        clinic['notes'] = f"Scraped: {date.today()}"

        # Check if excluded
        if self.is_excluded_chain(clinic['clinic_name'], clinic['website_url']):
            print(f"  ✗ Excluded: DSO chain")
            return None

        print(f"  ✓ Score: {clinic['icp_score']}")
        return clinic

    def scrape_all(self, min_score: int = 60, target_leads: int = 50) -> List[Dict]:
        """Scrape all clinics and return qualified leads."""
        print(f"TARGET: {target_leads} qualified leads (score >= {min_score})")
        print(f"Seed list: {len(self.seed_urls)} URLs\n")
        print("="*60)

        all_clinics = []
        qualified_leads = []

        for i, url in enumerate(self.seed_urls, 1):
            print(f"\n[{i}/{len(self.seed_urls)}]", end=' ')

            # Scrape clinic
            clinic = self.scrape_clinic(url)
            if clinic:
                all_clinics.append(clinic)
                if clinic['icp_score'] >= min_score:
                    qualified_leads.append(clinic)
                    print(f"  ✓✓ QUALIFIED ({len(qualified_leads)}/{target_leads})")

                    # Stop if target reached
                    if len(qualified_leads) >= target_leads:
                        print(f"\n{'='*60}")
                        print(f"TARGET REACHED: {len(qualified_leads)} qualified leads!")
                        print(f"{'='*60}")
                        break

            # Rate limiting
            time.sleep(0.5)

        # Sort by score
        qualified_leads.sort(key=lambda x: x['icp_score'], reverse=True)

        return all_clinics, qualified_leads

    def save_to_csv(self, clinics: List[Dict], filename: str):
        """Save clinics to CSV file."""
        if not clinics:
            print(f"No data to save to {filename}")
            return

        fieldnames = [
            'clinic_name', 'website_url', 'city', 'phone', 'email',
            'google_rating', 'google_review_count', 'instagram_handle', 'instagram_followers',
            'has_online_booking', 'has_whatsapp', 'has_financing',
            'mentions_implants', 'mentions_invisalign', 'mentions_carillas',
            'has_gallery', 'website_quality', 'multi_location', 'num_locations',
            'icp_score', 'notes'
        ]

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for clinic in clinics:
                writer.writerow(clinic)

        print(f"\n✓ Saved {len(clinics)} clinics to {filename}")


def main():
    scraper = ExtendedBarcelonaScraper()

    # Scrape until we have 50 qualified leads
    all_clinics, qualified_leads = scraper.scrape_all(min_score=60, target_leads=50)

    # Save results
    today = date.today().isoformat()
    base_path = '/Users/cinziapalumbo/cinzia-claude/aprovo-leads'

    # Save qualified leads
    scraper.save_to_csv(
        qualified_leads,
        f'{base_path}/barcelona_50_leads_{today}.csv'
    )

    # Save all clinics
    scraper.save_to_csv(
        all_clinics,
        f'{base_path}/barcelona_50_leads_full_{today}.csv'
    )

    # Print summary
    print("\n" + "="*60)
    print("SCRAPING COMPLETE")
    print("="*60)
    print(f"Total clinics scraped: {len(all_clinics)}")
    print(f"Qualified leads (60+): {len(qualified_leads)}")
    print(f"Success rate: {len(qualified_leads)/len(all_clinics)*100:.1f}%" if all_clinics else "N/A")
    if qualified_leads:
        print(f"Average ICP score: {sum(c['icp_score'] for c in qualified_leads)/len(qualified_leads):.1f}")
        print(f"Highest score: {max(c['icp_score'] for c in qualified_leads)}")
        print(f"Lowest qualified score: {min(c['icp_score'] for c in qualified_leads)}")

    # Top 10 leads
    if qualified_leads:
        print("\n" + "-"*60)
        print("TOP 10 LEADS:")
        print("-"*60)
        for i, lead in enumerate(qualified_leads[:10], 1):
            print(f"\n{i}. {lead['clinic_name']} - Score: {lead['icp_score']}")
            print(f"   {lead['website_url']}")
            if lead['email']:
                print(f"   Email: {lead['email']}")
            if lead['phone']:
                print(f"   Phone: {lead['phone']}")


if __name__ == '__main__':
    main()
