#!/usr/bin/env python3
"""
SEO Fixer for Trust SoCal Website
Automatically fixes common SEO issues
"""

import os
import re
from bs4 import BeautifulSoup

class SEOFixer:
    def __init__(self, base_path):
        self.base_path = base_path
        self.changes_made = []

    def get_html_files(self):
        """Get all HTML files in the directory"""
        html_files = []
        for root, dirs, files in os.walk(self.base_path):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.endswith('.html') and not file.endswith('-backup.html'):
                    html_files.append(os.path.join(root, file))
        return html_files

    def shorten_title(self, title, max_length=60):
        """Intelligently shorten a title to max_length chars"""
        if len(title) <= max_length:
            return title

        # Common patterns to remove or shorten
        # Remove "Trust SoCal" duplicates, keep one at end
        title = re.sub(r'\s*\|\s*Trust SoCal\s*-\s*', ' | ', title)
        title = re.sub(r'\s*-\s*Trust SoCal\s*\|', ' |', title)

        # Shorten common phrases
        replacements = [
            ('Joint Commission Accredited', 'Accredited'),
            ('Drug and Alcohol', 'Drug & Alcohol'),
            ('Addiction Treatment', 'Treatment'),
            ('Rehabilitation Center', 'Rehab'),
            ('Orange County', 'OC'),
            ('Southern California', 'SoCal'),
            (' Treatment Center', ''),
            (' Recovery Center', ''),
        ]

        for old, new in replacements:
            if len(title) <= max_length:
                break
            title = title.replace(old, new)

        # If still too long, truncate intelligently at word boundary
        if len(title) > max_length:
            # Try to keep "Trust SoCal" or brand at end
            if '|' in title:
                parts = title.split('|')
                main_part = parts[0].strip()
                brand_part = parts[-1].strip() if len(parts) > 1 else ''

                # Calculate available space
                brand_space = len(brand_part) + 3  # " | brand"
                main_max = max_length - brand_space

                if main_max > 20:
                    # Truncate main part at word boundary
                    if len(main_part) > main_max:
                        main_part = main_part[:main_max-3].rsplit(' ', 1)[0] + '...'
                    title = f"{main_part} | {brand_part}"
                else:
                    title = title[:max_length-3].rsplit(' ', 1)[0] + '...'
            else:
                title = title[:max_length-3].rsplit(' ', 1)[0] + '...'

        return title.strip()

    def shorten_meta_description(self, desc, max_length=155):
        """Intelligently shorten a meta description to max_length chars"""
        if len(desc) <= max_length:
            return desc

        # Remove redundant phrases
        replacements = [
            ('Joint Commission accredited ', ''),
            ('Joint Commission Accredited ', ''),
            ('drug and alcohol ', 'addiction '),
            ('Drug and Alcohol ', 'Addiction '),
            ('rehabilitation center', 'rehab'),
            ('treatment center', 'treatment'),
            ('Orange County, California', 'Orange County'),
            ('Southern California', 'SoCal'),
            ('Call us today', 'Call'),
            ('Contact us today', 'Call'),
            ('Learn more about', 'Learn about'),
            ('We offer ', ''),
            ('Our ', ''),
            ('including ', 'with '),
        ]

        for old, new in replacements:
            if len(desc) <= max_length:
                break
            desc = desc.replace(old, new)

        # If still too long, truncate at sentence or phrase boundary
        if len(desc) > max_length:
            # Try to end at a period
            truncated = desc[:max_length]
            last_period = truncated.rfind('.')
            last_comma = truncated.rfind(',')

            if last_period > max_length - 40:
                desc = desc[:last_period + 1]
            elif last_comma > max_length - 30:
                desc = desc[:last_comma] + '.'
            else:
                desc = desc[:max_length-3].rsplit(' ', 1)[0] + '...'

        return desc.strip()

    def fix_file(self, filepath):
        """Fix SEO issues in a single HTML file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'lxml')
        rel_path = os.path.relpath(filepath, self.base_path)
        changes = []

        # Fix title
        title_tag = soup.find('title')
        if title_tag and len(title_tag.get_text().strip()) > 60:
            old_title = title_tag.get_text().strip()
            new_title = self.shorten_title(old_title)
            if new_title != old_title:
                title_tag.string = new_title
                changes.append(f"Title: {len(old_title)} -> {len(new_title)} chars")

        # Also fix og:title and twitter:title
        for meta_name in ['og:title', 'twitter:title']:
            meta_tag = soup.find('meta', attrs={'property': meta_name})
            if meta_tag and meta_tag.get('content'):
                old_content = meta_tag['content']
                if len(old_content) > 60:
                    new_content = self.shorten_title(old_content)
                    if new_content != old_content:
                        meta_tag['content'] = new_content

        # Fix meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            old_desc = meta_desc['content'].strip()
            if len(old_desc) > 160:
                new_desc = self.shorten_meta_description(old_desc)
                if new_desc != old_desc:
                    meta_desc['content'] = new_desc
                    changes.append(f"Meta desc: {len(old_desc)} -> {len(new_desc)} chars")

        # Also fix og:description and twitter:description
        for meta_name in ['og:description', 'twitter:description']:
            meta_tag = soup.find('meta', attrs={'property': meta_name})
            if meta_tag and meta_tag.get('content'):
                old_content = meta_tag['content']
                if len(old_content) > 160:
                    new_content = self.shorten_meta_description(old_content)
                    if new_content != old_content:
                        meta_tag['content'] = new_content

        # Fix meta title tag (name="title")
        meta_title = soup.find('meta', attrs={'name': 'title'})
        if meta_title and meta_title.get('content'):
            old_content = meta_title['content']
            if len(old_content) > 60:
                new_content = self.shorten_title(old_content)
                if new_content != old_content:
                    meta_title['content'] = new_content

        if changes:
            # Write the modified content back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            self.changes_made.append({
                'file': rel_path,
                'changes': changes
            })
            return True
        return False

    def fix_all(self):
        """Fix all HTML files"""
        html_files = self.get_html_files()
        print(f"\n🔧 Processing {len(html_files)} HTML files...\n")

        fixed_count = 0
        for filepath in html_files:
            rel_path = os.path.relpath(filepath, self.base_path)
            if self.fix_file(filepath):
                print(f"  ✓ Fixed: {rel_path}")
                fixed_count += 1

        print(f"\n✅ Fixed {fixed_count} files")
        print(f"📋 Total changes: {sum(len(c['changes']) for c in self.changes_made)}")

        return self.changes_made


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fixer = SEOFixer(script_dir)
    fixer.fix_all()
