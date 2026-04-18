# Design System for Salam Baku Menu

*Photography-forward restaurant menu inspired by Airbnb's warm, image-first editorial approach — adapted for print (A4 booklet, Cyrillic/Russian).*

## 1. Visual Theme & Atmosphere

Salam Baku's printed menu is a warm, photography-forward booklet that feels like flipping through a food magazine where every page makes you want to order. The design operates on a foundation of textured ivory kraft paper (`#faf8f4`) with the signature **Forest Green** (`#1F3D32`) — pulled from the restaurant's existing brand — serving as the primary anchor color for wordmark, category headings, and ornamental rules. A secondary **Pink Magenta** (`#d94184`) appears only as thin horizontal rules at the top and bottom of each spread, framing the content with a subtle editorial touch.

The typography pairs a **Didone-style display serif** (italic + bold, reserved for category titles and the wordmark) with a **bold uppercase sans-serif** (dish names) and a **regular serif body** (descriptions). The combination produces a voice that is confident, intimate, and slightly theatrical — closer to a Michelin-guide plate than a fast-casual flyer. Slight negative letter-spacing (-0.02em) on display headings creates cozy, intimate titles; wide positive tracking (+0.08em) on dish names gives them gravitas without shouting.

What distinguishes this menu from a generic restaurant template is its commitment to photography as the hero. Each category page reserves 40–70 % of the area for a single large food photograph — half-bleed or full-bleed — with the dish list laid out beside or below it in two disciplined columns. Shadows are soft and three-layered, evoking natural paper depth rather than CSS glow. The result: a calm, photography-led composition that honors Azerbaijani cuisine's visual richness.

**Key Characteristics:**
- Textured ivory kraft-paper background (`#faf8f4`) — never flat white
- Forest Green (`#1F3D32`) as singular brand anchor: wordmark, category headings, ornamental rules
- Pink Magenta (`#d94184`) as thin accent rule only — top and bottom of each page
- Didone-style serif display + bold uppercase sans body + regular serif descriptions
- Cyrillic-first typography — every font must ship Cyrillic subset
- Photography is hero content — half-bleed or full-bleed on every category page
- Near-black warm text (`#1a1a1a`) — never pure `#000000`
- Three-layer soft shadow on featured dish cards: border ring + soft blur + stronger blur
- Generous print margins (14–18 mm) — the page breathes

## 2. Color Palette & Roles

### Primary Brand
- **Forest Green** (`#1F3D32`) — `--color-brand`: wordmark, category headings, ornament rules, footer stamps
- **Deep Forest** (`#14291f`) — `--color-brand-dark`: underlines, separator thick stroke
- **Moss Tint** (`#2d5944`) — `--color-brand-soft`: category eyebrow labels, "Обслуживание 10 %" italic footer

### Accent
- **Pink Magenta** (`#d94184`) — `--color-accent`: thin horizontal frame rules at top/bottom of each page, the one and only non-green, non-ink color on the page
- **Deep Magenta** (`#a41e5f`) — `--color-accent-dark`: reserved for price tiers or premium section markers (use sparingly)

### Text Scale
- **Warm Black** (`#1a1a1a`) — `--text-primary`: dish names, titles (never pure `#000`)
- **Ink Soft** (`#3a3328`) — `--text-body`: dish descriptions, running text
- **Ink Fade** (`#7a7264`) — `--text-muted`: disclaimers, footer, secondary labels
- **Price Green** (`#1F3D32`) — `--text-price`: prices render in brand Forest Green, never in red

### Surface & Rules
- **Paper Ivory** (`#faf8f4`) — `--bg`: main page background (with linen/paper texture overlay)
- **Paper Deep** (`#f0ead9`) — `--bg-alt`: subtle featured-block backgrounds (sets, combos, company platters)
- **Rule Thin** (`rgba(26, 26, 26, 0.15)`) — `--rule`: dotted leader between dish name and price
- **Rule Accent** (`#d94184`) — `--accent-rule`: 1 px pink line at top / bottom of each page

### Shadow (soft paper lift)
- **Card** (`rgba(26, 26, 26, 0.03) 0px 0px 0px 1px, rgba(26, 26, 26, 0.05) 0px 2px 6px, rgba(26, 26, 26, 0.08) 0px 4px 10px`): featured dish photo cards
- **Hover / interactive preview** (`rgba(26, 26, 26, 0.1) 0px 4px 14px`): used only in the HTML preview, removed for print output

## 3. Typography Rules

### Font Families (all must ship Cyrillic)
- **Display** (category headings, wordmark, page titles): `"Playfair Display", "PT Serif", Georgia, serif`
- **Dish name** (bold uppercase sans): `"Inter", "Manrope", "PT Sans", sans-serif`
- **Body / description** (italic serif): `"PT Serif", "Cormorant Garamond", Georgia, serif`
- **Price** (tabular figures): same as dish name, with `font-variant-numeric: tabular-nums`

### Hierarchy

| Role                     | Family        | Size     | Weight | Tracking | Case       | Notes                                             |
| ------------------------ | ------------- | -------- | ------ | -------- | ---------- | ------------------------------------------------- |
| Cover wordmark           | Display       | 56 pt    | 400 it | -0.01em  | mixed      | Italic serif, brand green                         |
| Cover "МЕНЮ"             | Display       | 118 pt   | 400 it | -0.02em  | sentence   | Huge italic, warm black                           |
| Category title           | Display       | 30–34 pt | 700    | -0.01em  | uppercase  | Brand green, tight                                |
| Category subtitle        | Body          | 11 pt    | 400 it | +0.02em  | sentence   | Italic serif, ink-soft                            |
| Eyebrow (Salam Baku · …) | Dish name     | 7.5 pt   | 600    | +0.4em   | uppercase  | Wide tracking, muted                              |
| Dish name                | Dish name     | 10 pt    | 700    | +0.08em  | uppercase  | Warm black, tight leading                         |
| Dish description         | Body          | 8.5 pt   | 400 it | +0.02em  | sentence   | Serif italic, ink-soft                            |
| Price                    | Dish name     | 10 pt    | 600    | +0.02em  | mixed      | Brand green, `tabular-nums`, `kzt` suffix at 7 pt |
| Subsection title         | Display       | 12 pt    | 700 it | +0.1em   | uppercase  | Centered, brand green                             |
| Footer meta              | Body          | 7.5 pt   | 400 it | +0.05em  | sentence   | Ink-fade, italic                                  |

### Principles
- **Warm weight range for display**: 500–700 only. Never 300 or 400 for any bold heading.
- **Intimacy via negative tracking**: -0.01em to -0.02em on large display elements (category headings, cover "МЕНЮ") creates editorial intimacy, not tech coldness.
- **Confidence via wide tracking on dish names**: +0.08em lets each uppercase dish name breathe — this is the *voice* of the menu.
- **Tabular numerics for prices**: `font-variant-numeric: tabular-nums` so 3 790 kzt and 27 000 kzt align vertically in columns.
- **Cyrillic is the default**: select every font weight/style for Cyrillic coverage before Latin. Test with characters: й ы ъ ё Ж Щ Ю Я.

## 4. Component Stylings

### Cover
- Centered composition on ivory background
- Pink accent rule at top (1 px, ~22 mm wide, centered)
- Airbnb-style "warm lift" wordmark: small emblem + `SALAM BAKU` in brand green, `RESTAURANT` at -50 % size below
- Thin green hairline rule above and below the "МЕНЮ" title (22 mm, with small diamond accents at each end)
- Large italic serif "МЕНЮ" in warm black, 118 pt
- Italic subtitle below (Russian tagline, 14 pt ink-soft)
- Pink accent rule at bottom (matching top)

### Category page layout
- **Top frame**: 1 px pink magenta rule, full-width
- **Eyebrow**: `SALAM BAKU · RESTAURANT`, dish-name font, micro size, muted
- **Title**: uppercase display serif in brand green, 30–34 pt
- **Subtitle**: italic one-liner, ink-soft, max 160 mm centered
- **Ornament rule**: centered composition `— ◆ —` or `— ✦ —` in brand green (not gold)
- **Body**: 2-column dish list + 1 photo rail (52–60 mm wide) OR 1-column + full-width hero photo
- **Photo rail**: `.photo-card` with 1.5 mm ivory padding, 1 px thin forest-green border, three-layer soft shadow, 50–100 mm tall
- **Featured-block**: `.set-block` with ivory-deep background, 1 px pink rules top and bottom, the price in display green
- **Bottom frame**: 1 px pink rule, matching top
- **Footer**: `Обслуживание 10 %`, Roman page number `· III ·`, `Все цены указаны в тенге`, all 7.5 pt ink-fade italic

### Dish row (`.item`)
- **Layout**: `[name] ················ [price]` — baseline-aligned horizontal flex
- **Name**: uppercase bold sans, warm black, wide tracking
- **Leader dots**: thin dotted border-bottom, `translateY(-3pt)` so dots sit mid-x-height
- **Price**: `2 790 kzt` — brand green bold, `kzt` at 70 % size in ink-fade
- **Description**: italic serif, ink-soft, one line preferred, wraps softly to two lines max

### Photography treatment
- **Dish photos**: square or 16:10 crops, centered dish, subtle paper background if possible
- **Half-bleed hero**: photo spans across 40–60 % of the page height, touching the page's right or left edge (bleed)
- **Full-bleed hero**: photo fills the page except top/bottom pink rules and the dish list column
- **Caption**: italic serif, centered below card, ink-soft, 7.5 pt

### Subsections (for Шашлыки-style multi-set pages)
- **Divider**: 2 mm top padding, 1 px `--rule` border-top
- **Subsection title**: centered italic display serif, brand green, +0.1em tracking, uppercase
- **Set block**: 2-line featured — full-width name on the left, price on the right, ivory-deep background, pink rules top and bottom
- **Inline item grid**: 3–4 columns, separated by 1 px vertical `--rule` borders, each cell center-aligned

## 5. Layout Principles

### Page Size
- **A4 portrait**: 210 × 297 mm, margin 0 at @page level, inner padding 14 × 14 × 12 mm on `.category`

### Spacing System
- Base unit: 2 mm
- Scale: 1, 2, 3, 4, 5, 7, 10, 14, 18, 22, 30 mm

### Whitespace Philosophy
- **Magazine pacing**: category pages are not packed — every page leaves a calm bottom third of breathing room when the dish list is shorter than the space allows. This is intentional.
- **Photography density**: one large hero photo > multiple small thumbnails. If you have two photos on a page, stagger them (top-right + bottom-left) and make both at least 60 × 60 mm.
- **Margin consistency**: left, right, and bottom margins identical; top margin slightly larger (18 mm) to make room for the pink rule + eyebrow.

### Column System
- Dish list: 2 columns, 8 mm gap, each column 48–55 mm wide
- With photo rail: 2 text columns (1 fr 1 fr) + 1 photo column (52 mm), 7 mm gap
- Subsection inline grid: 3–4 equal fractional columns, 3 mm gap

## 6. Depth & Elevation (paper, not pixels)

| Level              | Treatment                                                                                              | Use                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| Flat (Level 0)     | No shadow                                                                                              | Page background, text blocks                        |
| Paper rise (Lv. 1) | `rgba(26,26,26,0.03) 0 0 0 1px, rgba(26,26,26,0.05) 0 2px 6px, rgba(26,26,26,0.08) 0 4px 10px`         | Featured dish photo cards                           |
| Soft block (Lv. 2) | No shadow; ivory-deep background (`#f0ead9`) + 1 px pink rules top + bottom                            | Featured sets, combos, multi-person dishes          |
| Ornament (Lv. 3)   | 1 px brand-green hairline + small diamond accents (`◆`, `✦`)                                           | Decorative rules around cover title, subsection h3  |

**Shadow philosophy**: on paper, shadow suggests paper depth — not digital glow. Always three layers, always sub-0.1 opacity, always neutral (not colored).

## 7. Do's and Don'ts

### Do
- Use **Forest Green `#1F3D32`** as the ONLY brand color — wordmark, category headings, ornament rules, prices
- Use **Pink Magenta `#d94184`** only as thin frame rules (top + bottom of each page) and rare featured-block accents
- Use textured ivory **`#faf8f4`** as the page background (prefer subtle paper grain / linen texture over flat color)
- Render ALL fonts with Cyrillic subset — dishes are in Russian
- Use `tabular-nums` for prices so columns align
- Let photography lead — every category page gets at least one large food photo (half or full bleed)
- Use three-layer soft shadow on photo cards (paper lift, not digital glow)
- Apply -0.01em to -0.02em tracking on display headings; +0.08em tracking on uppercase dish names
- Keep `@page` margins at 0, `.page` dimensions at exactly 210 × 297 mm for A4 print
- Append `kzt` suffix at 70 % size in ink-fade after every price

### Don't
- Don't use cream + burgundy + gold — that's Victorian / classical, wrong era for Salam Baku
- Don't use pure black `#000000` for text — always warm `#1a1a1a`
- Don't introduce decorative fleurons, corner flourishes, or Victorian filigree
- Don't use thin font weights (300, 400) for any bold heading or dish name
- Don't wrap the whole page in a border frame — only thin horizontal pink rules at top + bottom
- Don't render prices in red / pink — prices are always brand green
- Don't use color for featured blocks — use the ivory-deep background + pink rules trick instead
- Don't forget Cyrillic coverage — test every weight/style with й ы ъ ё Ж Щ Ю Я
- Don't pack category pages — magazine pacing means empty bottom third is ok on short lists
- Don't use rounded corners beyond 2 mm — print aesthetics favor subtle straight edges (≠ Airbnb's 20 px web UI rounding)

## 8. Print Behavior

### Page Rules
```css
@page {
  size: A4 portrait;     /* 210 × 297 mm */
  margin: 0;             /* .page has explicit dims */
}
.page {
  width: 210mm;
  height: 297mm;
  page-break-after: always;
  break-after: page;
}
```

### Bleed (optional, for professional print shops)
- If the output will be trimmed: add 3 mm bleed on all sides → `size: 216mm 303mm`, `.page` 216 × 303 mm with content at 3 mm inset
- Add crop marks at each corner using small `::before` / `::after` pseudo-elements

### Color Management
- Export PDF in RGB first (simpler pipeline); convert to CMYK via Acrobat / Preview if the printer requires it
- Avoid large pure-white or pure-black areas — textured ivory naturally prints warmer

### Font Loading
- Use Google Fonts CDN with `subset=cyrillic,cyrillic-ext,latin` query param
- Include a `font-display: swap` fallback stack in case CDN fails

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: `#faf8f4` (paper ivory, add linen texture in production)
- Text: `#1a1a1a` (warm black)
- Brand: `#1F3D32` (forest green) — wordmark, headings, prices, rules
- Accent: `#d94184` (pink magenta) — thin top + bottom page rules ONLY
- Body ink: `#3a3328`
- Muted: `#7a7264`
- Featured-block surface: `#f0ead9`

### Example Component Prompts
- "Create a category page: A4 portrait, ivory background. Pink 1 px rule at top and bottom. Top: eyebrow `SALAM BAKU · RESTAURANT` 7.5 pt tracked, centered; title `САЛАТЫ С МАЙОНЕЗОМ` in Playfair Display 32 pt 700 uppercase forest green -0.01em tracking; italic serif subtitle below. Centered ornament rule `— ◆ —` in forest green. Body: 2 text columns (1 fr 1 fr) + 52 mm photo rail. Each dish row: uppercase Inter 700 +0.08em name on left, dotted leader, forest-green price with `kzt` suffix on right; italic serif description below. Photo card: 1.5 mm ivory padding, 1 px forest-green border, three-layer soft shadow, 50 mm tall, italic caption centered below."
- "Design the cover: ivory background, 1 px pink rule top and bottom. Centered: circular emblem (1 px forest-green border) next to `SALAM BAKU` wordmark in Playfair Display 20 pt 600 +0.18em uppercase forest green, with `RESTAURANT` in 7 pt 400 +0.5em below. Two hairline forest-green rules above and below the main title. Title `Меню` in Playfair Display italic 118 pt warm black. Italic subtitle `Подлинные вкусы Баку в сердце города` in Cormorant 14 pt ink-soft."
- "Design the Шашлыки subsection block: 1 px forest-green rule top. Centered subsection title `Шашлык из рыбы` in Playfair italic 12 pt 700 forest green +0.1em uppercase. Below: 4-column inline grid (Сёмга / Дорадо / Форель / Скумбрия), 1 px vertical rules between columns, each cell center-aligned: dish name Inter 700 8.5 pt uppercase + description Cormorant italic 7 pt + price Inter 600 9 pt forest green with `kzt` suffix."
- "Design a featured set block: 2 mm padding, ivory-deep `#f0ead9` background, 1 px pink rules top and bottom. Left: `СЕТ ШАШЛЫКОВ` Inter 700 11 pt uppercase +0.08em warm black. Right: `18 000 kzt` Inter 600 12 pt forest green tabular-nums. Italic serif description below, centered, 7.5 pt ink-soft."

### Iteration Guide
1. Start with the textured ivory page — color comes from photography and the two brand accents only
2. Forest green (`#1F3D32`) is the anchor — wordmark, headings, prices, ornamental rules all use it
3. Pink magenta (`#d94184`) is the single accent — thin top + bottom page rules, nothing else
4. Warm-black (`#1a1a1a`) text — warmth matters, pure black feels harsh on ivory
5. Three-layer paper-soft shadows on photo cards — never colored, never >0.1 opacity
6. Display serif (Playfair Display) for headings; bold sans (Inter) uppercase +0.08em for dish names; italic serif for descriptions
7. Photography is hero — each category page gets at least one half- or full-bleed food photo
8. Cyrillic is mandatory — test every font weight with й ы ъ ё Ж Щ Ю Я before shipping
9. Print in A4 portrait, 0 @page margin, 14 × 14 × 12 mm inner padding — and let the page breathe
