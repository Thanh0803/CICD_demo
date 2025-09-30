# CI/CD Python Demo (FastAPI + pytest + GitHub Actions + Docker)

This is a tiny demo showing CI (tests on every push/PR) and CD (container image publish on tags).

## Run locally
```bash
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Visit: http://127.0.0.1:8000/health

## Run tests
```bash
pytest -q
```

## Build & run with Docker
```bash
docker build -t cidemo:local .
docker run -p 8000:8000 cidemo:local
```

## CI
- On every push and pull request:
  - Set up Python, install deps, run `pytest`, and (optionally) build the Docker image.

## CD (container publish)
- When you push a tag like `v1.0.0`, it builds and publishes an image to GitHub Container Registry (GHCR).
- No extra secrets needed; it uses the built-in `GITHUB_TOKEN`.
- Image will be available as `ghcr.io/<OWNER>/<REPO>:<TAG>`.

### Steps to use
1) Create a new GitHub repo and push this project.
2) Go to the repo Settings → Packages → ensure GHCR is enabled for your account/org.
3) Push a tag to trigger CD:
   ```bash
   git tag v0.1.0 && git push origin v0.1.0
   ```

## Workflow summary
- `.github/workflows/ci.yml`: Test on push/PR; on tags, also build & push container to GHCR.