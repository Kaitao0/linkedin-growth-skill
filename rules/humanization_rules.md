# Humanization Rules

The single most important file in this skill. Generated text that reads as AI defeats the entire purpose. Every output goes through these rules before being shown to the user.

---

## Hard bans — never use these

### Words and phrases
- "delve", "delves", "delving"
- "in today's fast-paced world" / "no mundo acelerado de hoje"
- "in the realm of" / "no universo de"
- "navigating the complexities" / "navegando pelas complexidades"
- "it's not just X, it's Y" pattern
- "more than just" / "mais do que apenas"
- "leverage" as verb (use "use", "aplicar", "aproveitar")
- "unlock" used metaphorically ("unlock potential")
- "harness" used metaphorically
- "tapestry", "rica tapeçaria"
- "elevate" used metaphorically ("elevate your career")
- "game-changer", "divisor de águas" (overused)
- "revolutionize" / "revolucionar" (used loosely)
- "in conclusion", "em conclusão", "para concluir"
- "I hope this helps" / "espero que isso ajude"
- "feel free to" / "fique à vontade para"
- "remember", "lembre-se" as a paragraph opener
- "passionate about" / "apaixonado por" (without specific object)
- "results-driven", "orientado a resultados" (cliché)
- "synergy", "sinergia" (corporate filler)
- "ecosystem", "ecossistema" (when not technically accurate)

### Punctuation and structure
- Em-dash overuse. Use at most one em-dash per ~300 words. Prefer commas, parentheses, or new sentences.
- Parallel bullet lists where every bullet starts with the same word class (verb-verb-verb-verb). Vary structure.
- Three-item lists everywhere ("X, Y, and Z"). Use 2, 4, or 5 sometimes.
- Perfectly balanced sentences. Real writing has rhythm variation: short. Then a longer one with a clause. Then medium.
- Excessive headers and bold. Real LinkedIn posts have minimal formatting.

---

## Active practices — apply these

### Sentence rhythm
Mix sentence lengths deliberately. Pattern to aim for:
- Short. (3–6 words)
- Medium with a subordinate clause that adds nuance. (10–18 words)
- Longer flowing sentence that builds an idea, then turns, then lands somewhere unexpected. (20–30 words)
- Short again.

### Voice markers (Portuguese)
- Use contractions natural to spoken Portuguese: "tá", "pra", "tô" (only in informal posts, never in About/Headline).
- Drop subject pronouns when natural ("Comecei na área em..." instead of "Eu comecei na área em...").
- Use "a gente" instead of "nós" when the tone is informal.
- Real BR idioms: "rodar", "esbarrar com", "dar liga", "encaixar", "soltar a real", "topa?", "rolou".
- Avoid Portuguese that sounds translated from English ("ao final do dia" for "at the end of the day").

### Voice markers (English)
- Use light contractions: "I'm", "we're", "it's", "there's".
- Start sentences with "And", "But", "So" occasionally.
- Use sentence fragments for emphasis. Sometimes.
- Specific verbs over generic ones: "shipped", "rebuilt", "gutted", "bolted on" — not "implemented", "developed", "utilized".

### Specificity over abstraction
Replace abstract claims with concrete details:
- ❌ "I led a digital transformation initiative."
- ✅ "Trocamos um ERP de 18 anos por uma stack nova em 8 meses, com a operação rodando o tempo todo."

If the user hasn't given concrete numbers/details, **ask** — never invent.

### Micro-imperfections (controlled)
Real writing has slight roughness. Allow:
- One starting "Mas" or "E" per post.
- One sentence that trails into a question.
- One parenthetical aside.
- Occasional one-word paragraph for emphasis.

Do **not** allow:
- Typos.
- Grammar errors.
- Inconsistent tense.

### Niche jargon
Use the user's actual niche vocabulary. Examples:
- ERP/retail: "PDV", "frente de caixa", "fiscal", "homologação", "rollout".
- Backend: "p99", "throughput", "circuit breaker", "idempotência".
- Marketing: "funil", "ICP", "ARR", "churn".

If you don't know the niche jargon, ask the user for 5–10 terms they use daily.

### First-person ownership
- Use "eu" / "I" sparingly but clearly. Posts written entirely in third person feel corporate-distant.
- Show stakes: what was at risk, what you felt, what you learned.
- Be willing to say "I was wrong about X" — vulnerability outperforms polish on LinkedIn.

---

## Validation checklist (run mentally before showing output)

Before delivering any rewritten section or post, check:

- [ ] Zero hard-banned words/phrases.
- [ ] At most one em-dash per 300 words.
- [ ] Sentence lengths vary across the piece.
- [ ] At least one concrete detail (number, name, date, place) per ~100 words.
- [ ] No three consecutive sentences with the same opening word class.
- [ ] No "perfect" parallel bullet lists unless deliberately for impact.
- [ ] Sounds like a human in the user's actual voice when read aloud.
- [ ] If translated to the other language, would still keep the same energy.

If any check fails, rewrite. Then run `scripts/humanize_text.py` (if available) to flag remaining patterns.

---

## What "humanized" does NOT mean

- It does not mean unprofessional. The tone is corporate, respectful, calibrated to recruiters and decision-makers.
- It does not mean casual everywhere. The About section is more formal than a post about a Friday lesson learned.
- It does not mean shocking or controversial. Engagement-bait ("Unpopular opinion: 🚨") cheapens the brand.
- It does not mean pretending the user is someone they're not. Match their actual seniority and personality.

---

## Note on AI detectors

No AI detector is reliable. Tools like GPTZero, Originality.ai, ZeroGPT have false positive rates above 20% on human writing and miss humanized AI text routinely. The goal of these rules is not to "beat detectors" — it is to produce writing that real readers (recruiters, peers, clients) experience as authored by a competent human professional. That is the only metric that matters.
