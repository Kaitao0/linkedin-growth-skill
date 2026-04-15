# LinkedIn Growth Skill

🇺🇸 **English** | [🇧🇷 Português](README.pt-BR.md)

A [Claude Skill](https://www.anthropic.com/news/skills) that turns Claude into a senior personal-branding strategist for LinkedIn. It scores your profile section by section, rewrites every section in humanized professional tone, generates a monthly editorial calendar adapted to your niche, and produces ready-to-publish copy and PNG/carousel images.

You publish manually. The skill does not post for you. Optional Phase 2 hooks into your own n8n instance for scheduled posting if you want it.

---

## What it does

- **Audits** your profile against a 10-section rubric (photo, banner, headline, About, featured, experience, skills, recommendations, activity, bilingual setup) and gives you a score 0–100 per section.
- **Rewrites** every weak section in a tone that reads as authored by a real human professional — not by AI.
- **Generates** a monthly editorial calendar adapted to your niche, with post frequency, content type mix, and best publishing times.
- **Produces** ready-to-publish posts: copy + PNG image (or full carousel), with hook, body, reflective CTA, and hashtags.
- **Coaches** you through bilingual setup (PT/EN) within the same LinkedIn profile when relevant.
- **Iterates** based on real engagement metrics you report back over time.

---

## Requirements

- A [Claude.ai](https://claude.ai) account (free works, Pro recommended for Projects), **or** [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) installed locally.
- Optional: a `GEMINI_API_KEY` from [Google AI Studio](https://aistudio.google.com/apikey) to generate images via Gemini 2.5 Flash Image (Nano Banana). Without the key, the skill falls back to a Pillow-based template generator.
- Python 3.10+ if you want to run the helper scripts locally.

---

## Install

### Option A — Claude.ai (web/app)

1. Download or clone this repository.
2. Zip the entire `linkedin-growth-skill/` folder.
3. In Claude.ai: `Settings → Capabilities → Skills → Upload skill` and select the zip.
4. Create a new Project, set its instructions to `"Use the linkedin-growth-skill for everything in this project."`, and start a chat with `"Audit my LinkedIn profile."`

### Option B — Claude Code (local)

```bash
git clone https://github.com/<your-username>/linkedin-growth-skill.git ~/.claude/skills/linkedin-growth-skill
```

Then in any Claude Code session, the skill auto-loads when triggered.

Full step-by-step (including how to publish your own fork) is in [INSTALL.md](INSTALL.md).

---

## How to use

1. Create a Claude Project named after your personal brand.
2. Upload to it:
   - A PDF of your current LinkedIn profile (`More → Save to PDF` on LinkedIn).
   - Your current profile photo as a separate image.
   - 3–10 reference profiles you admire (URLs or screenshots).
   - 3–10 example posts you consider high-quality.
3. Open a chat in the project and say `"Audit my profile."`
4. The skill will run a 10-step first-run flow:
   - Detect or create the project structure
   - Parse your profile
   - Confirm your niche, audience, and language
   - Score every section
   - Rewrite weak sections
   - Analyze your profile photo
   - Set up bilingual strategy
   - Build the monthly calendar
   - Generate the first 4 posts (copy + images)
   - Set up the feedback loop
5. After publishing, send back the post analytics and the skill adapts the next batch.

---

## Project structure

```
linkedin-growth-skill/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file
├── README.pt-BR.md                   # Portuguese version
├── INSTALL.md                        # Detailed install + GitHub publish guide
├── LICENSE                           # MIT
├── .gitignore
├── .env.example
├── scripts/
│   ├── parse_linkedin_pdf.py
│   ├── analyze_profile_image.py
│   ├── generate_image_nano.py        # Gemini Nano Banana
│   ├── generate_image_pillow.py      # Fallback
│   ├── humanize_text.py              # AI-pattern auditor
│   └── post_to_n8n.py                # Optional Phase 2
├── rules/
│   ├── scoring_rubric.md
│   ├── humanization_rules.md
│   ├── content_strategy.md
│   ├── posting_schedule.md
│   └── bilingual_strategy.md
├── templates/
│   ├── projeto_claude/               # Initial Claude Project structure
│   └── post_templates/               # Visual templates
└── examples/
    └── example_run.md                # End-to-end usage example
```

---

## Privacy & safety

- Your profile data lives only in your Claude Project. Nothing is sent to any external service unless you opt in (Gemini for image generation, n8n for scheduled posting).
- API keys go in `.env` (already in `.gitignore`). Never commit them.
- This skill never automates posting on LinkedIn directly. Manual publishing keeps your account safe from LinkedIn's automation detection.
- AI-edited profile photos must respect LinkedIn's authenticity expectations. Background swaps and lighting fixes: fine. Face alterations: don't.

---

## Limitations

- LinkedIn does not provide a public API for personal profiles. The skill cannot scrape, log in, or post on your behalf within Claude itself.
- The "humanization" rules reduce AI-detection signals but no system can guarantee zero detection. The real goal is writing that *sounds human to readers*, not gaming any specific detector.
- Best-time-to-post defaults are calibrated for Brazil. Calibrate to your audience after the first month of data.

---

## Contributing

PRs welcome. If you ship a new niche calibration (frequency + best times), please include the methodology you used.

---

## License

[MIT](LICENSE) © 2026

---

## Credits

Built by the Claude community. Inspired by everyone who's been told their LinkedIn About section is "fine" when it's not.
