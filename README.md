Kubernetes Lite Deploy
======================

This repository contains a small Flask-based microservice and the surrounding files needed to run it in a container and on Kubernetes.

The service exposes a few simple endpoints and includes Prometheus-compatible metrics collection.

Project contents
----------------

- `app/` - the Python app, including source, tests, requirements, and a `Dockerfile`.
- `app/src/` - app code, including the Flask app factory, routes, config, logging, and middleware.
- `app/tests/` - a minimal test suite for the health and version endpoints.
- `k8s/` - basic Kubernetes manifests for Deployment and Service.
- `.github/workflows/ci.yml` - GitHub Actions workflow that installs dependencies, runs tests, and builds/pushes the Docker image to GHCR.
- `.github/dependabot.yml` - dependency update configuration for Python, GitHub Actions, and Docker.
- `README.md` - this file.
- `terraform/` - currently empty; reserved for infrastructure code if added later.
- `monitoring/` - currently empty; reserved for monitoring-related assets.

What the app does
-----------------

The Flask app provides:

- `/` - a simple application info response.
- `/health` - health check response.
- `/ready` - readiness probe response.
- `/version` - version response.
- `/metrics` - Prometheus metrics output.

The app factory also configures JSON logging and request metrics middleware.

Local development
-----------------

```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Run locally:

```bash
cd app
python -m src.app
```

The app listens on `0.0.0.0:5000` by default.

Docker
------

Build the image from `app/`:

```bash
cd app
docker build -t kubernetes-lite-deploy:latest .
```

Run it locally:

```bash
docker run -p 5000:5000 kubernetes-lite-deploy:latest
```

Kubernetes
----------

A basic Deployment and Service are provided in `k8s/`.

The Deployment is configured with:

- 2 replicas
- liveness probe on `/health`
- readiness probe on `/ready`

The Service exposes the app on port `80` and forwards traffic to container port `5000`.

CI/CD
-----

The GitHub Actions workflow in `.github/workflows/ci.yml`:

- sets up Python and installs dependencies
- runs tests
- builds a Docker image
- pushes image tags to GitHub Container Registry (GHCR)

If you want to change the image destination or registry, update the workflow accordingly.

Notes
-----

- `terraform/` is empty today, so infrastructure is not defined in this repo yet.
- `monitoring/` is also empty and can be used for dashboards or alerting configs later.
- `docs/` and `diagrams/` contain optional supporting doc assets.

That is the current shape of this project.

