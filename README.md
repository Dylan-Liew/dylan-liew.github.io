# Dylan Liew

Personal cybersecurity portfolio built with MkDocs Material.

The main repo owns the site shell, theme, navigation, sync script, and GitHub Pages deployment. Each content category lives in its own repository.

## Architecture

```text
dylan-liew.github.io/
  docs/                 # MkDocs site shell and generated content targets
  scripts/sync_content.py
  mkdocs.yml
  requirements.txt
  .github/workflows/pages.yml

../gyms/
  docs/                 # Certification notes and journeys

../labs/
  docs/                 # Lab notes and writeups

../blogs/
  docs/                 # Blog entries

../projects/
  docs/                 # Project entries
```

During CI, GitHub Actions checks out all repos, copies selected Markdown into `docs/`, builds the site, and deploys to GitHub Pages. This avoids git submodules.

## Local Setup

```bash
cd /mnt/c/Users/Dylan/Documents/GitHub/dylan-liew.github.io
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/sync_content.py --content-root ..
mkdocs serve
```

Open <http://127.0.0.1:8000/>.

## Build

```bash
python scripts/sync_content.py --content-root ..
mkdocs build --strict
```

Generated external content paths are ignored by git:

- `docs/gyms/`
- `docs/labs/`
- `docs/blogs/`
- `docs/projects/`

## Deployment

The workflow in `.github/workflows/pages.yml` deploys to GitHub Pages on pushes to `main`.

Before first deployment, set GitHub Pages source to **GitHub Actions**:

1. Open the repository on GitHub.
2. Go to **Settings -> Pages**.
3. Set **Build and deployment -> Source** to **GitHub Actions**.

## Plugins

Included now:

- `mkdocs-glightbox` for clean image previews.
- `mkdocs-minify-plugin` for smaller output.
- Material social cards in CI.

Worth considering later:

- `mkdocs-redirects` if old GitBook or portfolio URLs need redirects.
- `mkdocs-macros-plugin` for reusable note blocks.
- `mkdocs-git-authors-plugin` if multiple contributors appear.
- `mkdocs-awesome-nav` if maintaining the growing certification navigation manually becomes annoying.
