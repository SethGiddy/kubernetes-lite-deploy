Kubernetes Lite Deploy
======================

Lightweight Flask microservice demo with Prometheus metrics, intended for container+Kubernetes deployment.

Quickstart (local)
-------------------

1. Create and activate virtualenv, install deps:

```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run locally:

```bash
python -m src.app
# or (production) via gunicorn:
gunicorn -w 4 -b 0.0.0.0:5000 src.app:app
```

3. Run tests:

```bash
cd app
pytest -q
```

Docker
------

Build the image from the `app/` folder:

```bash
cd app
docker build -t kubernetes-lite-deploy:latest .
docker run -p 5000:5000 kubernetes-lite-deploy:latest
```

What I changed for you
----------------------
- Fixed metrics import/middleware integration so tests run.
- Added a production `Dockerfile` in `app/`.

Next recommended steps
----------------------
- Add basic Kubernetes manifests in `k8s/` (Deployment + Service + probes).
- Add a GitHub Actions workflow to run tests and build/push images.
- Populate `.github/workflows/` and `k8s/` when you're ready.

