# Learning Log

## 2026-10-02: Setup and containers

**Done:** Installed Colima, Docker, kubectl, kind, helm and k9s. Built a FastAPI app with /, /health and /metrics endpoints. Wrote a multi-stage Dockerfile running as a non-root user. Created a local kind cluster.

**Issues and fixes:**
- `pull access denied` on docker run: typo in the image name (hello-word)
- `Could not import module app.main`: main.py was outside the app folder
- REQUIREMENTS.txt in uppercase: works on macOS (case-insensitive filesystem) but would break inside the Linux container
- `ModuleNotFoundError` with the venv active: uvicorn was resolving to the global Python install; fixed by installing dependencies in the venv and running `python -m uvicorn`
- kubectl calling localhost:8080: no cluster in the kubeconfig; fixed by creating the kind cluster

**Incident during rolling update:**
- Changed the Deployment to image `platform-lab:0.2.0` before building it, so the new Pod went into ErrImagePull and then ImagePullBackOff
- The rolling update stopped after the first new Pod failed; the 3 old Pods kept serving traffic, so there was no downtime
- Fix: built 0.2.0, loaded it into kind, deleted the failing Pod to skip the backoff timer; the rollout then completed on its own
- Tested `rollout undo` back to 0.1.0, then reverted the manifest so Git and the cluster match again

## Config, health and troubleshooting

**Done:** Moved the app to the `lab` namespace. Added a ConfigMap, a Secret (created imperatively, kept out of Git), readiness and liveness probes, and CPU/memory requests and limits.

**Troubleshooting:**

### CrashLoopBackOff
- Symptom:
- How I diagnosed it:
- Root cause:
- Fix:

### OOMKilled
- Symptom:
- How I diagnosed it:
- Root cause:
- Fix:

### ImagePullBackOff
- Symptom:
- How I diagnosed it:
- Root cause:
- Fix:

### Readiness vs liveness failures
- What I observed:
