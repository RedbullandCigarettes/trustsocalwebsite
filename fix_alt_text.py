#!/usr/bin/env python3
"""
Fix missing alt text on images
"""

import os
import re
from bs4 import BeautifulSoup

def get_html_files(base_path):
    """Get all HTML files in the directory"""
    html_files = []
    for root, dirs, files in os.walk(base_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.html') and not file.endswith('-backup.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def generate_alt_text(src, page_context=""):
    """Generate appropriate alt text based on image filename and context"""
    if not src:
        return "Trust SoCal image"

    # Extract filename from src
    filename = os.path.basename(src).lower()
    filename_no_ext = os.path.splitext(filename)[0]

    # Common image mappings for Trust SoCal
    alt_mappings = {
        'logo': 'Trust SoCal Logo',
        'hero': 'Trust SoCal addiction treatment facility in Orange County',
        'hero-sunset': 'Sunset view at Trust SoCal rehab center Orange County',
        'therapy-session': 'Individual therapy session at Trust SoCal',
        'counseling': 'Addiction counseling session',
        'group-support': 'Group therapy support session',
        'meditation-room': 'Meditation and mindfulness room',
        'meditation': 'Meditation therapy for addiction recovery',
        'facility': 'Trust SoCal treatment facility',
        'facility-kitchen': 'Gourmet dining facility at Trust SoCal',
        'pool': 'Wellness pool at Trust SoCal',
        'exterior': 'Trust SoCal facility exterior',
        'bedroom': 'Private residential suite',
        'living-room': 'Comfortable living area',
        'yoga': 'Yoga therapy session',
        'fitness': 'Fitness center',
        'garden': 'Peaceful garden at treatment center',
        'beach': 'Orange County beach near treatment facility',
        'team': 'Trust SoCal medical team',
        'doctor': 'Medical professional at Trust SoCal',
        'nurse': 'Nursing staff providing care',
        'detox': 'Medical detox program',
        'family': 'Family therapy program',
    }

    # Check for direct mappings
    for key, alt in alt_mappings.items():
        if key in filename_no_ext:
            return alt

    # Check for IMG_ pattern (common for photos)
    if filename_no_ext.startswith('img_'):
        return 'Trust SoCal treatment facility'

    # Generate from filename by replacing common separators
    clean_name = filename_no_ext.replace('-', ' ').replace('_', ' ')
    clean_name = re.sub(r'\d+', '', clean_name).strip()  # Remove numbers

    if clean_name:
        # Title case and add context
        return f"{clean_name.title()} at Trust SoCal"

    return "Trust SoCal addiction treatment"

def fix_alt_text(filepath, base_path):
    """Fix missing alt text in a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'lxml')
    rel_path = os.path.relpath(filepath, base_path)

    fixed_count = 0
    images = soup.find_all('img')

    for img in images:
        alt = img.get('alt', '').strip()
        src = img.get('src', '')

        if not alt:
            # Generate alt text
            new_alt = generate_alt_text(src, rel_path)
            img['alt'] = new_alt
            fixed_count += 1

    if fixed_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return fixed_count

    return 0


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = get_html_files(script_dir)

    print(f"\n🔧 Checking {len(html_files)} HTML files for missing alt text...\n")

    total_fixed = 0
    files_fixed = 0

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, script_dir)
        count = fix_alt_text(filepath, script_dir)
        if count > 0:
            print(f"  ✓ Fixed {count} images in: {rel_path}")
            total_fixed += count
            files_fixed += 1

    print(f"\n✅ Fixed {total_fixed} images across {files_fixed} files")


if __name__ == "__main__":
    main()
