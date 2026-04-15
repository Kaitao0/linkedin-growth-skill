# Content Strategy

How every post is built. Apply alongside `humanization_rules.md`.

---

## Post anatomy

Every post follows this structure unless the user requests otherwise:

```
[HOOK — line 1, max 12 words, must trigger "see more"]
[blank line]
[CONTEXT — 1–3 short lines that set up the story or claim]
[blank line]
[BODY — the substance, broken into chunks of 1–3 lines with blank lines between]
[blank line]
[REFLECTION TURN — what changed, what the user learned, the insight]
[blank line]
[REFLECTIVE CTA — one open question to the reader]
[blank line]
[HASHTAGS — 3 to 5, mix of high/medium/niche]
```

Total length: 800–1300 characters for text posts. Carousels can go longer in the slides themselves.

---

## Hook patterns (line 1)

Pick one per post. Rotate across the calendar — never repeat the same pattern twice in a row.

### Pattern 1 — Counterintuitive claim
"Demitir o melhor dev do time foi a melhor decisão do trimestre."

### Pattern 2 — Specific number + stakes
"Em 47 dias, refizemos o ERP de 18 anos. Quase quebrou a operação 3 vezes."

### Pattern 3 — Confession
"Errei feio na primeira migração de PDV. Rolou downtime de 6h em 12 lojas."

### Pattern 4 — Before/after frame
"Antes: 3h pra fechar o caixa. Depois: 11 minutos."

### Pattern 5 — Direct question with stakes
"Você confiaria a integração fiscal de 80 lojas a um workflow no n8n?"

### Pattern 6 — Pattern interrupt
"Ninguém fala disso, mas implementar IA em retail tem um problema legal sério."

### Pattern 7 — Insider observation
"Toda vez que vejo um RH pedindo 'profissional resiliente' eu sei que o time tá pegando fogo."

### Pattern 8 — Micro-story opener
"Sexta, 23h. WhatsApp do diretor: 'o estoque tá negativo em 4 lojas'."

Avoid:
- "Hoje eu quero compartilhar..." (kills the hook).
- "Reflexão do dia:" (cheesy).
- Emoji at the start of line 1 (algorithm penalty in some niches).
- "🚨 ATENÇÃO 🚨" or any all-caps urgency theatre.

---

## Retention techniques (body)

LinkedIn rewards dwell time. Write for the reader to keep scrolling within the post.

### Whitespace
One idea per paragraph. Blank line between every paragraph. Avoid wall-of-text.

### Line breaks before reveals
Set up a question, break a line, then answer. Forces the reader's eye down.

```
A migração quebrou em produção.

Sabe o que era?

Um campo NULL que ninguém tinha mapeado em 2007.
```

### Open loops
Plant a question in line 3, answer it in line 8. The reader stays to close the loop.

### Concrete > abstract
Numbers, names, places, timestamps. "Terça às 14h" > "outro dia à tarde".

### Stop-scroll moments
Every 3–4 lines, a sentence that's noticeably shorter or has a turn.

---

## CTA patterns (the close)

Always reflective, always open-ended, always inviting the reader to think — not to buy.

Pick one per post:

- "E você, faria diferente?"
- "Concorda? Discorda?"
- "Qual foi a sua maior lição parecida com essa?"
- "O que você teria feito no meu lugar?"
- "Já passou por algo assim? Como resolveu?"
- "Qual a sua opinião?"
- "Curioso pra saber o que vocês pensam."
- "Me conta nos comentários."

Avoid:
- "Se gostou, curte e compartilha." (begging for engagement, algorithm dislikes).
- "Marca aquele amigo que..." (low-trust pattern).
- "Link na bio." (LinkedIn doesn't really have a "bio" — wrong platform reflex).

---

## Persuasion techniques (use sparingly, never all at once)

### Scarcity (selective)
Use only when true. Examples:
- "Aceito 3 projetos novos por trimestre. Esse é o último de 2026."
- "Vou abrir 5 vagas de mentoria mês que vem — só pra quem já trabalha com integração ERP."

Never invent scarcity. Audience smells it.

### Authority signals
- Cite specific years of experience with concrete details ("9 anos integrando ERPs em retail, 4 deles em rede com 80+ lojas").
- Drop tool/version names that signal depth ("TOTVS RM com Oracle 19c").
- Reference specific industry problems by name.

### Soft self-promotion
Frame the user as someone who solves a problem the reader has. Never list services like a brochure.

- ✅ "Se você está nesse mesmo dilema, comenta aqui ou me chama no DM. Curto trocar ideia sobre isso."
- ❌ "Ofereço consultoria em integração de sistemas. Solicite um orçamento."

### Social proof
- Mention real (anonymized when needed) cases: "Um cliente de varejo no Centro-Oeste...".
- Reference results, not vanity ("reduziu o fechamento de caixa de 3h para 11min" > "aumentou eficiência em 95%").

### Vulnerability
The single most underused technique. Posts admitting a mistake outperform posts claiming a victory by ~2–3x in engagement on LinkedIn. Plan at least one "what I got wrong" post per month.

---

## Hashtag strategy

3 to 5 per post. Mix:

- **1 broad** (high volume): #LinkedIn, #Tecnologia, #Carreira
- **1–2 medium**: #IntegraçãoDeSistemas, #VarejoTech, #ERP
- **1–2 niche**: #TOTVSRm, #N8nBrasil, #AutomaçãoFiscal

Place at the very end. Lowercase with capitals at word boundaries (#IntegraçãoDeSistemas, not #integraçãodesistemas).

Build a per-user hashtag bank in `nicho_e_publico.md` — rotate so the user isn't always tagging the same five things.

---

## Content type mix (per month)

For a typical 12-posts/month cadence (adjust to niche):

| Type | Count | Why |
|---|---|---|
| Authority (deep technical or industry insight) | 3 | Builds credibility with peers and clients |
| Story (specific case or moment with lesson) | 3 | Drives the highest engagement |
| Vulnerability / lesson learned | 2 | Builds trust, attracts comments |
| Opinion / counterintuitive take | 2 | Drives reach via debate |
| Behind-the-scenes / process | 1 | Humanizes the brand |
| Carousel (visual deep-dive) | 1 | Drives saves and dwell time |

For lower frequency (4 posts/month), pick: 1 authority, 1 story, 1 vulnerability, 1 opinion.

---

## Carousel-specific rules

When the post type is carousel:

- 6–10 slides total.
- Slide 1: hook + promise of what they'll learn.
- Slide 2: the problem or context.
- Slides 3 to N-1: one idea per slide, max 30 words.
- Slide N-1: summary or "the framework".
- Slide N: CTA + the user's name/handle.

Visual rules in `templates/post_templates/`.

---

## What never goes in a post

- Internal company information that wasn't pre-cleared.
- Client names without explicit permission.
- Financial figures of the employer.
- Negative comments about specific competitors or former employers.
- Politics/religion unless that IS the user's niche.
- Anything the user hasn't approved in writing in the chat.
