# Mindbuilddaily Agent — Starter Kit

This repo gives you a minimal, working foundation to **auto-generate 3 vertical images every day (1080×1920)** with text in **League Spartan (Header, size ~50)**, plus captions and hashtags. It uses:
- **OpenAI API** (for quotes/captions/hashtags)
- **Pillow** (to render text onto the image)
- Optional: **GitHub Actions** to run daily and save outputs as build artifacts

> TikTok auto-posting is intentionally not included here (TikTok’s API access is limited). The simplest approach is: generate images daily, then post manually or via a social scheduling tool that supports uploads.

---

## Quick Start (local)
1. **Install Python 3.10+** and create a venv:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Set env vars** (copy `.env` from `config.example.env` and fill your keys):
   ```bash
   cp config.example.env .env
   # edit .env to add OPENAI_API_KEY etc.
   ```

3. **Add the font** (League Spartan):
   - Put `LeagueSpartan-Bold.ttf` in `fonts/`
   - If missing, the script will fall back to a default system font.

4. **Run the generator**:
   ```bash
   python generate.py
   ```
   Output goes to `output/YYYY-MM-DD/` with 3 images + `captions.json`.

---

## How it works
- `generate.py` asks GPT for 3 short “Mindbuilddaily” statements (concise, motivational, not cringe), plus 3 captions and hashtags.
- It then renders each statement onto a clean 1080×1920 background (templates from `templates/theme.json`), with plenty of padding and sensible line breaks. Font is **League Spartan** size 50 by default.
- Filenames: `mindbuilddaily_1.png`, `mindbuilddaily_2.png`, `mindbuilddaily_3.png`.

### Consistent Style
The text style and layout are set in `prompts/style.md` and `templates/theme.json`. Adjust margins, font size, or background variants to match your brand.

---

## Scheduling options

### A) macOS/Linux cron (local machine/server)
Edit crontab:
```
0 20 * * * cd /path/to/mindbuilddaily-agent-starter && /path/to/python generate.py >> cron.log 2>&1
```
Runs **every day at 20:00** (Europe/Stockholm).

### B) GitHub Actions (free, easy)
- Commit this folder to a new GitHub repo.
- Add a repository secret **OPENAI_API_KEY** (Settings → Secrets → Actions).
- Enable the included workflow in `.github/workflows/daily.yml`.
- Each day, the workflow uploads images and `captions.json` as build artifacts you can download.

> If you want Google Drive/Dropbox delivery or Telegram, extend `generate.py` with those SDKs later.

---

## Safety & Brand Notes
- Keep copy **short, punchy, practical**. Avoid medical/financial claims.
- Always review outputs before posting.
- If you later want auto-posting, use a scheduler that supports TikTok uploads or export to Instagram Reels/YouTube Shorts where APIs are simpler.

---

## Troubleshooting
- **Font not found**: place `fonts/LeagueSpartan-Bold.ttf` or change `FONT_PATH` in `.env`.
- **Text wraps badly**: tweak `MAX_CHARS_PER_LINE`, `LINE_SPACING`, or margins in the code.
- **Swedish vs English**: set `LANG=sv` or `LANG=en` in `.env`.
- **Too verbose/cheesy**: adjust the system prompt in `prompts/style.md`.

---

© You. Use freely for Mindbuilddaily.
