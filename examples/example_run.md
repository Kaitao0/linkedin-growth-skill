# Example Run — End-to-End Usage

This walks through a typical first session with the skill, so you know what to expect.

---

## Setup (one time)

1. Create a Claude Project: `My LinkedIn Growth`.
2. Project instructions:
   > Use the linkedin-growth-skill for everything in this project. Always read all project files at the start of every session before responding.
3. Upload to the project:
   - `linkedin_profile.pdf` (your `Save to PDF` from LinkedIn)
   - `current_photo.jpg`
   - `references/` folder with screenshots of profiles you admire

---

## First chat

**You:**
> Audit my LinkedIn profile.

**Skill (Claude with skill loaded):**

Reads the project files, parses the PDF, and runs the 10-step flow.

You'll see something like:

```
Profile parsed. Detected 9 sections.

Confirm before I score:
- Niche detected: ERP integration & retail automation in Brazil
- Seniority: Manager level (4 years in current role)
- Primary audience guess: hiring managers + tech peers
- Languages: PT only (EN section empty)

Right or wrong?
```

**You:**
> Right. Add: I'm also interested in international remote roles.

**Skill:**

Updates `nicho_e_publico.md`, then runs scoring.

```
SCORE TABLE
| Section          | Score | Critical issue                                  |
|------------------|-------|-------------------------------------------------|
| Profile photo    | 45    | Sunglasses cover eyes — kills trust signal      |
| Banner           | 10    | Default LinkedIn gray                           |
| Headline         | 38    | Pipe-separated buzzwords, no specific niche     |
| About            | 22    | Section is empty                                |
| Experience       | 60    | Missing measurable results in current role      |
| Skills           | 55    | 18 skills, top 3 not pinned strategically       |
| Recommendations  | 30    | Only 2 received                                 |
| Activity         | 15    | No posts in last 90 days                        |
| Bilingual setup  | 0     | EN section empty (you want international roles) |

OVERALL: 32 / 100

Top 3 to fix first (highest impact):
1. About section (largest gap, highest visibility)
2. Headline (every search hit shows this)
3. Profile photo (blocks recruiter trust)

Want me to start with About?
```

**You:**
> Yes.

**Skill:**

Generates 2–3 About variants with different angles (e.g., authority-first, story-first, results-first), each ready to paste, each ~1500 characters, each following `humanization_rules.md`. Asks you which angle resonates.

---

## A few exchanges later...

**Skill:**

Builds the calendar:

```
APRIL 2026 CALENDAR (8 posts — 6 PT, 2 EN)

| Date     | Day | Time  | Lang | Type           | Topic                          |
|----------|-----|-------|------|----------------|--------------------------------|
| Apr 22   | Tue | 09:00 | PT   | Authority      | Migration of TOTVS RM in 47d   |
| Apr 24   | Thu | 09:00 | EN   | Carousel       | n8n vs cron jobs (5 lessons)   |
| Apr 28   | Mon | 09:00 | PT   | Story          | Friday-night incident in 12 PDVs|
| Apr 30   | Wed | 17:00 | PT   | Vulnerability  | Migration error that cost 6h   |
| ...                                                                       |

Generating the first 4 posts now (copy + images).
```

For each post, you get:
- A folder `historico_posts/2026-04-22_migracao-totvs/`
- `copy.md` with the full post text ready to paste
- `image.png` (or `slide_01.png` ... `slide_05.png` for carousel)
- `meta.json` with type, language, hashtags, scheduled time, empty `metrics` field

---

## After publishing

**You:**
> Posted the migration one. Got 47 likes, 12 comments, 1.4k impressions. Screenshot attached.

**Skill:**

Reads the screenshot, updates `meta.json` for that post:

```json
{
  "metrics": {
    "likes": 47,
    "comments": 12,
    "impressions": 1400,
    "engagement_rate": 0.042,
    "reported_at": "2026-04-23"
  }
}
```

Then comments:

```
That engagement rate (4.2%) is above your niche baseline (~2-3%).
Comments deep, not just emojis — high signal.
Authority + specific number in the hook drove this.

Adjusting next batch:
- Tuesday slot stays at 09:00 (working).
- Adding one more Authority-with-number post.
- Carousel scheduled Thursday — keep as planned.

Ready to generate the next 4?
```

---

## Recurring sessions

Just open the project and say something like:
- `Generate the next 4 posts.`
- `Re-score my profile.`
- `Rewrite my About — I got promoted.`
- `Plan the calendar for May.`

The skill reads all project files first, picks up where it left off.
