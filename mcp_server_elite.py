#!/usr/bin/env python3
"""
Elite MCP Server - Linda & Frank
Top-tier agents for treatment center website optimization

Linda: Avant-garde designer who thinks like someone searching for help
Frank: SEO expert who thinks like someone desperate to find the right facility
"""

import os
import json
import asyncio
import requests
import subprocess
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from mcp.types import Tool, TextContent
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import Response
import anthropic
import uvicorn

# Initialize
app = Server("linda-frank-elite")
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

# Project directory - configurable
PROJECT_DIR = os.environ.get('PROJECT_DIR', '/home/ubuntu/trust-socal')

# =============================================================================
# ELITE PERSONAS - WITH PATIENT/FAMILY EMPATHY
# =============================================================================

LINDA_ELITE = '''You are Linda, an elite healthcare web designer with 20+ years of experience designing for treatment centers.

## YOUR SUPERPOWER
You don't just design websites - you think like someone who is:
- Searching for treatment at 2am, scared and desperate
- A parent who just found out their child is using
- A spouse who's watching their partner destroy themselves
- Someone who's been to 3 rehabs already and is skeptical
- A professional terrified of anyone finding out

## WHAT YOU KNOW ABOUT PEOPLE SEEKING TREATMENT
1. They're often in crisis - design must be CALMING, not overwhelming
2. They're skeptical of flashy marketing - authenticity wins
3. They need to see REAL people, not stock photos of models
4. They want proof it works - but not in a salesy way
5. They're scared of judgment - design must feel welcoming, not clinical
6. They often search on mobile, late at night, hiding from family
7. They need the phone number IMMEDIATELY visible
8. They want to know: "Will my insurance cover this?"

## YOUR DESIGN PRINCIPLES FOR TREATMENT CENTERS
- **Trust over flash**: Warm, professional, not "luxury spa marketing"
- **Calm colors**: Soft blues, greens, warm neutrals - NOT harsh or clinical
- **Real imagery**: Actual facility, actual staff, actual nature nearby
- **Clear hierarchy**: Phone number, insurance, programs - in that order
- **Mobile-first**: 70% will visit on phones, often in private
- **Accessibility**: People in crisis may have impaired vision/cognition
- **White space**: Let the page breathe - mirror the peace they're seeking
- **Authentic testimonials**: Video > text, specific details > vague praise

## TRUST SIGNALS YOU LOOK FOR
- Staff photos with credentials
- Accreditation badges (CARF, Joint Commission)
- State licensing visible
- Success metrics (if honest and verifiable)
- Insurance logos
- Physical address visible
- Real reviews linked to Google/Yelp

## RED FLAGS THAT DESTROY TRUST
- Stock photos of happy models in white robes
- No physical address
- "Luxury" marketing that feels disconnected from recovery
- Aggressive pop-ups or chat bots
- Vague claims without evidence
- No staff bios or credentials
- Hidden pricing/insurance info

When you analyze a site, you FEEL what a desperate family member would feel.
You score based on: Would I trust my child's life to this place?'''

FRANK_ELITE = '''You are Frank, an elite SEO specialist who has spent 15+ years in healthcare marketing, specifically addiction and mental health treatment.

## YOUR SUPERPOWER
You don't just optimize for Google - you think like someone searching for help:
- "rehab near me that takes blue cross"
- "is my husband an alcoholic quiz"
- "how to convince someone to go to rehab"
- "best drug rehab orange county reviews"
- "how much does rehab cost without insurance"

## WHAT YOU KNOW ABOUT TREATMENT SEEKERS
1. They search different things at different stages:
   - Awareness: "signs of alcoholism" "is my son on drugs"
   - Consideration: "types of rehab programs" "inpatient vs outpatient"
   - Decision: "best rehab [city]" "[facility name] reviews"

2. They're YMYL (Your Money Your Life) searchers - Google scrutinizes heavily
3. They often search for loved ones, not themselves
4. Local intent is MASSIVE - "near me" queries
5. Insurance queries are high-value: "[insurance] rehab coverage"
6. They want answers, not sales pitches
7. Mobile-first, often late night searches

## YOUR SEO PRINCIPLES FOR TREATMENT CENTERS
- **E-E-A-T is EVERYTHING**: Experience, Expertise, Authoritativeness, Trust
- **Local SEO**: Google Business Profile, local citations, location pages
- **Schema markup**: MedicalOrganization, LocalBusiness, FAQPage, Review
- **Content depth**: Answer every question they might have
- **Author expertise**: Bios for all content writers with credentials
- **Fresh content**: Blog with genuine helpful content
- **Technical excellence**: Core Web Vitals, mobile-first, fast loading

## WHAT GOOGLE WANTS TO SEE FOR TREATMENT CENTERS
- Licensed medical professionals listed with credentials
- Physical address and phone number on every page
- Clear accreditation (CARF, Joint Commission, state license)
- Detailed program descriptions
- Transparent pricing/insurance information
- Real patient testimonials (HIPAA-compliant)
- Expertise signals: staff credentials, years of experience
- Contact information: multiple ways to reach real people

## KEYWORDS THAT MATTER (Treatment Center Context)
- "[City/Region] drug rehab"
- "[City/Region] alcohol treatment center"
- "[Insurance name] drug rehab coverage"
- "detox center near me"
- "mental health treatment [city]"
- "dual diagnosis treatment center"
- "[Condition] treatment program" (anxiety, depression, PTSD, trauma)

## RED FLAGS THAT KILL RANKINGS
- Thin content with no expertise signals
- No author bios on medical/health content
- Missing or incomplete schema markup
- Slow page speed (especially mobile)
- No Google Business Profile or inconsistent NAP
- Duplicate content across location pages
- Aggressive sales language without educational value
- Missing privacy policy, terms of service

When you audit a site, you think: Would Google trust this site with someone's life?
You score based on: Would this rank AND convert someone in crisis?'''

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def fetch_webpage(url):
    """Fetch and parse a webpage comprehensively."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        result = {"url": url, "status": response.status_code}

        # Title
        title = soup.find('title')
        result['title'] = title.get_text().strip() if title else None

        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        result['meta_description'] = meta_desc.get('content', '') if meta_desc else None

        # Headings
        headings = {}
        for level in range(1, 7):
            h_tags = soup.find_all(f'h{level}')
            if h_tags:
                headings[f'h{level}'] = [h.get_text().strip() for h in h_tags[:10]]
        result['headings'] = headings

        # Schema
        schemas = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                schemas.append(json.loads(script.string))
            except:
                pass
        result['schema'] = schemas if schemas else None

        # Images with analysis
        images = []
        for img in soup.find_all('img')[:20]:
            img_data = {
                "src": img.get('src', '')[:150],
                "alt": img.get('alt', ''),
                "has_alt": bool(img.get('alt', '').strip()),
                "likely_stock": 'stock' in img.get('src', '').lower() or 'shutterstock' in img.get('src', '').lower()
            }
            images.append(img_data)
        result['images'] = images
        result['images_without_alt'] = sum(1 for img in images if not img['has_alt'])

        # Links
        internal_links = []
        external_links = []
        for a in soup.find_all('a', href=True):
            href = a.get('href', '')
            if href.startswith('http') and url.split('/')[2] not in href:
                external_links.append(href[:100])
            elif href.startswith('/') or href.startswith('#'):
                internal_links.append(href)
        result['internal_links'] = len(internal_links)
        result['external_links'] = external_links[:10]

        # Phone numbers
        import re
        text = soup.get_text()
        phones = re.findall(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4}', text)
        result['phone_numbers'] = list(set(phones))[:5]

        # Trust signals
        trust_signals = {
            'has_address': bool(re.search(r'\d+\s+[\w\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd)', text, re.I)),
            'has_accreditation': any(term in text.lower() for term in ['carf', 'joint commission', 'jcaho', 'accredited', 'licensed']),
            'has_insurance_section': any(term in text.lower() for term in ['insurance', 'blue cross', 'aetna', 'cigna', 'united health']),
            'has_staff_section': any(term in text.lower() for term in ['our team', 'our staff', 'meet our', 'clinical team']),
            'has_testimonials': any(term in text.lower() for term in ['testimonial', 'review', 'success stor', 'patient stor']),
        }
        result['trust_signals'] = trust_signals

        # Content sample
        for tag in soup(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()
        main = soup.find('main') or soup.find('article') or soup.find('body')
        if main:
            result['content_sample'] = main.get_text(separator=' ', strip=True)[:3000]

        # Meta robots
        robots = soup.find('meta', attrs={'name': 'robots'})
        result['meta_robots'] = robots.get('content', '') if robots else 'not set'

        # Canonical
        canonical = soup.find('link', rel='canonical')
        result['canonical'] = canonical.get('href', '') if canonical else 'not set'

        return result
    except Exception as e:
        return {"url": url, "error": str(e)}

def run_agent(persona, task, context, model="claude-sonnet-4-20250514"):
    """Run an elite agent with comprehensive context."""
    prompt = f"""{task}

## CONTEXT
{json.dumps(context, indent=2) if isinstance(context, dict) else context}

Remember: Think like someone searching for treatment for themselves or a loved one.
What would make them TRUST this? What would make them LEAVE?"""

    response = client.messages.create(
        model=model,
        max_tokens=8000,
        system=persona,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def read_local_file(filepath):
    """Read a local file."""
    try:
        full_path = os.path.join(PROJECT_DIR, filepath) if not filepath.startswith('/') else filepath
        with open(full_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def write_local_file(filepath, content):
    """Write to a local file."""
    try:
        full_path = os.path.join(PROJECT_DIR, filepath) if not filepath.startswith('/') else filepath
        # Create backup
        if os.path.exists(full_path):
            backup_path = f"{full_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            with open(full_path, 'r') as f:
                with open(backup_path, 'w') as b:
                    b.write(f.read())
        # Write new content
        with open(full_path, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error writing file: {e}"

def list_project_files(directory=""):
    """List files in project directory."""
    try:
        target = os.path.join(PROJECT_DIR, directory)
        files = []
        for item in os.listdir(target):
            path = os.path.join(target, item)
            files.append({
                "name": item,
                "type": "directory" if os.path.isdir(path) else "file",
                "size": os.path.getsize(path) if os.path.isfile(path) else None
            })
        return files
    except Exception as e:
        return f"Error listing files: {e}"

# =============================================================================
# MCP TOOLS
# =============================================================================

@app.list_tools()
async def list_tools():
    return [
        # Analysis Tools
        Tool(
            name="linda_analyze",
            description="Linda analyzes a webpage from the perspective of someone searching for treatment. Evaluates design, UX, trust signals, and emotional impact.",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "The URL to analyze"}
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="frank_audit",
            description="Frank performs comprehensive SEO audit thinking like someone desperate to find the right treatment center. Covers E-E-A-T, local SEO, schema, and conversion.",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "The URL to audit"}
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="linda_frank_collaborate",
            description="Linda and Frank work together to provide comprehensive analysis and actionable recommendations for a treatment center website.",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "The URL to analyze"}
                },
                "required": ["url"]
            }
        ),
        # File Tools
        Tool(
            name="read_file",
            description="Read a file from the project directory",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {"type": "string", "description": "Path to the file (relative to project root)"}
                },
                "required": ["filepath"]
            }
        ),
        Tool(
            name="write_file",
            description="Write content to a file in the project directory (creates backup first)",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {"type": "string", "description": "Path to the file"},
                    "content": {"type": "string", "description": "Content to write"}
                },
                "required": ["filepath", "content"]
            }
        ),
        Tool(
            name="list_files",
            description="List files in the project directory",
            inputSchema={
                "type": "object",
                "properties": {
                    "directory": {"type": "string", "description": "Subdirectory to list (optional)", "default": ""}
                }
            }
        ),
        # Research Tools
        Tool(
            name="research_competitor",
            description="Linda and Frank research a competitor treatment center website together",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Competitor URL to research"}
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="generate_content",
            description="Frank generates SEO-optimized content for a specific page or topic, with Linda's input on emotional resonance",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "Topic or page type to create content for"},
                    "keywords": {"type": "string", "description": "Target keywords (comma-separated)"},
                    "page_type": {"type": "string", "description": "Type of page: homepage, service, location, condition, blog"}
                },
                "required": ["topic", "page_type"]
            }
        ),
        Tool(
            name="linda_design_review",
            description="Linda reviews a local HTML/CSS file and provides design improvement recommendations",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {"type": "string", "description": "Path to HTML or CSS file to review"}
                },
                "required": ["filepath"]
            }
        ),
        Tool(
            name="frank_seo_review",
            description="Frank reviews a local HTML file for SEO issues and provides fixes",
            inputSchema={
                "type": "object",
                "properties": {
                    "filepath": {"type": "string", "description": "Path to HTML file to review"}
                },
                "required": ["filepath"]
            }
        ),
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    log_msg = f"[{datetime.now()}] Tool: {name}, Args: {json.dumps(arguments)[:200]}"
    print(log_msg)
    with open('mcp_elite.log', 'a') as f:
        f.write(log_msg + '\n')

    try:
        # === ANALYSIS TOOLS ===
        if name == "linda_analyze":
            url = arguments.get("url")
            page_data = fetch_webpage(url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            task = """## DESIGN & TRUST ANALYSIS

Analyze this treatment center page as if you were a desperate parent searching for help at 2am.

Provide:
1. **First Impression (0-10)**: What do you FEEL in the first 3 seconds?
2. **Trust Score (0-10)**: Would you trust your child's life to this place?
3. **Visual Hierarchy**: Is the most important info (phone, insurance) immediately visible?
4. **Authenticity Check**: Real photos or stock? Genuine or salesy?
5. **Mobile Experience**: Would this work for someone hiding in a bathroom searching on their phone?
6. **Emotional Design**: Does it offer HOPE without being fake?
7. **Red Flags**: Anything that would make someone leave immediately?

## PRIORITY FIXES (Top 5)
List the 5 most impactful changes to increase trust and conversions."""

            result = run_agent(LINDA_ELITE, task, page_data)
            return [TextContent(type="text", text=f"# LINDA'S ELITE ANALYSIS\n\n{result}")]

        elif name == "frank_audit":
            url = arguments.get("url")
            page_data = fetch_webpage(url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            task = """## COMPREHENSIVE SEO AUDIT

Analyze this treatment center page as if you were consulting for a facility that needs to rank AND convert.

Provide:
1. **YMYL Compliance (0-10)**: Does this meet Google's standards for health content?
2. **E-E-A-T Score (0-10)**: Experience, Expertise, Authoritativeness, Trust signals?
3. **Technical SEO**:
   - Title tag analysis
   - Meta description analysis
   - Heading structure (H1-H6)
   - Schema markup review
   - Canonical/robots
4. **Local SEO**: NAP consistency, location signals, Google Business readiness
5. **Content Quality**: Depth, expertise signals, author credentials
6. **Trust Signals Found**: Accreditations, licenses, insurance, contact info
7. **Conversion Optimization**: Is it easy to take action?

## PRIORITY FIXES (Top 5)
List the 5 most impactful SEO improvements with specific implementation details."""

            result = run_agent(FRANK_ELITE, task, page_data)
            return [TextContent(type="text", text=f"# FRANK'S ELITE SEO AUDIT\n\n{result}")]

        elif name == "linda_frank_collaborate":
            url = arguments.get("url")
            page_data = fetch_webpage(url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            # Linda's analysis
            linda_task = """Analyze design, UX, and trust from the perspective of someone searching for treatment.
Focus on: First impression, authenticity, emotional design, mobile experience, trust signals.
Be specific and actionable. Rate key areas 0-10."""
            linda_result = run_agent(LINDA_ELITE, linda_task, page_data)

            # Frank's analysis
            frank_task = """Analyze SEO and conversion from the perspective of someone desperate to find help.
Focus on: E-E-A-T, technical SEO, local signals, content quality, conversion paths.
Be specific and actionable. Rate key areas 0-10."""
            frank_result = run_agent(FRANK_ELITE, frank_task, page_data)

            # Combined synthesis
            synthesis_prompt = f"""Linda and Frank have analyzed this treatment center website.

LINDA'S FINDINGS:
{linda_result}

FRANK'S FINDINGS:
{frank_result}

Create a unified action plan that:
1. Identifies the TOP 10 priorities (combining design + SEO)
2. Orders them by impact (what will help the most people find and trust this facility)
3. Provides specific implementation steps for each
4. Estimates effort level (Quick Win / Medium / Major Project)

Think like you're advising a treatment center owner who wants to SAVE MORE LIVES by being found and trusted online."""

            synthesis = run_agent(
                "You are a senior consultant synthesizing Linda (design) and Frank's (SEO) recommendations into a unified action plan.",
                synthesis_prompt,
                page_data
            )

            result = f"""# LINDA & FRANK COLLABORATIVE ANALYSIS
## URL: {url}

---

# LINDA'S DESIGN & TRUST REVIEW

{linda_result}

---

# FRANK'S SEO & CONVERSION AUDIT

{frank_result}

---

# UNIFIED ACTION PLAN

{synthesis}
"""
            return [TextContent(type="text", text=result)]

        # === FILE TOOLS ===
        elif name == "read_file":
            filepath = arguments.get("filepath")
            content = read_local_file(filepath)
            return [TextContent(type="text", text=content)]

        elif name == "write_file":
            filepath = arguments.get("filepath")
            content = arguments.get("content")
            result = write_local_file(filepath, content)
            return [TextContent(type="text", text=result)]

        elif name == "list_files":
            directory = arguments.get("directory", "")
            files = list_project_files(directory)
            if isinstance(files, str):  # Error message
                return [TextContent(type="text", text=files)]
            result = f"## Files in {directory or 'project root'}\n\n"
            for f in files:
                icon = "📁" if f['type'] == 'directory' else "📄"
                size = f" ({f['size']} bytes)" if f['size'] else ""
                result += f"{icon} {f['name']}{size}\n"
            return [TextContent(type="text", text=result)]

        # === RESEARCH TOOLS ===
        elif name == "research_competitor":
            url = arguments.get("url")
            page_data = fetch_webpage(url)
            if "error" in page_data:
                return [TextContent(type="text", text=f"Error: {page_data['error']}")]

            task = """Analyze this COMPETITOR treatment center website.

Identify:
1. **What they do WELL** that we should learn from
2. **What they do POORLY** that we can beat them on
3. **Unique value propositions** they're claiming
4. **Trust signals** they're using
5. **SEO strategy** (keywords they're targeting, content approach)
6. **Design patterns** worth noting

How can we DIFFERENTIATE and provide MORE VALUE to someone searching for treatment?"""

            result = run_agent(LINDA_ELITE + "\n\n" + FRANK_ELITE, task, page_data)
            return [TextContent(type="text", text=f"# COMPETITOR RESEARCH: {url}\n\n{result}")]

        elif name == "generate_content":
            topic = arguments.get("topic")
            keywords = arguments.get("keywords", "")
            page_type = arguments.get("page_type")

            task = f"""Generate SEO-optimized, emotionally resonant content for a treatment center.

TOPIC: {topic}
PAGE TYPE: {page_type}
TARGET KEYWORDS: {keywords}

Requirements:
1. Write from a place of genuine empathy - someone is reading this at their lowest point
2. Include E-E-A-T signals (expertise, credentials, experience)
3. Optimize for target keywords naturally
4. Include clear calls-to-action that don't feel pushy
5. Address common fears and objections
6. Provide genuine value and information

Format the content with proper HTML structure (headings, paragraphs, lists).
Include meta title and description suggestions."""

            result = run_agent(FRANK_ELITE, task, {"topic": topic, "keywords": keywords, "page_type": page_type})
            return [TextContent(type="text", text=f"# GENERATED CONTENT\n\n{result}")]

        elif name == "linda_design_review":
            filepath = arguments.get("filepath")
            content = read_local_file(filepath)
            if content.startswith("Error"):
                return [TextContent(type="text", text=content)]

            task = """Review this HTML/CSS file from a design perspective.

Think like someone who just Googled "best rehab near me" and landed on this page.

Provide:
1. **Visual hierarchy issues**
2. **Trust signal placement**
3. **Color/typography concerns**
4. **Mobile responsiveness issues**
5. **Specific CSS/HTML fixes with code examples**"""

            result = run_agent(LINDA_ELITE, task, {"filepath": filepath, "content": content[:15000]})
            return [TextContent(type="text", text=f"# LINDA'S DESIGN REVIEW: {filepath}\n\n{result}")]

        elif name == "frank_seo_review":
            filepath = arguments.get("filepath")
            content = read_local_file(filepath)
            if content.startswith("Error"):
                return [TextContent(type="text", text=content)]

            task = """Review this HTML file for SEO issues.

Provide:
1. **Title tag analysis and fix**
2. **Meta description analysis and fix**
3. **Heading structure fixes**
4. **Schema markup recommendations (with code)**
5. **Internal linking opportunities**
6. **Content optimization suggestions**

Include specific code fixes I can implement."""

            result = run_agent(FRANK_ELITE, task, {"filepath": filepath, "content": content[:15000]})
            return [TextContent(type="text", text=f"# FRANK'S SEO REVIEW: {filepath}\n\n{result}")]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        error_msg = f"Error in {name}: {str(e)}"
        print(error_msg)
        return [TextContent(type="text", text=error_msg)]

# =============================================================================
# SERVER SETUP
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
    print("=" * 60)
    print("ELITE MCP SERVER - Linda & Frank")
    print("=" * 60)
    print(f"Project Directory: {PROJECT_DIR}")
    print("\nTools available:")
    print("  - linda_analyze: Design & trust analysis")
    print("  - frank_audit: SEO & conversion audit")
    print("  - linda_frank_collaborate: Combined analysis")
    print("  - read_file: Read project files")
    print("  - write_file: Write project files")
    print("  - list_files: List project directory")
    print("  - research_competitor: Analyze competitor sites")
    print("  - generate_content: Create SEO content")
    print("  - linda_design_review: Review local HTML/CSS")
    print("  - frank_seo_review: Review local HTML for SEO")
    print("\nStarting server on port 8080...")
    print("=" * 60)
    uvicorn.run(starlette_app, host="0.0.0.0", port=8080)
