# Learning Log

## 2026-10-02: Setup and containers

**Done:** Installed Colima, Docker, kubectl, kind, helm and k9s. Built a FastAPI app with /, /health and /metrics endpoints. Wrote a multi-stage Dockerfile running as a non-root user. Created a local kind cluster.

**Issues and fixes:**
- `pull access denied` on docker run: typo in the image name (hello-word)
- `Could not import module app.main`: main.py was outside the app folder
- REQUIREMENTS.txt in uppercase: works on macOS (case-insensitive filesystem) but would break inside the Linux container
- `ModuleNotFoundError` with the venv active: uvicorn was resolving to the global Python install; fixed by installing dependencies in the venv and running `python -m uvicorn`
- kubectl calling localhost:8080: no cluster in the kubeconfig; fixed by creating the kind cluster
