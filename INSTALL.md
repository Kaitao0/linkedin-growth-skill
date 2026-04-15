# Install & Publish Guide

🇺🇸 English | 🇧🇷 Português below

---

## 🇺🇸 English

### Part 1 — Publish this skill to your own GitHub

If you already have Git installed, skip to step 4.

#### 1. Install Git

- **Windows**: download from [git-scm.com](https://git-scm.com/download/win) and run the installer.
- **macOS**: open Terminal and run `xcode-select --install`.
- **Linux**: `sudo apt install git` (Debian/Ubuntu) or `sudo dnf install git` (Fedora).

Verify: `git --version`

#### 2. Create a GitHub account

Go to [github.com](https://github.com) and sign up if you don't have one.

#### 3. Configure Git locally

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

#### 4. Create the repository on GitHub

1. Click `+` → `New repository` at the top right.
2. Name: `linkedin-growth-skill`
3. Description: `A Claude Skill that audits and grows LinkedIn profiles end-to-end.`
4. Visibility: **Public** (so the community can use it).
5. Do **not** initialize with README, .gitignore, or license — we'll push our own.
6. Click `Create repository`.

#### 5. Push your local copy

In your terminal, navigate to the folder containing `linkedin-growth-skill/`:

```bash
cd path/to/linkedin-growth-skill
git init
git add .
git commit -m "Initial release of linkedin-growth-skill"
git branch -M main
git remote add origin https://github.com/<your-username>/linkedin-growth-skill.git
git push -u origin main
```

If GitHub asks for authentication, use a [Personal Access Token](https://github.com/settings/tokens) (Settings → Developer settings → Personal access tokens → Generate new token, classic, with `repo` scope) as the password.

#### 6. Add a topic for discoverability

On the repo page on GitHub, click the gear icon next to "About" and add topics:
`claude-skill`, `linkedin`, `personal-branding`, `ai-skill`, `claude-ai`

---

### Part 2 — Install the skill in Claude

#### Option A — Claude.ai (web/app) — easiest

Skills on Claude.ai are uploaded as `.zip` files.

1. From your local clone, zip the entire `linkedin-growth-skill/` folder.
   ```bash
   cd path/to/linkedin-growth-skill/..
   zip -r linkedin-growth-skill.zip linkedin-growth-skill/
   ```
   On Windows, right-click the folder → Send to → Compressed (zipped) folder.

2. Open Claude.ai → click your profile → **Settings** → **Capabilities** → **Skills**.

3. Click **Upload skill** and select the zip file.

4. Wait for "Installed". The skill is now available across your account.

5. Create a new Project named after your personal brand. In the project's **Instructions** field, paste:
   > Use the linkedin-growth-skill for everything in this project. Always read all project files at the start of every session before responding.

6. Upload to the project: your LinkedIn PDF, your current profile photo, and any reference profiles/posts.

7. Open a chat in the project and say:
   > Audit my LinkedIn profile.

#### Option B — Claude Code (local CLI)

If you use Claude Code, skills live in `~/.claude/skills/`.

```bash
# Clone directly into the skills folder
mkdir -p ~/.claude/skills
git clone https://github.com/<your-username>/linkedin-growth-skill.git ~/.claude/skills/linkedin-growth-skill
```

The skill auto-loads in any Claude Code session when its trigger words appear.

To use the helper scripts (PDF parsing, image generation), install Python dependencies:

```bash
cd ~/.claude/skills/linkedin-growth-skill
python -m pip install -r scripts/requirements.txt
```

If you want to use Gemini for image generation, copy `.env.example` to `.env` and fill your key:

```bash
cp .env.example .env
# Edit .env and paste your GEMINI_API_KEY
```

---

### Part 3 — Update the skill later

When you change anything in the skill (or pull updates from upstream):

```bash
cd path/to/linkedin-growth-skill
git pull              # if pulling from upstream
git add .
git commit -m "Describe what changed"
git push
```

For Claude.ai users: re-zip and re-upload via Settings → Skills (delete the old version first).
For Claude Code users: just `git pull` — the skill reloads automatically next session.

---

## 🇧🇷 Português

### Parte 1 — Publicar a skill no seu GitHub

Se já tem Git instalado, pule pro passo 4.

#### 1. Instalar Git

- **Windows**: baixe em [git-scm.com](https://git-scm.com/download/win) e execute o instalador.
- **macOS**: abra o Terminal e rode `xcode-select --install`.
- **Linux**: `sudo apt install git` (Debian/Ubuntu) ou `sudo dnf install git` (Fedora).

Confirme: `git --version`

#### 2. Criar conta no GitHub

Vá em [github.com](https://github.com) e cadastre-se se ainda não tem.

#### 3. Configurar Git localmente

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

#### 4. Criar o repositório no GitHub

1. Clique em `+` → `New repository` no canto superior direito.
2. Nome: `linkedin-growth-skill`
3. Descrição: `Uma Claude Skill que audita e cresce perfis do LinkedIn de ponta a ponta.`
4. Visibilidade: **Public** (pra comunidade poder usar).
5. **Não** inicialize com README, .gitignore nem licença — vamos enviar a nossa.
6. Clique em `Create repository`.

#### 5. Subir sua cópia local

No terminal, navegue até a pasta que contém `linkedin-growth-skill/`:

```bash
cd caminho/para/linkedin-growth-skill
git init
git add .
git commit -m "Initial release of linkedin-growth-skill"
git branch -M main
git remote add origin https://github.com/<seu-usuario>/linkedin-growth-skill.git
git push -u origin main
```

Se o GitHub pedir autenticação, use um [Personal Access Token](https://github.com/settings/tokens) (Settings → Developer settings → Personal access tokens → Generate new token, classic, com escopo `repo`) como senha.

#### 6. Adicionar topics pra descoberta

Na página do repo no GitHub, clique na engrenagem ao lado de "About" e adicione topics:
`claude-skill`, `linkedin`, `personal-branding`, `ai-skill`, `claude-ai`

---

### Parte 2 — Instalar a skill no Claude

#### Opção A — Claude.ai (web/app) — mais fácil

Skills no Claude.ai são carregadas como arquivos `.zip`.

1. Da sua cópia local, compacte a pasta `linkedin-growth-skill/` inteira.
   ```bash
   cd caminho/para/linkedin-growth-skill/..
   zip -r linkedin-growth-skill.zip linkedin-growth-skill/
   ```
   No Windows, clique direito na pasta → Enviar para → Pasta compactada.

2. Abra Claude.ai → clique no seu perfil → **Configurações** → **Recursos** → **Skills**.

3. Clique em **Carregar skill** e selecione o zip.

4. Aguarde "Instalado". A skill agora tá disponível na sua conta.

5. Crie um novo Projeto com o nome da sua marca pessoal. No campo **Instruções** do projeto, cole:
   > Use a linkedin-growth-skill em tudo desse projeto. Sempre leia todos os arquivos do projeto no início de cada sessão antes de responder.

6. Suba pro projeto: seu PDF do LinkedIn, sua foto atual e quaisquer perfis/posts de referência.

7. Abra um chat no projeto e mande:
   > Faz auditoria do meu perfil do LinkedIn.

#### Opção B — Claude Code (CLI local)

Se você usa Claude Code, skills ficam em `~/.claude/skills/`.

```bash
# Clone direto na pasta de skills
mkdir -p ~/.claude/skills
git clone https://github.com/<seu-usuario>/linkedin-growth-skill.git ~/.claude/skills/linkedin-growth-skill
```

A skill ativa sozinha em qualquer sessão do Claude Code quando o gatilho aparece.

Pra usar os scripts auxiliares (parsing de PDF, geração de imagem), instale as dependências Python:

```bash
cd ~/.claude/skills/linkedin-growth-skill
python -m pip install -r scripts/requirements.txt
```

Se quiser usar o Gemini pra geração de imagem, copie `.env.example` pra `.env` e preencha sua chave:

```bash
cp .env.example .env
# Edite .env e cole sua GEMINI_API_KEY
```

---

### Parte 3 — Atualizar a skill depois

Quando mudar qualquer coisa na skill (ou pull de updates do upstream):

```bash
cd caminho/para/linkedin-growth-skill
git pull              # se pegar updates do upstream
git add .
git commit -m "Descreva o que mudou"
git push
```

Pra usuários do Claude.ai: zipe de novo e suba via Configurações → Skills (delete a versão antiga primeiro).
Pra usuários do Claude Code: só `git pull` — a skill recarrega sozinha na próxima sessão.
