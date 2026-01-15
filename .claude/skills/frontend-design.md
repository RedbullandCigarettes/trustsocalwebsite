# Frontend Design Skill for Trust SoCal

## Design Direction: Serene Recovery Aesthetic

This addiction treatment website should evoke **trust, calm, hope, and professionalism**. The aesthetic is "Coastal California Recovery" - clean, warm, and aspirational.

## Typography Rules

**DO:**
- Use Playfair Display for headings (elegant, trustworthy)
- Use Inter for body text (clean, readable)
- Large, confident heading sizes (2.5-4rem for h1)
- Generous line-height (1.6-1.8 for body)

**DON'T:**
- Mix more than 2 font families
- Use thin/light weights for important text
- Crowd text together

## Color Palette (STRICT)

```css
--primary-teal: #2E8B8B;      /* Trust, calm - primary brand */
--primary-orange: #E07850;    /* Warmth, hope - accent/CTA */
--cream-white: #FAF9F6;       /* Soft backgrounds */
--warm-gray: #4A4A4A;         /* Body text */
--soft-teal: #E8F4F4;         /* Highlights, cards */
```

**Rules:**
- Teal dominates (60%) - headers, logos, primary elements
- Orange for CTAs and accents only (10%)
- Cream/white backgrounds (30%)
- Never use pure black (#000) - use warm gray instead

## Header/Logo Standards

The header logo MUST display:
- Logo image (50x50) on LEFT
- Text on RIGHT of image (side-by-side, not stacked)
- "Trust SoCal" in teal, 24px, bold
- Tagline below in orange, 12px, uppercase

```css
.logo a {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 12px;
}
```

## Motion & Interaction

**Subtle, professional animations:**
- Fade-in on scroll (0.3s ease)
- Hover states: slight lift (translateY -2px) + shadow
- Button hovers: background color shift, not dramatic transforms
- Page load: gentle fade-in, no flashy entrances

**DON'T:**
- Bounce or elastic animations (too playful for healthcare)
- Aggressive color transitions
- Anything that feels "gimmicky"

## Card & Section Design

- Soft shadows: `0 4px 20px rgba(0,0,0,0.08)`
- Rounded corners: 12-16px for cards, 8px for buttons
- Generous padding: 40-60px for sections
- White/cream card backgrounds on soft gray page background

## CTA Buttons

```css
.btn-primary {
    background: var(--primary-orange);
    color: white;
    padding: 16px 32px;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s ease;
}
.btn-primary:hover {
    background: #c96840;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(224, 120, 80, 0.3);
}
```

## Healthcare Trust Signals

Always visible:
- Joint Commission Accredited badge
- 24/7 support phone number
- Professional imagery (no stock photo clichés)
- Clean, uncluttered layouts

## What Makes This a 10/10

1. **Cohesive** - Every element follows the same design language
2. **Trustworthy** - Professional, not flashy
3. **Accessible** - High contrast, readable fonts
4. **Calming** - Teal/cream palette evokes peace
5. **Action-oriented** - Clear CTAs in warm orange
6. **Fast** - No heavy animations or effects
