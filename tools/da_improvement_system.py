#!/usr/bin/env python3
"""
Domain Authority Improvement System for Trust SoCal
====================================================
Comprehensive SEO analysis and DA improvement toolkit.
"""

import os
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import glob

class DomainAuthorityAnalyzer:
    """Analyze and improve domain authority factors."""

    def __init__(self, site_path):
        self.site_path = site_path
        self.pages = []
        self.issues = []
        self.internal_links = {}
        self.external_links = {}
        self.orphan_pages = []
        self.backlink_opportunities = []

    def scan_all_pages(self):
        """Scan all HTML pages in the site."""
        html_files = glob.glob(os.path.join(self.site_path, '**/*.html'), recursive=True)

        for filepath in html_files:
            # Skip backup files
            if 'backup' in filepath.lower() or 'old' in filepath.lower() or 'test' in filepath.lower():
                continue

            rel_path = os.path.relpath(filepath, self.site_path)

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                soup = BeautifulSoup(content, 'html.parser')

                page_data = {
                    'path': rel_path,
                    'filepath': filepath,
                    'title': self._get_title(soup),
                    'meta_description': self._get_meta_description(soup),
                    'h1': self._get_h1(soup),
                    'word_count': self._get_word_count(soup),
                    'internal_links': self._get_internal_links(soup, rel_path),
                    'external_links': self._get_external_links(soup),
                    'schema_types': self._get_schema_types(soup),
                    'images': self._get_images(soup),
                    'canonical': self._get_canonical(soup),
                    'has_video_schema': self._has_video_schema(soup),
                    'has_faq_schema': self._has_faq_schema(soup),
                }

                self.pages.append(page_data)

            except Exception as e:
                self.issues.append(f"Error reading {rel_path}: {str(e)}")

        return self.pages

    def _get_title(self, soup):
        title = soup.find('title')
        return title.get_text().strip() if title else None

    def _get_meta_description(self, soup):
        meta = soup.find('meta', attrs={'name': 'description'})
        return meta.get('content', '').strip() if meta else None

    def _get_h1(self, soup):
        h1 = soup.find('h1')
        return h1.get_text().strip() if h1 else None

    def _get_word_count(self, soup):
        # Remove script and style elements
        for element in soup(['script', 'style', 'header', 'footer', 'nav']):
            element.decompose()
        text = soup.get_text()
        words = text.split()
        return len(words)

    def _get_internal_links(self, soup, current_path):
        links = []
        for a in soup.find_all('a', href=True):
            href = a.get('href', '')
            if href.startswith('#') or href.startswith('tel:') or href.startswith('mailto:'):
                continue
            if not href.startswith('http'):
                links.append({
                    'href': href,
                    'text': a.get_text().strip()[:50]
                })
        return links

    def _get_external_links(self, soup):
        links = []
        for a in soup.find_all('a', href=True):
            href = a.get('href', '')
            if href.startswith('http') and 'trustsocal.com' not in href:
                links.append({
                    'href': href,
                    'text': a.get_text().strip()[:50],
                    'rel': a.get('rel', [])
                })
        return links

    def _get_schema_types(self, soup):
        schemas = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(script.string)
                if isinstance(data, dict):
                    schema_type = data.get('@type', 'Unknown')
                    if isinstance(schema_type, list):
                        schemas.extend(schema_type)
                    else:
                        schemas.append(schema_type)
            except:
                pass
        return schemas

    def _get_images(self, soup):
        images = []
        for img in soup.find_all('img'):
            images.append({
                'src': img.get('src', ''),
                'alt': img.get('alt', ''),
                'has_alt': bool(img.get('alt'))
            })
        return images

    def _get_canonical(self, soup):
        link = soup.find('link', rel='canonical')
        return link.get('href') if link else None

    def _has_video_schema(self, soup):
        for script in soup.find_all('script', type='application/ld+json'):
            if 'VideoObject' in script.string:
                return True
        return False

    def _has_faq_schema(self, soup):
        for script in soup.find_all('script', type='application/ld+json'):
            if 'FAQPage' in script.string:
                return True
        return False

    def analyze_internal_linking(self):
        """Analyze internal linking structure."""
        # Build link graph
        link_graph = {}
        all_pages = set(p['path'] for p in self.pages)

        for page in self.pages:
            link_graph[page['path']] = set()
            for link in page['internal_links']:
                href = link['href']
                # Normalize path
                if href.startswith('../'):
                    # Resolve relative path
                    pass
                elif href.startswith('./'):
                    href = href[2:]
                link_graph[page['path']].add(href)

        # Find orphan pages (no incoming links)
        linked_pages = set()
        for source, targets in link_graph.items():
            linked_pages.update(targets)

        # Main pages that should have links
        important_pages = [p for p in self.pages if p['path'] in [
            'index.html', 'services.html', 'about.html', 'contact.html',
            'insurance.html', 'locations.html'
        ]]

        # Calculate link scores
        link_scores = {}
        for page in self.pages:
            incoming = sum(1 for source, targets in link_graph.items()
                          if page['path'] in targets or any(page['path'] in t for t in targets))
            outgoing = len(page['internal_links'])
            link_scores[page['path']] = {
                'incoming': incoming,
                'outgoing': outgoing,
                'score': incoming * 2 + outgoing
            }

        return link_scores

    def generate_da_report(self):
        """Generate comprehensive DA improvement report."""
        report = {
            'generated': datetime.now().isoformat(),
            'site_path': self.site_path,
            'total_pages': len(self.pages),
            'summary': {},
            'technical_seo': {},
            'content_analysis': {},
            'schema_analysis': {},
            'link_analysis': {},
            'recommendations': [],
            'backlink_opportunities': [],
            'competitor_gaps': []
        }

        # Technical SEO Summary
        pages_with_title = sum(1 for p in self.pages if p['title'])
        pages_with_meta = sum(1 for p in self.pages if p['meta_description'])
        pages_with_h1 = sum(1 for p in self.pages if p['h1'])
        pages_with_canonical = sum(1 for p in self.pages if p['canonical'])
        pages_with_video = sum(1 for p in self.pages if p['has_video_schema'])
        pages_with_faq = sum(1 for p in self.pages if p['has_faq_schema'])

        report['technical_seo'] = {
            'pages_with_title': pages_with_title,
            'pages_without_title': len(self.pages) - pages_with_title,
            'pages_with_meta_description': pages_with_meta,
            'pages_without_meta_description': len(self.pages) - pages_with_meta,
            'pages_with_h1': pages_with_h1,
            'pages_without_h1': len(self.pages) - pages_with_h1,
            'pages_with_canonical': pages_with_canonical,
            'pages_with_video_schema': pages_with_video,
            'pages_with_faq_schema': pages_with_faq
        }

        # Content Analysis
        thin_content = [p for p in self.pages if p['word_count'] < 300]
        strong_content = [p for p in self.pages if p['word_count'] > 1500]
        pillar_content = [p for p in self.pages if p['word_count'] > 3000]

        report['content_analysis'] = {
            'thin_content_pages': len(thin_content),
            'thin_content_list': [p['path'] for p in thin_content],
            'strong_content_pages': len(strong_content),
            'pillar_content_pages': len(pillar_content),
            'average_word_count': sum(p['word_count'] for p in self.pages) / len(self.pages) if self.pages else 0
        }

        # Schema Analysis
        all_schemas = []
        for page in self.pages:
            all_schemas.extend(page['schema_types'])
        schema_counts = {}
        for schema in all_schemas:
            schema_counts[schema] = schema_counts.get(schema, 0) + 1

        report['schema_analysis'] = {
            'total_schemas': len(all_schemas),
            'unique_schema_types': len(set(all_schemas)),
            'schema_distribution': schema_counts
        }

        # Link Analysis
        link_scores = self.analyze_internal_linking()
        total_internal_links = sum(len(p['internal_links']) for p in self.pages)
        total_external_links = sum(len(p['external_links']) for p in self.pages)

        report['link_analysis'] = {
            'total_internal_links': total_internal_links,
            'total_external_links': total_external_links,
            'avg_internal_links_per_page': total_internal_links / len(self.pages) if self.pages else 0,
            'pages_with_low_internal_links': len([p for p in self.pages if len(p['internal_links']) < 3])
        }

        # Generate Recommendations
        recommendations = []

        # Priority 1: Critical Technical Issues
        if report['technical_seo']['pages_without_title'] > 0:
            recommendations.append({
                'priority': 'CRITICAL',
                'category': 'Technical SEO',
                'issue': f"{report['technical_seo']['pages_without_title']} pages missing title tags",
                'impact': 'High - Title tags are a primary ranking factor',
                'action': 'Add unique, keyword-optimized title tags to all pages'
            })

        if report['technical_seo']['pages_without_meta_description'] > 0:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'Technical SEO',
                'issue': f"{report['technical_seo']['pages_without_meta_description']} pages missing meta descriptions",
                'impact': 'Medium - Affects click-through rates from search results',
                'action': 'Add compelling meta descriptions with target keywords'
            })

        # Priority 2: Content Issues
        if report['content_analysis']['thin_content_pages'] > 0:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'Content',
                'issue': f"{report['content_analysis']['thin_content_pages']} pages have thin content (<300 words)",
                'impact': 'High - Thin content may be considered low quality by Google',
                'action': 'Expand content or consolidate thin pages',
                'pages': report['content_analysis']['thin_content_list'][:10]
            })

        # Priority 3: Schema Opportunities
        if report['technical_seo']['pages_with_faq_schema'] < 10:
            recommendations.append({
                'priority': 'MEDIUM',
                'category': 'Schema',
                'issue': 'Limited FAQ schema implementation',
                'impact': 'Medium - FAQ schema can earn featured snippets',
                'action': 'Add FAQ schema to service and treatment pages'
            })

        # Priority 4: Internal Linking
        if report['link_analysis']['avg_internal_links_per_page'] < 5:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'Internal Linking',
                'issue': f"Low average internal links ({report['link_analysis']['avg_internal_links_per_page']:.1f} per page)",
                'impact': 'High - Internal linking distributes page authority',
                'action': 'Add contextual internal links between related content'
            })

        # Priority 5: Backlink Strategy
        recommendations.append({
            'priority': 'CRITICAL',
            'category': 'Backlinks',
            'issue': 'Need to build high-authority backlinks',
            'impact': 'Very High - Backlinks are the #1 ranking factor',
            'action': 'Submit to directories, create linkable content, pursue PR'
        })

        report['recommendations'] = recommendations

        # Backlink Opportunities (from research)
        report['backlink_opportunities'] = [
            {'site': 'Recovery.com', 'da': 70, 'type': 'Directory', 'priority': 'HIGH', 'cost': 'Free'},
            {'site': 'Psychology Today', 'da': 90, 'type': 'Directory', 'priority': 'HIGH', 'cost': 'Free'},
            {'site': 'Rehabs.com', 'da': 65, 'type': 'Directory', 'priority': 'HIGH', 'cost': 'Free'},
            {'site': 'SAMHSA FindTreatment.gov', 'da': 90, 'type': 'Government', 'priority': 'CRITICAL', 'cost': 'Free'},
            {'site': 'Google Business Profile', 'da': 100, 'type': 'Local', 'priority': 'CRITICAL', 'cost': 'Free'},
            {'site': 'Yelp', 'da': 94, 'type': 'Directory', 'priority': 'HIGH', 'cost': 'Free'},
            {'site': 'Healthgrades', 'da': 80, 'type': 'Healthcare', 'priority': 'HIGH', 'cost': 'Free'},
            {'site': 'Addiction Center', 'da': 60, 'type': 'Directory', 'priority': 'MEDIUM', 'cost': 'Free'},
            {'site': 'NAATP', 'da': 55, 'type': 'Association', 'priority': 'MEDIUM', 'cost': 'Membership'},
            {'site': 'Apple Maps', 'da': 100, 'type': 'Local', 'priority': 'HIGH', 'cost': 'Free'},
            {'site': 'Bing Places', 'da': 100, 'type': 'Local', 'priority': 'HIGH', 'cost': 'Free'},
        ]

        # Competitor Gap Analysis
        report['competitor_gaps'] = [
            {
                'competitor': 'Covenant Hills Treatment',
                'strength': 'Christ-centered 12-step approach, 30+ years established',
                'gap': 'Trust SoCal could emphasize unique treatment philosophies'
            },
            {
                'competitor': 'Chapters Capistrano',
                'strength': 'Luxury oceanfront positioning, CARF + Joint Commission',
                'gap': 'Trust SoCal has Joint Commission - consider CARF certification'
            },
            {
                'competitor': 'Yellowstone Recovery',
                'strength': 'Nonprofit, "lowest cost" messaging, 25+ years',
                'gap': 'Trust SoCal could highlight value/ROI messaging'
            },
            {
                'competitor': 'Ocean Hills Recovery',
                'strength': 'Video content strategy, family-focused messaging',
                'gap': 'Trust SoCal has video schema - need actual video content'
            },
            {
                'competitor': 'Resurgence Behavioral Health',
                'strength': 'Multiple locations, trauma-informed positioning',
                'gap': 'Trust SoCal has location pages - expand trauma content'
            }
        ]

        # Calculate overall DA score estimate
        score = 0
        score += min(30, report['technical_seo']['pages_with_title'] / len(self.pages) * 30)
        score += min(20, report['content_analysis']['pillar_content_pages'] * 5)
        score += min(20, report['schema_analysis']['total_schemas'] / len(self.pages) * 10)
        score += min(15, report['link_analysis']['avg_internal_links_per_page'] * 3)
        score += 15 if report['technical_seo']['pages_with_canonical'] > len(self.pages) * 0.8 else 5

        report['summary'] = {
            'estimated_technical_score': round(score, 1),
            'grade': 'A' if score >= 85 else 'B+' if score >= 75 else 'B' if score >= 65 else 'C' if score >= 50 else 'D',
            'top_priority': 'Build High-Authority Backlinks',
            'quick_wins': [
                'Submit to SAMHSA FindTreatment.gov',
                'Claim Google Business Profile',
                'Submit to Recovery.com and Psychology Today',
                'Add FAQ schema to all service pages'
            ]
        }

        return report


def main():
    """Run the DA improvement analysis."""
    site_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print("=" * 60)
    print("DOMAIN AUTHORITY IMPROVEMENT SYSTEM")
    print("Trust SoCal - Comprehensive SEO Analysis")
    print("=" * 60)
    print()

    analyzer = DomainAuthorityAnalyzer(site_path)

    print("Scanning all pages...")
    pages = analyzer.scan_all_pages()
    print(f"Found {len(pages)} pages to analyze")
    print()

    print("Generating DA improvement report...")
    report = analyzer.generate_da_report()

    # Save report
    report_path = os.path.join(site_path, 'DA_IMPROVEMENT_REPORT.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Report saved to: {report_path}")
    print()

    # Print summary
    print("=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)
    print()
    print(f"Total Pages Analyzed: {report['total_pages']}")
    print(f"Technical Score: {report['summary']['estimated_technical_score']}/100")
    print(f"Grade: {report['summary']['grade']}")
    print()

    print("TECHNICAL SEO:")
    print(f"  - Pages with Title: {report['technical_seo']['pages_with_title']}")
    print(f"  - Pages with Meta Description: {report['technical_seo']['pages_with_meta_description']}")
    print(f"  - Pages with H1: {report['technical_seo']['pages_with_h1']}")
    print(f"  - Pages with Video Schema: {report['technical_seo']['pages_with_video_schema']}")
    print(f"  - Pages with FAQ Schema: {report['technical_seo']['pages_with_faq_schema']}")
    print()

    print("CONTENT ANALYSIS:")
    print(f"  - Average Word Count: {report['content_analysis']['average_word_count']:.0f}")
    print(f"  - Thin Content Pages (<300 words): {report['content_analysis']['thin_content_pages']}")
    print(f"  - Strong Content Pages (>1500 words): {report['content_analysis']['strong_content_pages']}")
    print(f"  - Pillar Content Pages (>3000 words): {report['content_analysis']['pillar_content_pages']}")
    print()

    print("SCHEMA ANALYSIS:")
    print(f"  - Total Schema Blocks: {report['schema_analysis']['total_schemas']}")
    print(f"  - Unique Schema Types: {report['schema_analysis']['unique_schema_types']}")
    print()

    print("INTERNAL LINKING:")
    print(f"  - Total Internal Links: {report['link_analysis']['total_internal_links']}")
    print(f"  - Avg Links Per Page: {report['link_analysis']['avg_internal_links_per_page']:.1f}")
    print(f"  - Pages with Low Links (<3): {report['link_analysis']['pages_with_low_internal_links']}")
    print()

    print("=" * 60)
    print("TOP RECOMMENDATIONS")
    print("=" * 60)
    for i, rec in enumerate(report['recommendations'][:5], 1):
        print(f"\n{i}. [{rec['priority']}] {rec['category']}")
        print(f"   Issue: {rec['issue']}")
        print(f"   Action: {rec['action']}")
    print()

    print("=" * 60)
    print("BACKLINK OPPORTUNITIES (Priority)")
    print("=" * 60)
    for opp in report['backlink_opportunities']:
        print(f"  [{opp['priority']}] {opp['site']} (DA: {opp['da']}) - {opp['cost']}")
    print()

    print("=" * 60)
    print("QUICK WINS TO IMPLEMENT NOW")
    print("=" * 60)
    for win in report['summary']['quick_wins']:
        print(f"  ✓ {win}")
    print()

    return report


if __name__ == '__main__':
    main()
