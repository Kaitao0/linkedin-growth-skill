# LinkedIn Growth Skill

[🇺🇸 English](README.md) | 🇧🇷 **Português**

Uma [Claude Skill](https://www.anthropic.com/news/skills) que transforma o Claude num estrategista sênior de marca pessoal pro LinkedIn. Avalia seu perfil seção por seção, reescreve cada uma com tom humanizado e profissional, gera um calendário editorial mensal adaptado ao seu nicho e produz posts prontos pra publicar — texto + imagem PNG ou carrossel.

Você publica manualmente. A skill não posta por você. A Fase 2 opcional integra com seu próprio n8n pra agendamento, se quiser.

---

## O que ela faz

- **Auditoria** do seu perfil em 10 seções (foto, banner, headline, sobre, destaques, experiência, competências, recomendações, atividade, perfil bilíngue) com nota 0–100 por seção.
- **Reescreve** cada seção fraca com tom que soa autoral — escrito por um profissional real, não por IA.
- **Gera** um calendário editorial mensal adaptado ao seu nicho, com frequência, mix de tipos de conteúdo e melhores horários de publicação.
- **Produz** posts prontos: copy + imagem PNG (ou carrossel completo), com gancho, corpo, CTA reflexivo e hashtags.
- **Orienta** na configuração bilíngue (PT/EN) dentro do mesmo perfil quando faz sentido.
- **Itera** baseado nas métricas reais que você reporta de volta.

---

## Requisitos

- Conta no [Claude.ai](https://claude.ai) (gratuito funciona, Pro recomendado pelos Projetos), **ou** [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) instalado localmente.
- Opcional: `GEMINI_API_KEY` do [Google AI Studio](https://aistudio.google.com/apikey) pra gerar imagens via Gemini 2.5 Flash Image (Nano Banana). Sem a chave, a skill cai num gerador baseado em templates Pillow.
- Python 3.10+ se quiser rodar os scripts auxiliares localmente.

---

## Instalação

### Opção A — Claude.ai (web/app)

1. Baixe ou clone esse repositório.
2. Compacte a pasta `linkedin-growth-skill/` inteira em zip.
3. No Claude.ai: `Configurações → Recursos → Skills → Carregar skill` e selecione o zip.
4. Crie um novo Projeto, configure as instruções como `"Use a linkedin-growth-skill em tudo desse projeto."`, e abra um chat com `"Faz uma auditoria do meu perfil do LinkedIn."`

### Opção B — Claude Code (local)

```bash
git clone https://github.com/<seu-usuario>/linkedin-growth-skill.git ~/.claude/skills/linkedin-growth-skill
```

Pronto — em qualquer sessão do Claude Code a skill ativa automaticamente quando o gatilho for detectado.

Passo-a-passo completo (incluindo como publicar seu próprio fork) tá em [INSTALL.md](INSTALL.md).

---

## Como usar

1. Crie um Projeto no Claude com o nome da sua marca pessoal.
2. Suba pra ele:
   - Um PDF do seu perfil atual do LinkedIn (`Mais → Salvar em PDF` no LinkedIn).
   - Sua foto de perfil atual como imagem separada.
   - 3–10 perfis de referência que você admira (URLs ou prints).
   - 3–10 posts que você considera bons exemplos.
3. Abra um chat no projeto e mande `"Faz auditoria do meu perfil."`
4. A skill vai rodar 10 passos da primeira execução:
   - Detectar ou criar a estrutura do projeto
   - Parsear seu perfil
   - Confirmar nicho, público e idioma
   - Pontuar todas as seções
   - Reescrever as seções fracas
   - Analisar sua foto de perfil
   - Configurar estratégia bilíngue
   - Montar o calendário do mês
   - Gerar os 4 primeiros posts (copy + imagens)
   - Configurar o loop de feedback
5. Depois de publicar, manda as métricas de volta e a skill adapta a próxima leva.

---

## Estrutura do projeto

```
linkedin-growth-skill/
├── SKILL.md                          # Definição principal da skill
├── README.md                         # Versão inglês
├── README.pt-BR.md                   # Esse arquivo
├── INSTALL.md                        # Guia detalhado de instalação + publicação
├── LICENSE                           # MIT
├── .gitignore
├── .env.example
├── scripts/
│   ├── parse_linkedin_pdf.py
│   ├── analyze_profile_image.py
│   ├── generate_image_nano.py        # Gemini Nano Banana
│   ├── generate_image_pillow.py      # Fallback
│   ├── humanize_text.py              # Auditor anti-IA
│   └── post_to_n8n.py                # Fase 2 opcional
├── rules/
│   ├── scoring_rubric.md
│   ├── humanization_rules.md
│   ├── content_strategy.md
│   ├── posting_schedule.md
│   └── bilingual_strategy.md
├── templates/
│   ├── projeto_claude/               # Estrutura inicial do Projeto Claude
│   └── post_templates/               # Templates visuais
└── examples/
    └── example_run.md                # Exemplo de uso ponta-a-ponta
```

---

## Privacidade e segurança

- Os dados do seu perfil ficam só no seu Projeto Claude. Nada vai pra serviço externo a menos que você opte (Gemini pra imagens, n8n pra agendamento).
- Chaves de API vão no `.env` (já no `.gitignore`). Nunca comite.
- A skill nunca automatiza postagem no LinkedIn diretamente. Publicação manual mantém sua conta segura da detecção de automação do LinkedIn.
- Fotos editadas por IA precisam respeitar as expectativas de autenticidade do LinkedIn. Trocar fundo, ajustar luz: ok. Alterar rosto: não.

---

## Limitações

- LinkedIn não oferece API pública pra perfis pessoais. A skill não consegue scrapeartar, logar nem postar por você dentro do Claude.
- As regras de "humanização" reduzem sinais de IA mas nenhum sistema garante detecção zero. O objetivo real é escrita que *soa humana pra leitores reais*, não burlar detector específico.
- Os horários padrão de melhor postagem são calibrados pra Brasil. Ajuste pro seu público após o primeiro mês de dados.

---

## Contribuir

PRs bem-vindos. Se enviar uma calibração nova de nicho (frequência + horários), inclua a metodologia que usou.

---

## Licença

[MIT](LICENSE) © 2026

---

## Créditos

Feito pela comunidade Claude. Inspirado por todo mundo que já ouviu que sua seção "Sobre" do LinkedIn tava "ok" quando não tava.
