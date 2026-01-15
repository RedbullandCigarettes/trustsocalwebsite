#!/usr/bin/env python3
"""
Simple SEO Crawler for Trust SoCal Website
Analyzes on-page SEO elements, broken links, and content quality
"""

import os
import re
import json
import time
from urllib.parse import urljoin, urlparse
from collections import defaultdict
from bs4 import BeautifulSoup
import requests

class SEOCrawler:
    def __init__(self, base_path, base_url="https://trustsocal.com"):
        self.base_path = base_path
        self.base_url = base_url
        self.results = {
            "pages": [],
            "issues": [],
            "summary": {}
        }
        self.crawled = set()

    def get_html_files(self):
        """Get all HTML files in the directory"""
        html_files = []
        for root, dirs, files in os.walk(self.base_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.endswith('.html'):
                    html_files.append(os.path.join(root, file))
        return html_files

    def analyze_page(self, filepath):
        """Analyze a single HTML page for SEO elements"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'lxml')
        rel_path = os.path.relpath(filepath, self.base_path)

        page_data = {
            "file": rel_path,
            "url": urljoin(self.base_url, rel_path.replace('.html', '') if rel_path != 'index.html' else ''),
            "title": None,
            "title_length": 0,
            "meta_description": None,
            "meta_description_length": 0,
            "h1_tags": [],
            "h2_tags": [],
            "canonical": None,
            "word_count": 0,
            "internal_links": [],
            "external_links": [],
            "images_without_alt": [],
            "images_total": 0,
            "schema_types": [],
            "issues": []
        }

        # Title
        title_tag = soup.find('title')
        if title_tag:
            page_data["title"] = title_tag.get_text().strip()
            page_data["title_length"] = len(page_data["title"])
        else:
            page_data["issues"].append("Missing <title> tag")

        # Meta Description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            page_data["meta_description"] = meta_desc['content'].strip()
            page_data["meta_description_length"] = len(page_data["meta_description"])
        else:
            page_data["issues"].append("Missing meta description")

        # Canonical URL
        canonical = soup.find('link', attrs={'rel': 'canonical'})
        if canonical:
            page_data["canonical"] = canonical.get('href')
        else:
            page_data["issues"].append("Missing canonical URL")

        # H1 Tags
        h1_tags = soup.find_all('h1')
        page_data["h1_tags"] = [h1.get_text().strip() for h1 in h1_tags]
        if len(h1_tags) == 0:
            page_data["issues"].append("Missing H1 tag")
        elif len(h1_tags) > 1:
            page_data["issues"].append(f"Multiple H1 tags ({len(h1_tags)})")

        # H2 Tags
        h2_tags = soup.find_all('h2')
        page_data["h2_tags"] = [h2.get_text().strip() for h2 in h2_tags]

        # Word Count (body text only)
        body = soup.find('body')
        if body:
            text = body.get_text(separator=' ', strip=True)
            words = re.findall(r'\b\w+\b', text)
            page_data["word_count"] = len(words)
            if page_data["word_count"] < 300:
                page_data["issues"].append(f"Low word count ({page_data['word_count']} words)")

        # Links
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:'):
                continue
            if href.startswith('http') and self.base_url not in href:
                page_data["external_links"].append(href)
            else:
                page_data["internal_links"].append(href)

        # Images
        images = soup.find_all('img')
        page_data["images_total"] = len(images)
        for img in images:
            if not img.get('alt') or img.get('alt').strip() == '':
                page_data["images_without_alt"].append(img.get('src', 'unknown'))

        if page_data["images_without_alt"]:
            page_data["issues"].append(f"{len(page_data['images_without_alt'])} images missing alt text")

        # Schema/Structured Data
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                schema = json.loads(script.string)
                if isinstance(schema, dict):
                    schema_type = schema.get('@type', 'Unknown')
                    if isinstance(schema_type, list):
                        page_data["schema_types"].extend(schema_type)
                    else:
                        page_data["schema_types"].append(schema_type)
            except:
                pass

        # Title length checks
        if page_data["title_length"] > 0:
            if page_data["title_length"] < 30:
                page_data["issues"].append(f"Title too short ({page_data['title_length']} chars)")
            elif page_data["title_length"] > 60:
                page_data["issues"].append(f"Title too long ({page_data['title_length']} chars)")

        # Meta description length checks
        if page_data["meta_description_length"] > 0:
            if page_data["meta_description_length"] < 120:
                page_data["issues"].append(f"Meta description too short ({page_data['meta_description_length']} chars)")
            elif page_data["meta_description_length"] > 160:
                page_data["issues"].append(f"Meta description too long ({page_data['meta_description_length']} chars)")

        return page_data

    def crawl(self):
        """Crawl all HTML files and analyze them"""
        html_files = self.get_html_files()
        print(f"\n🔍 Found {len(html_files)} HTML files to analyze...\n")

        for filepath in html_files:
            print(f"  Analyzing: {os.path.relpath(filepath, self.base_path)}")
            page_data = self.analyze_page(filepath)
            self.results["pages"].append(page_data)

            for issue in page_data["issues"]:
                self.results["issues"].append({
                    "file": page_data["file"],
                    "issue": issue
                })

        # Generate summary
        self.results["summary"] = {
            "total_pages": len(self.results["pages"]),
            "total_issues": len(self.results["issues"]),
            "pages_with_issues": len([p for p in self.results["pages"] if p["issues"]]),
            "pages_without_issues": len([p for p in self.results["pages"] if not p["issues"]]),
            "avg_word_count": sum(p["word_count"] for p in self.results["pages"]) // max(len(self.results["pages"]), 1),
            "total_images": sum(p["images_total"] for p in self.results["pages"]),
            "images_missing_alt": sum(len(p["images_without_alt"]) for p in self.results["pages"]),
        }

        return self.results

    def print_report(self):
        """Print a formatted SEO report"""
        print("\n" + "="*60)
        print("🔎 SEO AUDIT REPORT - Trust SoCal")
        print("="*60)

        # Summary
        s = self.results["summary"]
        print(f"\n📊 SUMMARY")
        print(f"   Total Pages: {s['total_pages']}")
        print(f"   Pages with Issues: {s['pages_with_issues']}")
        print(f"   Total Issues Found: {s['total_issues']}")
        print(f"   Average Word Count: {s['avg_word_count']}")
        print(f"   Total Images: {s['total_images']}")
        print(f"   Images Missing Alt: {s['images_missing_alt']}")

        # Issues by type
        issue_counts = defaultdict(int)
        for issue in self.results["issues"]:
            # Normalize issue type
            issue_text = issue["issue"]
            if "Missing" in issue_text:
                issue_counts["Missing Elements"] += 1
            elif "too short" in issue_text:
                issue_counts["Content Too Short"] += 1
            elif "too long" in issue_text:
                issue_counts["Content Too Long"] += 1
            elif "Multiple H1" in issue_text:
                issue_counts["Multiple H1 Tags"] += 1
            elif "images missing alt" in issue_text:
                issue_counts["Missing Alt Text"] += 1
            elif "Low word count" in issue_text:
                issue_counts["Low Word Count"] += 1
            else:
                issue_counts["Other"] += 1

        print(f"\n⚠️  ISSUES BY TYPE")
        for issue_type, count in sorted(issue_counts.items(), key=lambda x: -x[1]):
            print(f"   {issue_type}: {count}")

        # Detailed issues
        print(f"\n📋 DETAILED ISSUES")
        for page in self.results["pages"]:
            if page["issues"]:
                print(f"\n   📄 {page['file']}")
                for issue in page["issues"]:
                    print(f"      ⚠️  {issue}")

        # Pages without issues
        good_pages = [p for p in self.results["pages"] if not p["issues"]]
        if good_pages:
            print(f"\n✅ PAGES WITH NO ISSUES ({len(good_pages)})")
            for page in good_pages:
                print(f"   ✓ {page['file']}")

        # Schema coverage
        print(f"\n🏷️  SCHEMA MARKUP COVERAGE")
        pages_with_schema = [p for p in self.results["pages"] if p["schema_types"]]
        print(f"   Pages with Schema: {len(pages_with_schema)}/{s['total_pages']}")
        schema_types_used = set()
        for page in self.results["pages"]:
            schema_types_used.update(page["schema_types"])
        if schema_types_used:
            print(f"   Schema Types: {', '.join(sorted(schema_types_used))}")

        print("\n" + "="*60)
        print("✅ Audit Complete!")
        print("="*60 + "\n")

    def save_report(self, output_file="seo_report.json"):
        """Save the full report to JSON"""
        output_path = os.path.join(self.base_path, output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2)
        print(f"📁 Full report saved to: {output_file}")


if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    crawler = SEOCrawler(script_dir)
    crawler.crawl()
    crawler.print_report()
    crawler.save_report()
