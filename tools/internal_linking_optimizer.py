#!/usr/bin/env python3
"""
Internal Linking Optimizer for Trust SoCal
==========================================
Analyzes internal linking structure and suggests improvements.
"""

import os
import re
import json
from bs4 import BeautifulSoup
import glob
from collections import defaultdict

class InternalLinkingOptimizer:
    """Optimize internal linking for better SEO."""

    def __init__(self, site_path):
        self.site_path = site_path
        self.pages = {}
        self.link_graph = defaultdict(set)
        self.incoming_links = defaultdict(list)
        self.suggested_links = []

        # Define topic clusters for linking
        self.topic_clusters = {
            'detox': {
                'keywords': ['detox', 'withdrawal', 'medical detox', 'detoxification'],
                'hub': 'services/medical-detox.html',
                'related': ['treatment/alcohol-addiction.html', 'treatment/opioid-addiction.html',
                           'treatment/heroin-addiction.html', 'treatment/fentanyl-addiction.html']
            },
            'residential': {
                'keywords': ['residential', 'inpatient', 'live-in', '24/7 care'],
                'hub': 'services/residential-treatment.html',
                'related': ['services/medical-detox.html', 'services/php.html']
            },
            'outpatient': {
                'keywords': ['outpatient', 'iop', 'php', 'partial hospitalization', 'intensive outpatient'],
                'hub': 'services/iop.html',
                'related': ['services/php.html', 'services/aftercare.html', 'services/sober-living.html']
            },
            'alcohol': {
                'keywords': ['alcohol', 'alcoholism', 'drinking', 'beer', 'wine', 'liquor'],
                'hub': 'treatment/alcohol-addiction.html',
                'related': ['services/medical-detox.html', 'alcohol-rehab-orange-county.html']
            },
            'opioids': {
                'keywords': ['opioid', 'heroin', 'fentanyl', 'painkiller', 'prescription drug'],
                'hub': 'treatment/opioid-addiction.html',
                'related': ['treatment/heroin-addiction.html', 'treatment/fentanyl-addiction.html',
                           'services/mat-treatment.html']
            },
            'dual_diagnosis': {
                'keywords': ['dual diagnosis', 'co-occurring', 'mental health', 'depression', 'anxiety', 'ptsd'],
                'hub': 'treatment/dual-diagnosis.html',
                'related': ['treatment/depression-and-addiction.html', 'treatment/anxiety-and-addiction.html',
                           'treatment/ptsd-and-addiction.html']
            },
            'insurance': {
                'keywords': ['insurance', 'coverage', 'pay', 'cost', 'afford'],
                'hub': 'insurance.html',
                'related': ['insurance/aetna.html', 'insurance/cigna.html', 'insurance/blue-cross-blue-shield.html',
                           'rehab-cost-orange-county.html']
            },
            'locations': {
                'keywords': ['orange county', 'irvine', 'newport', 'costa mesa', 'huntington', 'anaheim'],
                'hub': 'locations.html',
                'related': ['drug-rehab-orange-county.html', 'alcohol-rehab-orange-county.html']
            }
        }

        # High-priority pages that should receive more internal links
        self.priority_pages = [
            'drug-rehab-orange-county.html',
            'alcohol-rehab-orange-county.html',
            'rehab-cost-orange-county.html',
            'services/medical-detox.html',
            'services/residential-treatment.html',
            'insurance.html',
            'contact.html'
        ]

    def scan_pages(self):
        """Scan all HTML pages and build link graph."""
        html_files = glob.glob(os.path.join(self.site_path, '**/*.html'), recursive=True)

        for filepath in html_files:
            # Skip backup/test files
            if any(x in filepath.lower() for x in ['backup', '-old', 'test-']):
                continue

            rel_path = os.path.relpath(filepath, self.site_path)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                soup = BeautifulSoup(content, 'html.parser')

                # Get page info
                title = soup.find('title')
                h1 = soup.find('h1')

                # Remove nav/footer for content analysis
                for elem in soup.find_all(['nav', 'footer', 'header']):
                    elem.decompose()

                body_text = soup.get_text().lower()

                self.pages[rel_path] = {
                    'filepath': filepath,
                    'title': title.get_text() if title else '',
                    'h1': h1.get_text() if h1 else '',
                    'content': body_text,
                    'word_count': len(body_text.split()),
                    'outgoing_links': [],
                    'incoming_links': []
                }

                # Find all internal links
                for a in soup.find_all('a', href=True):
                    href = a.get('href', '')
                    if href.startswith('#') or href.startswith('tel:') or href.startswith('mailto:'):
                        continue
                    if href.startswith('http') and 'trustsocal.com' not in href:
                        continue

                    # Normalize path
                    if href.startswith('http'):
                        href = href.replace('https://trustsocal.com/', '').replace('http://trustsocal.com/', '')

                    # Handle relative paths
                    if href.startswith('../'):
                        # Resolve relative to current file
                        current_dir = os.path.dirname(rel_path)
                        href = os.path.normpath(os.path.join(current_dir, href))
                    elif href.startswith('./'):
                        href = href[2:]

                    anchor_text = a.get_text().strip()
                    self.pages[rel_path]['outgoing_links'].append({
                        'href': href,
                        'anchor': anchor_text
                    })
                    self.link_graph[rel_path].add(href)
                    self.incoming_links[href].append({
                        'from': rel_path,
                        'anchor': anchor_text
                    })

            except Exception as e:
                print(f"Error processing {rel_path}: {e}")

        return self.pages

    def find_linking_opportunities(self):
        """Find opportunities to add internal links."""
        opportunities = []

        for page_path, page_data in self.pages.items():
            content = page_data['content']

            for cluster_name, cluster_data in self.topic_clusters.items():
                hub_page = cluster_data['hub']

                # Skip if this IS the hub page
                if page_path == hub_page:
                    continue

                # Check if content mentions cluster keywords
                keyword_matches = sum(1 for kw in cluster_data['keywords'] if kw in content)

                if keyword_matches >= 2:
                    # Check if already links to hub
                    links_to_hub = any(hub_page in link['href'] for link in page_data['outgoing_links'])

                    if not links_to_hub:
                        opportunities.append({
                            'page': page_path,
                            'missing_link_to': hub_page,
                            'cluster': cluster_name,
                            'keyword_matches': keyword_matches,
                            'priority': 'HIGH' if page_path in self.priority_pages else 'MEDIUM'
                        })

                # Check related pages
                for related in cluster_data['related']:
                    if page_path == related:
                        continue

                    links_to_related = any(related in link['href'] for link in page_data['outgoing_links'])

                    if not links_to_related and keyword_matches >= 1:
                        opportunities.append({
                            'page': page_path,
                            'missing_link_to': related,
                            'cluster': cluster_name,
                            'keyword_matches': keyword_matches,
                            'priority': 'MEDIUM'
                        })

        # Sort by priority and keyword matches
        opportunities.sort(key=lambda x: (x['priority'] == 'HIGH', x['keyword_matches']), reverse=True)

        return opportunities[:50]  # Top 50 opportunities

    def find_orphan_pages(self):
        """Find pages with no or few incoming links."""
        orphans = []

        for page_path in self.pages:
            incoming = self.incoming_links.get(page_path, [])

            # Filter out nav/footer links (usually from every page)
            unique_sources = set(link['from'] for link in incoming)

            if len(unique_sources) < 3:
                orphans.append({
                    'page': page_path,
                    'incoming_link_count': len(unique_sources),
                    'priority': 'HIGH' if page_path in self.priority_pages else 'LOW'
                })

        orphans.sort(key=lambda x: (x['priority'] == 'HIGH', -x['incoming_link_count']))
        return orphans

    def find_anchor_text_opportunities(self):
        """Find opportunities to improve anchor text."""
        issues = []

        generic_anchors = ['click here', 'read more', 'learn more', 'here', 'this page', 'link']

        for page_path, page_data in self.pages.items():
            for link in page_data['outgoing_links']:
                anchor = link['anchor'].lower().strip()

                if any(generic in anchor for generic in generic_anchors) or len(anchor) < 3:
                    issues.append({
                        'page': page_path,
                        'link_to': link['href'],
                        'current_anchor': link['anchor'],
                        'issue': 'Generic or empty anchor text',
                        'suggestion': f"Use descriptive anchor text with target keywords"
                    })

        return issues[:30]

    def generate_report(self):
        """Generate comprehensive internal linking report."""
        self.scan_pages()

        opportunities = self.find_linking_opportunities()
        orphans = self.find_orphan_pages()
        anchor_issues = self.find_anchor_text_opportunities()

        # Calculate link distribution
        link_counts = {page: len(links) for page, links in self.link_graph.items()}
        incoming_counts = {page: len(links) for page, links in self.incoming_links.items()}

        report = {
            'summary': {
                'total_pages': len(self.pages),
                'total_internal_links': sum(link_counts.values()),
                'avg_outgoing_links': sum(link_counts.values()) / len(self.pages) if self.pages else 0,
                'avg_incoming_links': sum(incoming_counts.values()) / len(self.pages) if self.pages else 0,
                'orphan_pages': len([o for o in orphans if o['incoming_link_count'] == 0]),
                'low_link_pages': len([o for o in orphans if o['incoming_link_count'] < 3])
            },
            'top_linked_pages': sorted(incoming_counts.items(), key=lambda x: x[1], reverse=True)[:10],
            'least_linked_pages': sorted(incoming_counts.items(), key=lambda x: x[1])[:10],
            'linking_opportunities': opportunities,
            'orphan_pages': orphans[:20],
            'anchor_text_issues': anchor_issues,
            'priority_page_status': []
        }

        # Check priority pages
        for priority_page in self.priority_pages:
            if priority_page in incoming_counts:
                report['priority_page_status'].append({
                    'page': priority_page,
                    'incoming_links': incoming_counts[priority_page],
                    'status': 'GOOD' if incoming_counts[priority_page] >= 10 else 'NEEDS MORE LINKS'
                })

        return report

    def print_recommendations(self):
        """Print actionable recommendations."""
        report = self.generate_report()

        print("=" * 70)
        print("INTERNAL LINKING OPTIMIZATION REPORT")
        print("Trust SoCal Website Analysis")
        print("=" * 70)
        print()

        print("SUMMARY")
        print("-" * 70)
        print(f"Total Pages Analyzed: {report['summary']['total_pages']}")
        print(f"Total Internal Links: {report['summary']['total_internal_links']}")
        print(f"Average Outgoing Links/Page: {report['summary']['avg_outgoing_links']:.1f}")
        print(f"Average Incoming Links/Page: {report['summary']['avg_incoming_links']:.1f}")
        print(f"Orphan Pages (0 incoming): {report['summary']['orphan_pages']}")
        print(f"Low-Link Pages (<3 incoming): {report['summary']['low_link_pages']}")
        print()

        print("TOP LINKED PAGES (Most Authority)")
        print("-" * 70)
        for page, count in report['top_linked_pages']:
            print(f"  {count:3d} links -> {page}")
        print()

        print("PRIORITY PAGES STATUS")
        print("-" * 70)
        for status in report['priority_page_status']:
            emoji = "✓" if status['status'] == 'GOOD' else "⚠"
            print(f"  {emoji} {status['page']}: {status['incoming_links']} links ({status['status']})")
        print()

        print("TOP LINKING OPPORTUNITIES")
        print("-" * 70)
        for i, opp in enumerate(report['linking_opportunities'][:15], 1):
            print(f"  {i}. [{opp['priority']}] {opp['page']}")
            print(f"     -> Add link to: {opp['missing_link_to']}")
            print(f"     Cluster: {opp['cluster']}, Keyword matches: {opp['keyword_matches']}")
            print()

        print("ANCHOR TEXT ISSUES")
        print("-" * 70)
        for issue in report['anchor_text_issues'][:10]:
            print(f"  Page: {issue['page']}")
            print(f"  Current: '{issue['current_anchor']}' -> {issue['link_to']}")
            print(f"  Issue: {issue['issue']}")
            print()

        # Save report
        report_path = os.path.join(self.site_path, 'INTERNAL_LINKING_REPORT.json')
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        print(f"Full report saved to: {report_path}")

        return report


def main():
    site_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    optimizer = InternalLinkingOptimizer(site_path)
    optimizer.print_recommendations()


if __name__ == '__main__':
    main()
