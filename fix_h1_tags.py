#!/usr/bin/env python3
"""
Fix multiple H1 tags - change logo H1 to span
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

def fix_h1_tags(filepath, base_path):
    """Fix multiple H1 tags by changing logo H1 to span"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'lxml')
    rel_path = os.path.relpath(filepath, base_path)

    h1_tags = soup.find_all('h1')

    if len(h1_tags) <= 1:
        return False  # No fix needed

    fixed = False

    # Find the H1 in the logo/header area (usually contains "Trust SoCal" only)
    for h1 in h1_tags:
        text = h1.get_text().strip()

        # Check if this is the logo H1 (short text, in header/logo div)
        parent_classes = []
        for parent in h1.parents:
            if parent.get('class'):
                parent_classes.extend(parent.get('class'))

        is_logo_h1 = (
            text == "Trust SoCal" or
            'logo' in ' '.join(parent_classes).lower() or
            'header' in ' '.join(parent_classes).lower() and len(text) < 20
        )

        if is_logo_h1 and text == "Trust SoCal":
            # Change H1 to span with class for styling
            new_tag = soup.new_tag('span')
            new_tag['class'] = 'logo-title'
            new_tag.string = text

            # Preserve any existing style attribute
            if h1.get('style'):
                new_tag['style'] = h1['style']

            h1.replace_with(new_tag)
            fixed = True
            break  # Only fix one logo H1

    if fixed:
        # Write the modified content back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True

    return False


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = get_html_files(script_dir)

    print(f"\n🔧 Checking {len(html_files)} HTML files for multiple H1 tags...\n")

    fixed_count = 0
    for filepath in html_files:
        rel_path = os.path.relpath(filepath, script_dir)
        if fix_h1_tags(filepath, script_dir):
            print(f"  ✓ Fixed: {rel_path}")
            fixed_count += 1

    print(f"\n✅ Fixed {fixed_count} files with multiple H1 tags")


if __name__ == "__main__":
    main()
