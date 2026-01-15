#!/usr/bin/env python3
"""
Linda - Healthcare Web Design Expert Agent
Specializes in addiction treatment center website design
"""

import anthropic
import os
import json
import time
from pathlib import Path

class HealthcareDesignAgent:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.model = "claude-sonnet-4-20250514"
        self.conversation_history = []

    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def think(self, prompt):
        """Send a message and get a response"""
        self.add_message("user", prompt)

        response = self.client.messages.create(
            model=self.model,
            max_tokens=8000,
            messages=self.conversation_history
        )

        assistant_message = response.content[0].text
        self.add_message("assistant", assistant_message)

        return assistant_message

    def analyze_website(self, html_path, css_path, images_dir):
        """Analyze current website and provide recommendations"""

        # Read current files
        with open(html_path, 'r') as f:
            html_content = f.read()

        with open(css_path, 'r') as f:
            css_content = f.read()

        # List images
        images = list(Path(images_dir).glob('*'))
        image_list = '\n'.join([f"- {img.name} ({img.stat().st_size} bytes)" for img in images])

        prompt = f"""You are an expert healthcare web design specialist with 15+ years of experience designing websites for addiction treatment centers, rehabs, and behavioral health facilities.

Your task is to analyze the current Trust SoCal website and provide a comprehensive redesign plan.

CURRENT WEBSITE FILES:

=== index.html ===
{html_content[:5000]}
...

=== CSS (styles.css) ===
{css_content[:3000]}
...

=== Available Images ===
{image_list}

RESEARCH REQUIREMENTS:

Before making recommendations, research and analyze these top addiction treatment center websites:
1. American Addiction Centers (americanaddictioncenters.org)
2. Hazelden Betty Ford Foundation (hazeldenbettyford.org)
3. Promises Treatment Centers (promises.com)
4. The Canyon Malibu (thecanyonmalibu.com)
5. Passages Malibu (passagesmalibu.com)

ANALYSIS CRITERIA:

For each website, analyze:
- Hero section design and imagery strategy
- Color psychology and branding
- Use of photography vs. illustrations
- Trust-building elements (certifications, testimonials, etc.)
- Layout and information architecture
- Call-to-action placement and design
- Mobile responsiveness patterns
- Typography choices
- Use of whitespace
- Emotional design elements

DELIVERABLES:

1. **Competitive Analysis Summary** - What are the top 3-5 design patterns used by leading rehab centers?

2. **Current Website Audit** - What are the specific problems with the Trust SoCal site?
   - Missing elements
   - Design issues
   - Image usage problems
   - UX/UI issues
   - Trust signals

3. **Redesign Recommendations** - Specific, actionable improvements:
   - Hero section redesign
   - Image strategy (what photos to use where)
   - Layout improvements
   - New sections to add
   - Color/typography refinements
   - Trust-building elements to add

4. **Implementation Plan** - Step-by-step guide to implement changes

Focus on creating a website that:
- Builds trust and credibility
- Evokes hope and healing
- Looks premium and professional
- Converts visitors to phone calls
- Uses the available facility photos effectively

Be specific and thorough. This needs to be production-ready."""

        return self.think(prompt)

    def create_redesign(self):
        """Ask agent to create the actual redesigned files"""
        prompt = """Now, based on your research and recommendations, create the complete redesigned website files.

Provide:
1. Complete new index.html with improved structure
2. Complete new CSS with improved styling
3. Specific instructions for which images to use where

Make sure to:
- Use the sunset image (hero-sunset.jpg) as hero background
- Use facility photos (facility-exterior.jpg, facility-kitchen.jpg, facility-bathroom.jpg, residential-interior.jpg) prominently
- Include trust signals (certifications, years in business, etc.)
- Add testimonial sections
- Improve typography and spacing
- Add professional hover effects and animations
- Include clear CTAs throughout
- Make it look as good as the top rehab websites you researched

Output the complete HTML and CSS code."""

        return self.think(prompt)

def main():
    print("=" * 60)
    print("LINDA - HEALTHCARE WEB DESIGN EXPERT")
    print("Addiction Treatment Center Website Specialist")
    print("=" * 60)
    print()

    agent = HealthcareDesignAgent()

    # Paths
    base_dir = Path(__file__).parent.parent
    html_path = base_dir / "index.html"
    css_path = base_dir / "css" / "styles.css"
    images_dir = base_dir / "images"
    output_dir = base_dir / "agent" / "redesign"
    output_dir.mkdir(exist_ok=True)

    print("📊 PHASE 1: Analyzing current website and researching competitors...")
    print()

    analysis = agent.analyze_website(html_path, css_path, images_dir)

    # Save analysis
    with open(output_dir / "analysis.md", "w") as f:
        f.write(analysis)

    print(analysis)
    print("\n" + "=" * 60)
    print("✅ Analysis complete! Saved to agent/redesign/analysis.md")
    print("=" * 60)
    print()

    print("🎨 PHASE 2: Creating redesigned website...")
    print()

    redesign = agent.create_redesign()

    # Save redesign
    with open(output_dir / "redesign_plan.md", "w") as f:
        f.write(redesign)

    print(redesign)
    print("\n" + "=" * 60)
    print("✅ Redesign complete! Saved to agent/redesign/redesign_plan.md")
    print("=" * 60)
    print()

    print("💡 Next steps:")
    print("1. Review the analysis in agent/redesign/analysis.md")
    print("2. Review the redesign plan in agent/redesign/redesign_plan.md")
    print("3. Extract the HTML/CSS code and implement")
    print()

if __name__ == "__main__":
    main()
