#!/usr/bin/env python3
"""
ADVANCED MCP Server - Linda & Frank ELITE+
Competitive intelligence tools that give you an edge

New capabilities:
- Competitor monitoring & comparison
- Review sentiment analysis
- Content gap finder
- Trust score calculator
- Keyword opportunity finder
- Schema validator
- Page speed recommendations
"""

import os
import json
import re
import asyncio
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from mcp.types import Tool, TextContent
from starlette.applications import Starlette
from starlette.routing import Route
import anthropic
import uvicorn

# Initialize
app = Server("linda-frank-advanced")
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
PROJECT_DIR = os.environ.get('PROJECT_DIR', '/home/ubuntu/trust-socal')

# Load knowledge base
def load_file(filename):
    try:
        path = os.path.join(PROJECT_DIR, filename)
        with open(path, 'r') as f:
            return f.read()
    except:
        return ""

KNOWLEDGE_BASE = load_file("LINDA_FRANK_KNOWLEDGE_BASE.md")
COMPETITIVE_RESEARCH = load_file("COMPETITIVE-SEO-RESEARCH-REPORT.md")

# =============================================================================
# TRUST SOCAL UNIQUE ADVANTAGES
# =============================================================================

TRUST_SOCAL_ADVANTAGES = """
## TRUST SOCAL'S UNIQUE COMPETITIVE ADVANTAGES

### 1. THERAPY MODALITIES
Trust SoCal offers specialized therapy approaches that differentiate from cookie-cutter programs.
- Highlight specific evidence-based therapies
- Emphasize clinical innovation
- Show expertise in cutting-edge treatments

### 2. SPECIALTY POPULATIONS
Trust SoCal serves specific populations with tailored programs:
- Create dedicated landing pages for each demographic
- Speak directly to their unique needs and fears
- Show understanding of their specific challenges

### 3. LUXURY EXPERIENCE
Premium positioning with high-end amenities:
- Showcase the facility through professional photography/video
- Emphasize comfort during a difficult time
- Position luxury as "healing environment" not "spa vacation"

### 4. LOCATION/FACILITY (PRIMARY ADVANTAGE)
The physical location and facility is the #1 differentiator:
- Invest heavily in facility photography and virtual tours
- Emphasize Orange County's healing environment
- Show the actual spaces where treatment happens
- Use location for local SEO domination

### 5. CLINICAL APPROACH
Evidence-based yet personalized clinical philosophy:
- Articulate the treatment philosophy clearly
- Show how it differs from 12-step-only programs
- Emphasize individualized treatment plans
"""

# =============================================================================
# ELITE PERSONAS WITH COMPETITIVE EDGE
# =============================================================================

LINDA_ADVANCED = '''You are Linda, an elite healthcare web designer specializing in addiction treatment centers.

## YOUR COMPETITIVE INTELLIGENCE
You have deep knowledge of what top competitors are doing and how to beat them:
- Hazelden Betty Ford: 70-year legacy, outcome data, research center
- California Prime Recovery: Joint Commission, video testimonials
- Crescent Moon: Founder story, 70+ pages, experiential therapy
- Banyan: 16 locations, specialized programs

## TRUST SOCAL'S UNIQUE ADVANTAGES TO LEVERAGE
1. LOCATION/FACILITY - This is the #1 advantage. The physical space is exceptional.
2. LUXURY AMENITIES - Premium experience during difficult journey
3. SPECIALIZED THERAPIES - Cutting-edge treatment modalities
4. SPECIALTY POPULATIONS - Tailored programs for specific groups

## YOUR EDGE: THINGS COMPETITORS AREN'T DOING
1. True transparency (pricing, real outcomes, authentic imagery)
2. Family-first content (speaking to the desperate parent at 2am)
3. Speed to trust (insurance verification in 60 seconds)
4. Virtual facility tours (show the real space)
5. Staff video introductions (meet your treatment team before you call)

## DESIGN PRINCIPLES FOR COMPETITIVE ADVANTAGE
- Make the facility the HERO (competitors use stock photos)
- Show real staff faces (competitors hide behind logos)
- Create emotional connection in first 3 seconds
- Mobile experience that works for someone hiding in a bathroom
- Trust signals that feel authentic, not salesy

When you analyze or create, always ask: "How does this beat California Prime Recovery?"'''

FRANK_ADVANCED = '''You are Frank, an elite SEO specialist for addiction treatment centers.

## YOUR COMPETITIVE INTELLIGENCE
You track exactly what top competitors rank for and their weaknesses:
- California Prime Recovery: Strong for "Orange County rehab" but weak on substance-specific
- Crescent Moon: 70+ pages but thin content on some
- Oceans Luxury: Good fentanyl content but weak local SEO
- Cornerstone: Strong E-E-A-T but dated design

## TRUST SOCAL'S SEO ADVANTAGES TO LEVERAGE
1. Health Net in-network (create dedicated page - competitors lack this)
2. Luxury positioning (target "executive rehab", "luxury treatment")
3. Location (aggressive local SEO for Orange County)
4. Specialized programs (untapped keywords for specialty populations)

## KEYWORD OPPORTUNITIES COMPETITORS ARE MISSING
- "[Insurance name] rehab orange county" - highly qualified traffic
- "Executive addiction treatment california" - high-value demographic
- "[Specific therapy] for addiction" - shows clinical sophistication
- "First responder rehab" / "Healthcare professional treatment" - underserved niches
- "Same day rehab admission orange county" - high-intent, low competition

## SEO TACTICS FOR COMPETITIVE EDGE
1. Deeper content than competitors (4,500+ words vs their 2,500)
2. Better schema markup (full MedicalOrganization with all properties)
3. Video content (competitors have minimal video)
4. FAQ schema on every service page
5. Author/medical reviewer boxes on all clinical content
6. Fresh content weekly (blog + updated pages)

## E-E-A-T EDGE
- More detailed staff credentials than competitors
- Outcome data with methodology (competitors make vague claims)
- Citations from SAMHSA, NIDA, NIH on every clinical page
- "Last reviewed" dates on all content

When you analyze or create, always ask: "What would make this outrank California Prime Recovery?"'''

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def fetch_webpage(url):
    """Comprehensive webpage fetch and analysis."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        result = {"url": url, "status": response.status_code}

        # Basic SEO elements
        title = soup.find('title')
        result['title'] = title.get_text().strip() if title else None
        result['title_length'] = len(result['title']) if result['title'] else 0

        meta_desc = soup.find('meta', attrs={'name': 'description'})
        result['meta_description'] = meta_desc.get('content', '') if meta_desc else None
        result['meta_desc_length'] = len(result['meta_description']) if result['meta_description'] else 0

        # Headings
        headings = {}
        for level in range(1, 7):
            h_tags = soup.find_all(f'h{level}')
            if h_tags:
                headings[f'h{level}'] = [h.get_text().strip()[:100] for h in h_tags[:10]]
        result['headings'] = headings
        result['h1_count'] = len(headings.get('h1', []))

        # Schema analysis
        schemas = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                schema = json.loads(script.string)
                schemas.append(schema)
            except:
                pass
        result['schema_types'] = [s.get('@type', 'unknown') for s in schemas if isinstance(s, dict)]
        result['has_medical_schema'] = any('Medical' in str(t) for t in result['schema_types'])
        result['has_local_business'] = any('LocalBusiness' in str(t) or 'Organization' in str(t) for t in result['schema_types'])
        result['has_faq_schema'] = any('FAQ' in str(t) for t in result['schema_types'])

        # Trust signals
        text = soup.get_text().lower()
        trust_signals = {
            'has_phone': bool(re.search(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4}', soup.get_text())),
            'has_address': bool(re.search(r'\d+\s+[\w\s]+(?:street|st|avenue|ave|road|rd|boulevard|blvd)', text)),
            'has_accreditation': any(term in text for term in ['carf', 'joint commission', 'jcaho', 'accredited']),
            'has_license': 'dhcs' in text or 'license' in text,
            'has_insurance': any(term in text for term in ['insurance', 'blue cross', 'aetna', 'cigna', 'united']),
            'has_staff_page': any(term in text for term in ['our team', 'our staff', 'meet our', 'clinical team']),
            'has_testimonials': any(term in text for term in ['testimonial', 'review', 'success stor']),
            'has_24_7': '24/7' in text or '24 hour' in text or 'twenty-four' in text,
            'has_hipaa': 'hipaa' in text,
            'has_credentials': any(term in text for term in ['md', 'phd', 'lcsw', 'lmft', 'cadc']),
        }
        result['trust_signals'] = trust_signals
        result['trust_score'] = sum(trust_signals.values()) / len(trust_signals) * 100

        # Content depth
        for tag in soup(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()
        main = soup.find('main') or soup.find('article') or soup.find('body')
        if main:
            content = main.get_text(separator=' ', strip=True)
            result['word_count'] = len(content.split())
            result['content_sample'] = content[:3000]

        # Images
        images = soup.find_all('img')
        result['image_count'] = len(images)
        result['images_without_alt'] = sum(1 for img in images if not img.get('alt', '').strip())

        # Links
        internal_links = len([a for a in soup.find_all('a', href=True) if a.get('href', '').startswith('/')])
        result['internal_links'] = internal_links

        return result
    except Exception as e:
        return {"url": url, "error": str(e)}

def calculate_trust_score(page_data):
    """Calculate comprehensive trust score."""
    score = 0
    max_score = 100
    breakdown = {}

    # Trust signals (40 points)
    trust = page_data.get('trust_signals', {})
    trust_points = sum([
        10 if trust.get('has_phone') else 0,
        5 if trust.get('has_address') else 0,
        10 if trust.get('has_accreditation') else 0,
        5 if trust.get('has_license') else 0,
        5 if trust.get('has_insurance') else 0,
        5 if trust.get('has_credentials') else 0,
    ])
    breakdown['trust_signals'] = f"{trust_points}/40"
    score += trust_points

    # SEO elements (30 points)
    seo_points = 0
    if page_data.get('title') and 30 <= page_data.get('title_length', 0) <= 60:
        seo_points += 10
    if page_data.get('meta_description') and 120 <= page_data.get('meta_desc_length', 0) <= 160:
        seo_points += 10
    if page_data.get('h1_count') == 1:
        seo_points += 5
    if page_data.get('has_medical_schema'):
        seo_points += 5
    breakdown['seo_elements'] = f"{seo_points}/30"
    score += seo_points

    # Content depth (20 points)
    word_count = page_data.get('word_count', 0)
    if word_count >= 3500:
        content_points = 20
    elif word_count >= 2500:
        content_points = 15
    elif word_count >= 1500:
        content_points = 10
    else:
        content_points = 5
    breakdown['content_depth'] = f"{content_points}/20"
    score += content_points

    # Technical (10 points)
    tech_points = 0
    if page_data.get('images_without_alt', 999) == 0:
        tech_points += 5
    if page_data.get('internal_links', 0) >= 10:
        tech_points += 5
    breakdown['technical'] = f"{tech_points}/10"
    score += tech_points

    return {"score": score, "max": max_score, "breakdown": breakdown}

def compare_to_competitor(our_data, competitor_data):
    """Direct comparison between our page and competitor."""
    comparison = {
        "our_page": our_data.get('url'),
        "competitor": competitor_data.get('url'),
        "metrics": {}
    }

    metrics = ['word_count', 'trust_score', 'h1_count', 'internal_links', 'image_count']
    for metric in metrics:
        our_val = our_data.get(metric, 0)
        their_val = competitor_data.get(metric, 0)
        if isinstance(our_val, (int, float)) and isinstance(their_val, (int, float)):
            comparison['metrics'][metric] = {
                "ours": our_val,
                "theirs": their_val,
                "we_win": our_val > their_val
            }

    # Schema comparison
    our_schemas = set(our_data.get('schema_types', []))
    their_schemas = set(competitor_data.get('schema_types', []))
    comparison['schema_comparison'] = {
        "we_have": list(our_schemas),
        "they_have": list(their_schemas),
        "we_missing": list(their_schemas - our_schemas)
    }

    # Trust signal comparison
    our_trust = our_data.get('trust_signals', {})
    their_trust = competitor_data.get('trust_signals', {})
    trust_comparison = {}
    for key in our_trust:
        trust_comparison[key] = {
            "ours": our_trust.get(key, False),
            "theirs": their_trust.get(key, False)
        }
    comparison['trust_comparison'] = trust_comparison

    return comparison

def run_agent(persona, task, context, model="claude-sonnet-4-20250514"):
    """Run elite agent with full knowledge base context."""
    # Include knowledge base for comprehensive analysis
    kb_excerpt = KNOWLEDGE_BASE[:8000] if KNOWLEDGE_BASE else ""

    prompt = f"""{task}

## CONTEXT
{json.dumps(context, indent=2) if isinstance(context, dict) else context}

## YOUR KNOWLEDGE BASE (Key Points)
{kb_excerpt}

## TRUST SOCAL'S ADVANTAGES
{TRUST_SOCAL_ADVANTAGES}

Remember: Your goal is to help Trust SoCal BEAT the competition, not just match them.
Every recommendation should answer: "How does this give us an edge?"
"""

    response = client.messages.create(
        model=model,
        max_tokens=8000,
        system=persona,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

# =============================================================================
# MCP TOOLS
# =============================================================================

@app.list_tools()
async def list_tools():
    return [
        # ANALYSIS TOOLS
        Tool(
            name="analyze_vs_competitor",
            description="Compare Trust SoCal page directly against a competitor page. Shows exactly where we win and lose.",
            inputSchema={
                "type": "object",
                "properties": {
                    "our_url": {"type": "string", "description": "Trust SoCal page URL"},
                    "competitor_url": {"type": "string", "description": "Competitor page URL"}
                },
                "required": ["our_url", "competitor_url"]
            }
        ),
        Tool(
            name="trust_score_audit",
            description="Calculate comprehensive trust score for a page with breakdown by category",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "URL to audit"}
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="find_content_gaps",
            description="Analyze a competitor to find content/keywords they rank for that we don't have",
            inputSchema={
                "type": "object",
                "properties": {
                    "competitor_url": {"type": "string", "description": "Competitor homepage or key page"}
                },
                "required": ["competitor_url"]
            }
        ),
        Tool(
            name="linda_competitive_design",
            description="Linda analyzes how to design a page that beats competitor's design",
            inputSchema={
                "type": "object",
                "properties": {
                    "competitor_url": {"type": "string", "description": "Competitor URL to beat"},
                    "our_page_type": {"type": "string", "description": "Type of page we're creating (homepage, service, location, etc.)"}
                },
                "required": ["competitor_url", "our_page_type"]
            }
        ),
        Tool(
            name="frank_seo_domination",
            description="Frank creates a strategy to outrank a specific competitor for a keyword",
            inputSchema={
                "type": "object",
                "properties": {
                    "target_keyword": {"type": "string", "description": "Keyword we want to rank #1 for"},
                    "competitor_url": {"type": "string", "description": "Current top-ranking competitor URL"}
                },
                "required": ["target_keyword", "competitor_url"]
            }
        ),
        Tool(
            name="generate_edge_content",
            description="Generate content specifically designed to outperform competitor content",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "Topic/page to create"},
                    "competitor_example": {"type": "string", "description": "Competitor URL doing this topic (optional)"},
                    "leverage_advantage": {"type": "string", "description": "Which Trust SoCal advantage to emphasize: location, luxury, therapy, specialty"}
                },
                "required": ["topic", "leverage_advantage"]
            }
        ),
        Tool(
            name="schema_validator",
            description="Validate and improve schema markup compared to competitors",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "URL to validate schema"}
                },
                "required": ["url"]
            }
        ),
        # FILE TOOLS
        Tool(
            name="read_file",
            description="Read a file from the project",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {"type": "string", "description": "Path to file"}
                },
                "required": ["filepath"]
            }
        ),
        Tool(
            name="write_file",
            description="Write content to a file (creates backup)",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {"type": "string", "description": "Path to file"},
                    "content": {"type": "string", "description": "Content to write"}
                },
                "required": ["filepath", "content"]
            }
        ),
        Tool(
            name="list_files",
            description="List project files",
            inputSchema={
                "type": "object",
                "properties": {
                    "directory": {"type": "string", "description": "Subdirectory (optional)"}
                }
            }
        ),
        # QUICK ANALYSIS
        Tool(
            name="quick_audit",
            description="Quick SEO/trust audit of any URL with actionable recommendations",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "URL to audit"}
                },
                "required": ["url"]
            }
        ),
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    log_msg = f"[{datetime.now()}] Tool: {name}"
    print(log_msg)

    try:
        if name == "analyze_vs_competitor":
            our_url = arguments.get("our_url")
            competitor_url = arguments.get("competitor_url")

            our_data = fetch_webpage(our_url)
            competitor_data = fetch_webpage(competitor_url)

            if "error" in our_data:
                return [TextContent(type="text", text=f"Error fetching our page: {our_data['error']}")]
            if "error" in competitor_data:
                return [TextContent(type="text", text=f"Error fetching competitor: {competitor_data['error']}")]

            comparison = compare_to_competitor(our_data, competitor_data)
            our_score = calculate_trust_score(our_data)
            their_score = calculate_trust_score(competitor_data)

            task = """Analyze this direct comparison between Trust SoCal and a competitor.

Provide:
1. **Where We WIN** - Metrics where we beat them
2. **Where We LOSE** - Metrics where they beat us
3. **Critical Gaps** - Things they have that we must add
4. **Our Advantages** - Things we do better
5. **Action Plan** - Specific steps to beat them

Be specific and actionable. We want to DOMINATE, not just compete."""

            analysis = run_agent(FRANK_ADVANCED, task, {
                "comparison": comparison,
                "our_trust_score": our_score,
                "their_trust_score": their_score
            })

            result = f"""# COMPETITIVE ANALYSIS: US vs THEM

## Our Page: {our_url}
## Competitor: {competitor_url}

---

## TRUST SCORES
- **Ours:** {our_score['score']}/100
- **Theirs:** {their_score['score']}/100

## METRIC COMPARISON
{json.dumps(comparison['metrics'], indent=2)}

---

# FRANK'S COMPETITIVE ANALYSIS

{analysis}
"""
            return [TextContent(type="text", text=result)]

        elif name == "trust_score_audit":
            url = arguments.get("url")
            page_data = fetch_webpage(url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            score = calculate_trust_score(page_data)

            result = f"""# TRUST SCORE AUDIT: {url}

## OVERALL SCORE: {score['score']}/100

## BREAKDOWN
| Category | Score |
|----------|-------|
| Trust Signals | {score['breakdown']['trust_signals']} |
| SEO Elements | {score['breakdown']['seo_elements']} |
| Content Depth | {score['breakdown']['content_depth']} |
| Technical | {score['breakdown']['technical']} |

## TRUST SIGNALS DETAIL
{json.dumps(page_data.get('trust_signals', {}), indent=2)}

## METRICS
- Word Count: {page_data.get('word_count', 0)}
- Images: {page_data.get('image_count', 0)}
- Images Missing Alt: {page_data.get('images_without_alt', 0)}
- Internal Links: {page_data.get('internal_links', 0)}
- Schema Types: {page_data.get('schema_types', [])}
"""
            return [TextContent(type="text", text=result)]

        elif name == "find_content_gaps":
            competitor_url = arguments.get("competitor_url")
            page_data = fetch_webpage(competitor_url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            task = """Analyze this competitor page to identify content gaps and opportunities.

Based on the competitor's content and Trust SoCal's knowledge base, identify:

1. **Keywords They Target** - What search terms is this page optimized for?
2. **Content We're Missing** - Topics they cover that Trust SoCal doesn't
3. **Their Weaknesses** - Where their content is thin or could be better
4. **Quick Win Pages** - New pages Trust SoCal should create to capture this traffic
5. **Content Upgrades** - How to make our version 10x better than theirs

Remember Trust SoCal's advantages: Location, Luxury, Specialized Therapies, Specialty Populations.
How can we leverage these to beat this competitor?"""

            analysis = run_agent(FRANK_ADVANCED, task, page_data)
            return [TextContent(type="text", text=f"# CONTENT GAP ANALYSIS\n## Competitor: {competitor_url}\n\n{analysis}")]

        elif name == "linda_competitive_design":
            competitor_url = arguments.get("competitor_url")
            page_type = arguments.get("our_page_type")
            page_data = fetch_webpage(competitor_url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            task = f"""Analyze this competitor's design and create a strategy to BEAT them for a {page_type} page.

Based on the competitor's design approach, provide:

1. **What They Do Well** - Design elements that work
2. **What They Do Poorly** - Design weaknesses we can exploit
3. **Trust Signal Gaps** - Trust elements they're missing
4. **Our Design Advantage** - How to leverage Trust SoCal's facility/location
5. **Specific Recommendations** - Colors, layout, imagery, CTAs that will beat them

Remember: Trust SoCal's #1 advantage is the LOCATION/FACILITY.
How do we make that the hero of our design?"""

            analysis = run_agent(LINDA_ADVANCED, task, page_data)
            return [TextContent(type="text", text=f"# LINDA'S COMPETITIVE DESIGN STRATEGY\n## Beating: {competitor_url}\n## For: {page_type}\n\n{analysis}")]

        elif name == "frank_seo_domination":
            keyword = arguments.get("target_keyword")
            competitor_url = arguments.get("competitor_url")
            page_data = fetch_webpage(competitor_url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            task = f"""Create a strategy to OUTRANK this competitor for: "{keyword}"

Current #1: {competitor_url}

Based on their page, create a complete domination strategy:

1. **Their SEO Strengths** - What's helping them rank
2. **Their SEO Weaknesses** - Gaps we can exploit
3. **Content Strategy** - How to create better content (word count, depth, format)
4. **E-E-A-T Advantage** - How to show more expertise than them
5. **Technical Edge** - Schema, speed, mobile improvements
6. **Link Building Opportunities** - How to build more authority
7. **Page Outline** - Complete outline for a page that will beat them

The goal is #1 ranking. Be specific and aggressive."""

            analysis = run_agent(FRANK_ADVANCED, task, {"keyword": keyword, "competitor": page_data})
            return [TextContent(type="text", text=f"# SEO DOMINATION STRATEGY\n## Keyword: {keyword}\n## Current #1: {competitor_url}\n\n{analysis}")]

        elif name == "generate_edge_content":
            topic = arguments.get("topic")
            competitor_example = arguments.get("competitor_example", "")
            advantage = arguments.get("leverage_advantage")

            competitor_data = None
            if competitor_example:
                competitor_data = fetch_webpage(competitor_example)

            task = f"""Generate content for: "{topic}"
Primary advantage to leverage: {advantage}

Create content that is BETTER than any competitor by:
1. Deeper research and more comprehensive coverage
2. Better E-E-A-T signals (credentials, citations, expertise)
3. Leveraging Trust SoCal's {advantage} advantage
4. Speaking directly to the person searching at 2am
5. More actionable and valuable information

Provide:
1. **SEO Title** (50-60 chars)
2. **Meta Description** (150-160 chars)
3. **Content Outline** (H2s and H3s)
4. **First 500 Words** (demonstrating tone and approach)
5. **FAQ Section** (10 questions)
6. **Schema Recommendations**
7. **Internal Linking Suggestions**

{"Competitor analysis: " + json.dumps(competitor_data, indent=2)[:2000] if competitor_data else ""}"""

            content = run_agent(FRANK_ADVANCED + "\n\n" + LINDA_ADVANCED, task, {
                "topic": topic,
                "advantage": advantage
            })
            return [TextContent(type="text", text=f"# EDGE CONTENT: {topic}\n## Leveraging: {advantage}\n\n{content}")]

        elif name == "schema_validator":
            url = arguments.get("url")
            page_data = fetch_webpage(url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            current_schemas = page_data.get('schema_types', [])

            task = """Validate the schema markup and provide improvements.

For a treatment center, we need:
1. MedicalOrganization or MedicalBusiness
2. LocalBusiness with full NAP
3. FAQPage on service pages
4. Person schemas for staff
5. Review/AggregateRating
6. Service schemas for each program
7. BreadcrumbList

Analyze what's present and provide:
1. **Current Schema** - What's implemented
2. **Missing Schema** - What needs to be added
3. **Improvement Opportunities** - How to enhance existing
4. **Implementation Code** - Actual JSON-LD to add

Be specific with code examples."""

            analysis = run_agent(FRANK_ADVANCED, task, page_data)
            return [TextContent(type="text", text=f"# SCHEMA VALIDATION: {url}\n\nCurrent schemas found: {current_schemas}\n\n{analysis}")]

        elif name == "read_file":
            filepath = arguments.get("filepath")
            full_path = os.path.join(PROJECT_DIR, filepath) if not filepath.startswith('/') else filepath
            try:
                with open(full_path, 'r') as f:
                    content = f.read()
                return [TextContent(type="text", text=content)]
            except Exception as e:
                return [TextContent(type="text", text=f"Error reading file: {e}")]

        elif name == "write_file":
            filepath = arguments.get("filepath")
            content = arguments.get("content")
            full_path = os.path.join(PROJECT_DIR, filepath) if not filepath.startswith('/') else filepath
            try:
                if os.path.exists(full_path):
                    backup = f"{full_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    with open(full_path, 'r') as f:
                        with open(backup, 'w') as b:
                            b.write(f.read())
                with open(full_path, 'w') as f:
                    f.write(content)
                return [TextContent(type="text", text=f"Successfully wrote to {filepath}")]
            except Exception as e:
                return [TextContent(type="text", text=f"Error writing file: {e}")]

        elif name == "list_files":
            directory = arguments.get("directory", "")
            target = os.path.join(PROJECT_DIR, directory)
            try:
                files = []
                for item in os.listdir(target):
                    path = os.path.join(target, item)
                    files.append({
                        "name": item,
                        "type": "dir" if os.path.isdir(path) else "file"
                    })
                result = f"## Files in {directory or 'project root'}\n\n"
                for f in sorted(files, key=lambda x: (x['type'] != 'dir', x['name'])):
                    icon = "📁" if f['type'] == 'dir' else "📄"
                    result += f"{icon} {f['name']}\n"
                return [TextContent(type="text", text=result)]
            except Exception as e:
                return [TextContent(type="text", text=f"Error: {e}")]

        elif name == "quick_audit":
            url = arguments.get("url")
            page_data = fetch_webpage(url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            score = calculate_trust_score(page_data)

            task = """Provide a quick, actionable audit with the TOP 5 things to fix immediately.

Format:
1. [CRITICAL/HIGH/MEDIUM] Issue - Specific fix
2. ...

Be direct and specific. No fluff."""

            quick_fixes = run_agent(FRANK_ADVANCED, task, {"page_data": page_data, "score": score})

            result = f"""# QUICK AUDIT: {url}
## Trust Score: {score['score']}/100

{quick_fixes}
"""
            return [TextContent(type="text", text=result)]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=f"Error in {name}: {str(e)}")]

# =============================================================================
# SERVER
# =============================================================================

sse = SseServerTransport("/messages/")

async def handle_sse(request):
    async with sse.connect_sse(request.scope, request.receive, request._send) as streams:
        await app.run(streams[0], streams[1], app.create_initialization_options())

starlette_app = Starlette(
    routes=[
        Route("/sse", endpoint=handle_sse),
        Route("/messages/", endpoint=sse.handle_post_message, methods=["POST"]),
    ]
)

if __name__ == "__main__":
    print("=" * 70)
    print("ADVANCED MCP SERVER - Linda & Frank ELITE+")
    print("=" * 70)
    print(f"Project: {PROJECT_DIR}")
    print(f"Knowledge Base: {len(KNOWLEDGE_BASE)} chars")
    print(f"Competitive Research: {len(COMPETITIVE_RESEARCH)} chars")
    print("\nADVANCED TOOLS:")
    print("  - analyze_vs_competitor: Direct page comparison")
    print("  - trust_score_audit: Comprehensive trust scoring")
    print("  - find_content_gaps: Competitor content analysis")
    print("  - linda_competitive_design: Design strategy to beat competitors")
    print("  - frank_seo_domination: SEO strategy for #1 ranking")
    print("  - generate_edge_content: Content that beats competitors")
    print("  - schema_validator: Schema markup validation")
    print("  - quick_audit: Fast actionable audit")
    print("\nStarting on port 8080...")
    print("=" * 70)
    uvicorn.run(starlette_app, host="0.0.0.0", port=8080)
