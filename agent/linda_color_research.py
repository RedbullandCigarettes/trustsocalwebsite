#!/usr/bin/env python3
"""
Linda's Behavioral Health Color Psychology Research
Deep dive into what colors actually work in addiction treatment
"""

import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

print("=" * 70)
print("LINDA - COLOR PSYCHOLOGY RESEARCH")
print("Behavioral Health & Addiction Treatment Color Analysis")
print("=" * 70)
print()
print("🎨 Linda is conducting deep research on behavioral health colors...")
print()
print("Research Focus:")
print("  • Top 10 rehab facility website color schemes")
print("  • Color psychology in behavioral health")
print("  • What converts vs. what repels patients")
print("  • Eliminating aggressive orange/red tones")
print()
print("=" * 70)
print()

research_prompt = """You are Linda, a healthcare web design expert specializing in behavioral health.

CRITICAL ISSUE: The current Trust SoCal website uses aggressive orange (#c77124) that doesn't work for behavioral health. You need to find what ACTUALLY works.

DEEP RESEARCH ASSIGNMENT:

Analyze these 10 top behavioral health websites and document their EXACT color schemes:

1. **American Addiction Centers** (americanaddictioncenters.org)
2. **Hazelden Betty Ford** (hazeldenbettyford.org)
3. **The Canyon Malibu** (thecanyonmalibu.com)
4. **Promises Treatment Centers** (promises.com)
5. **Passages Malibu** (passagesmalibu.com)
6. **Sierra Tucson** (sierratucson.com)
7. **Betty Ford Center** (bettyfordcenter.org)
8. **Caron Treatment Centers** (caron.org)
9. **Mountainside Treatment** (mountainside.com)
10. **Newport Academy** (newportacademy.com)

FOR EACH WEBSITE, DOCUMENT:

**Color Analysis Table:**
| Element | Color | Hex Code | Psychology |
|---------|-------|----------|------------|
| Primary Brand | [describe] | #XXXXX | [emotion evoked] |
| Secondary Accent | [describe] | #XXXXX | [emotion evoked] |
| CTA Buttons | [describe] | #XXXXX | [urgency level] |
| Background | [describe] | #XXXXX | [feeling created] |
| Text | [describe] | #XXXXX | [readability] |

**THEN PROVIDE:**

## 1. COLOR PATTERN ANALYSIS

What colors dominate successful behavioral health websites?
- Blues: What % use blue as primary? What shades?
- Greens: What % use green? What psychology?
- Earth tones: Browns, tans, beiges - when and why?
- Purples: Any use? What message?
- What colors are AVOIDED entirely?

## 2. COLOR PSYCHOLOGY FOR BEHAVIORAL HEALTH

**Blues:**
- Navy/Dark Blue (#[hex]): Trust, stability, medical credibility
- Medium Blue (#[hex]): Calm, peace, professionalism
- Light Blue (#[hex]): Hope, sky, new beginnings

**Greens:**
- Sage/Muted Green (#[hex]): Healing, nature, growth
- Forest Green (#[hex]): Grounding, earth, stability
- Teal/Aqua (#[hex]): Tranquility, balance

**Warm Accents (NOT aggressive):**
- Gold/Honey (#[hex]): Warmth without urgency
- Terracotta/Clay (#[hex]): Earthiness, comfort
- Sage Rose (#[hex]): Compassion, gentleness

**AVOID:**
- Bright Red: Aggression, danger, stress
- Bright Orange: Urgency, alarm, pressure
- Neon anything: Unprofessional, jarring

## 3. TRUST SOCAL RECOMMENDATIONS

Based on your research, provide:

**New Color Scheme:**
```
Primary Color: [Name] #XXXXXX
Reason: [Why this works for behavioral health]
Examples: [Which top sites use similar]

Accent Color 1: [Name] #XXXXXX
Reason: [Psychology and purpose]
Examples: [Which top sites use similar]

Accent Color 2: [Name] #XXXXXX
Reason: [When and how to use]
Examples: [Which top sites use similar]

Background: [Name] #XXXXXX
Reason: [How it creates space]

Text: [Name] #XXXXXX
Reason: [Readability and emotion]
```

## 4. CONVERSATION WITH FRANK (SEO EXPERT)

Prepare these talking points:

**How Color Impacts SEO:**
- Trust signals → Lower bounce rate
- Professional colors → Longer time on site
- Calming palette → More form completions
- Medical credibility → Better brand authority

**Conversion Psychology:**
- Crisis intervention: What color CTAs work best?
- Insurance verification: What colors reduce anxiety?
- Family inquiries: What colors build trust?

## 5. BEFORE & AFTER

**Current (Problems):**
- Navy #1d2758: Good - keep
- Orange #c77124: TOO AGGRESSIVE - replace with [your recommendation]

**Recommended:**
- Primary: #XXXXXX because [reason]
- Accent 1: #XXXXXX because [reason]
- Accent 2: #XXXXXX because [reason]

Be specific with hex codes. This will be implemented immediately.
"""

print("🔍 Analyzing top 10 behavioral health websites...")
print("⏱️  This will take about 2 minutes...")
print()

response = client.messages.create(
    model='claude-sonnet-4-20250514',
    max_tokens=16000,
    messages=[{'role': 'user', 'content': research_prompt}]
)

research = response.content[0].text

# Save the research
with open('linda_color_research.md', 'w') as f:
    f.write("# Linda's Behavioral Health Color Psychology Research\n\n")
    f.write(research)

print(research)
print()
print("=" * 70)
print("✅ Color research complete!")
print("📄 Saved to: agent/linda_color_research.md")
print("=" * 70)
print()
print("📞 Linda is now ready to discuss findings with Frank...")
