#!/usr/bin/env python3
"""
Count the number of physical locations for each dental clinic.
Adds num_locations column to the CSV files.
"""

import csv
import re
import time
from typing import Dict, Optional
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup


class LocationCounter:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        })
        self.session.verify = False
        requests.packages.urllib3.disable_warnings()

    def find_locations_page(self, base_url: str, soup: BeautifulSoup) -> Optional[str]:
        """Find the locations/clinics page URL."""
        # Common location page keywords in Spanish and English
        location_keywords = [
            'clinicas', 'clínicas', 'centros', 'sedes', 'locations',
            'ubicaciones', 'nuestras clinicas', 'nuestros centros',
            'donde estamos', 'dónde estamos', 'encuéntranos'
        ]

        # Check all links on the page
        for link in soup.find_all('a', href=True):
            href = link.get('href', '').lower()
            text = link.get_text().lower()

            # Check if link text or href contains location keywords
            if any(kw in text or kw in href for kw in location_keywords):
                # Construct full URL
                full_url = urljoin(base_url, link['href'])
                return full_url

        return None

    def count_locations_on_page(self, html: str, text: str) -> int:
        """Count location indicators on a page."""
        count = 0

        # Method 1: Look for address patterns (multiple Spanish addresses)
        # Spanish address pattern: street name + number + postal code + city
        address_pattern = r'(?:Calle|Carrer|Avda|Avenida|Passeig|C/|Av\.|Plaza|Pl\.)[^<\n]{10,80}(?:\d{5}|Barcelona|Madrid|Valencia|Sevilla)'
        addresses = re.findall(address_pattern, text, re.IGNORECASE)
        if addresses:
            count = max(count, len(addresses))

        # Method 2: Look for Google Maps iframes (each location usually has a map)
        maps_iframes = re.findall(r'maps\.google\.com/maps\?.*?embed|google\.com/maps/embed', html)
        if maps_iframes:
            count = max(count, len(maps_iframes))

        # Method 3: Look for phone number patterns (multiple unique phone numbers)
        phone_pattern = r'(?:\+34|34)?\s*[96]\d{2}\s*\d{3}\s*\d{3}'
        phones = set(re.findall(phone_pattern, text))
        if len(phones) > 1:
            count = max(count, len(phones))

        # Method 4: Count explicit location headers (h2, h3 with city names)
        soup = BeautifulSoup(html, 'html.parser')
        location_headers = soup.find_all(['h2', 'h3', 'h4'], string=re.compile(
            r'Barcelona|Madrid|Valencia|Sevilla|Málaga|Bilbao|Terrassa|Sabadell|Badalona|Hospitalet|Mataró',
            re.IGNORECASE
        ))
        if location_headers:
            count = max(count, len(location_headers))

        # Method 5: Look for structured location lists
        # Find divs/sections that contain location information
        location_sections = soup.find_all(['div', 'section'], class_=re.compile(
            r'location|clinic|centro|sede', re.IGNORECASE
        ))
        if location_sections:
            count = max(count, len(location_sections))

        return count

    def get_location_count(self, url: str) -> int:
        """Get the number of locations for a clinic."""
        try:
            print(f"  Checking: {url[:60]}")

            # Get main page
            response = self.session.get(url, timeout=10, allow_redirects=True)
            if response.status_code != 200:
                print(f"    ✗ HTTP {response.status_code}")
                return 1  # Default to 1 location

            soup = BeautifulSoup(response.content, 'html.parser')
            html = str(soup)
            text = soup.get_text()

            # First, try to find a dedicated locations page
            locations_page_url = self.find_locations_page(url, soup)

            if locations_page_url and locations_page_url != url:
                print(f"    Found locations page: {locations_page_url[:50]}")
                try:
                    loc_response = self.session.get(locations_page_url, timeout=10)
                    if loc_response.status_code == 200:
                        loc_soup = BeautifulSoup(loc_response.content, 'html.parser')
                        count = self.count_locations_on_page(str(loc_soup), loc_soup.get_text())
                        if count > 0:
                            print(f"    ✓ Found {count} locations")
                            return count
                except:
                    pass

            # If no dedicated page or count failed, analyze main page
            count = self.count_locations_on_page(html, text)

            if count == 0:
                # Default to 1 if we can't find multiple locations
                count = 1

            print(f"    ✓ {count} location{'s' if count != 1 else ''}")
            return count

        except Exception as e:
            print(f"    ✗ Error: {str(e)[:50]}")
            return 1  # Default to 1 location on error

    def update_csv_with_locations(self, input_file: str, output_file: str):
        """Read CSV, add num_locations column, write updated CSV."""
        print(f"\nProcessing: {input_file}")
        print("=" * 70)

        # Read existing CSV
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            fieldnames = reader.fieldnames

        # Add num_locations to fieldnames (insert after multi_location)
        if 'num_locations' not in fieldnames:
            multi_loc_index = fieldnames.index('multi_location')
            fieldnames = list(fieldnames)
            fieldnames.insert(multi_loc_index + 1, 'num_locations')

        # Process each row
        for i, row in enumerate(rows, 1):
            print(f"\n[{i}/{len(rows)}] {row['clinic_name'][:50]}")

            website = row.get('website_url', '')
            if website:
                num_locations = self.get_location_count(website)
                row['num_locations'] = num_locations
            else:
                row['num_locations'] = 1  # Default to 1 if no website

            time.sleep(1)  # Rate limiting

        # Write updated CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"\n✓ Updated CSV saved: {output_file}")
        print(f"  Added num_locations column to {len(rows)} clinics")

        # Summary stats
        multi_location_clinics = [r for r in rows if int(r['num_locations']) > 1]
        if multi_location_clinics:
            print(f"\n📊 Multi-location clinics: {len(multi_location_clinics)}")
            for clinic in sorted(multi_location_clinics, key=lambda x: -int(x['num_locations']))[:5]:
                print(f"  • {clinic['clinic_name'][:45]} - {clinic['num_locations']} locations")


def main():
    counter = LocationCounter()

    # Update both CSV files
    files = [
        ('aprovo_leads_barcelona_2026-01-21.csv', 'aprovo_leads_barcelona_2026-01-21_updated.csv'),
        ('aprovo_leads_barcelona_full_2026-01-21.csv', 'aprovo_leads_barcelona_full_2026-01-21_updated.csv'),
    ]

    for input_file, output_file in files:
        counter.update_csv_with_locations(input_file, output_file)
        print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()
