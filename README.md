# Salam Baku — Menü (design source)

Print-ready HTML+CSS source for the Salam Baku Restaurant menu (25 pages, A4 portrait, Russian/Cyrillic, Azerbaijani cuisine).

## Structure

- `src/index.html` — pilot pages (cover + 4 categories)
- `src/styles.css` — design tokens + layout (classic "Bakü Elegance" theme)
- `content/pilot.json` — structured menu content (dishes, prices, descriptions)
- `assets/photos/` — cropped dish photos (demo quality, from existing menu)
- `scripts/crop-photos.py` — photo cropping pipeline
- `render.sh` — headless Chrome → PDF
- `output/pilot.pdf` — rendered pilot
- `docs/superpowers/specs/2026-04-18-salam-baku-menu-design.md` — design spec

## Render

```bash
./render.sh  # → output/pilot.pdf
```

Requires macOS + Chrome. Renders A4 portrait, 0 margin, print-ready.

## Design brief (reference)

- **Brand color:** forest green (`#1F3D32`) — from original menu
- **Accent:** thin pink/magenta rule at top/bottom
- **Background:** textured white kraft paper
- **Typography:** Didone-style display serif (italic/bold) + bold sans body (uppercase, wide tracking)
- **Layout:** large food photography (half/full-bleed) + 2-col item list
- **Mood:** modern botanical / high-end casual

Current pilot uses cream + burgundy + gold (Elegance theme) — to be refactored toward the green/white/pink DNA of the original printed menu.

## Stack direction (planned)

- Paged.js for @page, bleed, running heads
- Theme variables inspired by electricbookworks/paged-design
- Preserve Cyrillic support (PT Serif / Playfair Display / custom Didone)
