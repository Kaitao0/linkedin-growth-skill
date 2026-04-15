# Claude Project Structure — LinkedIn Growth

This is the recommended folder structure for a Claude Project that uses the `linkedin-growth-skill`.

```
my-linkedin-growth/
├── perfil_atual.md           # Snapshot of current LinkedIn profile
├── perfil_otimizado.md       # Rewritten sections (PT and EN)
├── nicho_e_publico.md        # Niche, audience, keywords, reference profiles
├── calendario_editorial.md   # Monthly editorial calendar
├── referencias/              # Reference profiles & posts the user admires
│   ├── perfis/
│   └── posts/
├── historico_posts/          # All generated posts + their metrics
│   └── 2026-04-21_migracao-erp/
│       ├── copy.md           # Final post copy
│       ├── image.png         # Or slide_01.png ... slide_N.png
│       └── meta.json         # Type, lang, hashtags, scheduled time, metrics
└── assets/                   # Profile photo, banner, brand colors
    ├── current_photo.jpg
    ├── optimized_photo.png
    ├── banner.png
    └── brand_colors.json
```

## Setup steps for the user

1. Create a new Claude Project named after your personal brand.
2. Upload to it: a PDF of your current LinkedIn profile (use LinkedIn's `More → Save to PDF`), your current profile photo as a separate image, and 3–10 reference profiles/posts you admire.
3. In the project's instructions, paste:

   > "Use the linkedin-growth-skill for everything in this project. Always read the project files at the start of every session before responding."

4. Start a chat in the project and say "Audit my profile" to begin the first run.

The skill will populate all the markdown files automatically based on what you provide.
