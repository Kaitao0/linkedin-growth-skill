# Posting Schedule

Frequency and timing depend on niche, audience timezone, and content type. Defaults below — adjust based on the user's actual engagement data after the first month.

---

## Frequency by niche

| Niche cluster | Posts per week | Notes |
|---|---|---|
| Tech leadership, B2B sales, consulting | 2–3 | Audience is active, expects regular signal |
| Engineering / backend / data | 1–2 | Audience reads more than posts; quality over quantity |
| Creative (design, marketing) | 3–5 | Visual-heavy, faster cadence acceptable |
| Executive / C-level | 1 | Each post must carry weight |
| Job-seeking active phase | 3–4 | Maximize visibility window |
| Founders / personal brand | 3–5 | Brand is the product |

Default to the lower bound and ramp up only if the audience responds.

---

## Best times to post (Brazil)

Based on aggregate LinkedIn engagement patterns for BR audience. These are starting hypotheses — recalibrate per user after 30 days of data.

| Day | Best windows (BRT) | Content type fit |
|---|---|---|
| Monday | 08:00–10:00 | Authority, week-opener insights |
| Tuesday | 08:00–10:00, 12:00–13:00 | Highest overall reach. Best for flagship posts. |
| Wednesday | 08:00–10:00, 17:00–18:00 | Stories, vulnerability posts |
| Thursday | 08:00–10:00 | Second-best reach. Carousels work well. |
| Friday | 08:00–11:00 | Lighter content, behind-the-scenes |
| Saturday | avoid | Engagement <40% of weekday baseline |
| Sunday | 18:00–20:00 (light only) | Reflective posts only |

---

## Best times by content type

- **Authority / technical**: weekday mornings (08:00–10:00). Decision-makers scroll while drinking coffee.
- **Story / vulnerability**: late afternoon (17:00–19:00). End-of-workday reflection mode.
- **Opinion / debate**: Tuesday or Thursday morning. Maximum dwell time for comments.
- **Carousel**: Tuesday/Thursday morning. People save them for later.
- **Behind-the-scenes**: Friday morning. Lower stakes, conversational.
- **Polls**: Wednesday morning. Mid-week engagement peak.

---

## International timezone handling

If the user posts EN content for international recruiters:

| Target market | Best window (UTC) | BRT equivalent |
|---|---|---|
| US East Coast | 13:00–15:00 UTC | 10:00–12:00 BRT |
| US West Coast | 16:00–18:00 UTC | 13:00–15:00 BRT |
| Europe (DE/UK/FR) | 08:00–10:00 UTC | 05:00–07:00 BRT (schedule the night before) |
| Global (mixed) | 13:00 UTC | 10:00 BRT — best compromise |

---

## Calendar template (monthly)

Output the calendar as a table with these columns:

| Date | Day | Time (BRT) | Lang | Type | Topic | Hook draft | Status |
|---|---|---|---|---|---|---|---|
| 2026-04-21 | Tue | 09:00 | PT | Authority | Migração de ERP em retail | "Em 47 dias refizemos..." | draft |
| 2026-04-23 | Thu | 09:00 | EN | Carousel | n8n vs cron jobs | "Why we ditched cron..." | draft |
| 2026-04-25 | Sat | — | — | — | — | — | rest day |

Save to `calendario_editorial.md` in the user's project. Update it weekly based on engagement data reported back.

---

## Adapting the calendar

After every 4 published posts, look at:

- Which post had the highest engagement rate (likes + comments + reposts) ÷ impressions.
- Which post had the most comment depth (replies, not just one-liners).
- Which post drove the most profile visits.
- Which post hooks underperformed (people saw the first line and scrolled past).

Then:
- Double down on the format that performed best for the next batch.
- Drop the format that consistently underperforms.
- Move publication time slightly (±1h) to test if timing helps.

Never change more than two variables at once or you can't tell what worked.

---

## When to break the schedule

Post off-schedule when:

- A genuine industry event happens that the user has expertise on (within 24h).
- The user has a real launch, anniversary, or milestone.
- A previous post is going viral — post a follow-up within 48h to capture the audience.

Do **not** post off-schedule when:

- The user feels FOMO from someone else's post.
- A trending topic has nothing to do with the user's niche.
- The post would violate the content rules in `content_strategy.md`.
