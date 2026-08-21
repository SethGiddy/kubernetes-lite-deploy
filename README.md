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
- `terraform/` - reserved for infrastructure code if added later.
- `monitoring/` - local Prometheus and Grafana files for observability.

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

For a local Kubernetes cluster, build the image and apply the manifests:

```bash
docker build -t kubernetes-lite-deploy:latest ./app
kubectl apply -f k8s/
kubectl port-forward service/kubernetes-lite-deploy 5000:80
```

Then open http://localhost:5000. The Deployment uses `IfNotPresent` so a locally built image can be used without a registry.

Local monitoring
----------------

Prometheus and Grafana can run locally at no hosting cost:

```bash
cd monitoring
docker compose up --build
```

See `monitoring/README.md` for dashboard setup and local URLs.

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

- `terraform/` is reserved for future infrastructure definitions.
- `monitoring/` contains a local-only Prometheus and Grafana setup.
- `docs/` and `diagrams/` contain optional supporting doc assets.

That is the current shape of this project.

Project Demonstration
---------------------

The application is deployed to a local Kubernetes cluster running on Docker Desktop.

Example response from the root endpoint:

```json
{
	"application": "devops-health-api",
	"message": "Welcome to Kubernetes Lite Deploy",
	"version": "1.0.0"
}
```

Architecture
------------

```text
Docker Image
		 |
		 v
Kubernetes Deployment
		 |
		 +--> Pod
		 +--> Pod
		 +--> Pod ...
		 |
		 v
ClusterIP Service (port 80)
		 |
		 v
Flask API (port 5000)
		 |
		 v
Metrics Server
		 |
		 v
Horizontal Pod Autoscaler
CPU target: 60% | Minimum: 2 pods | Maximum: 10 pods
```

Technologies
------------

- Python and Flask
- Gunicorn
- Docker
- Kubernetes
- Docker Desktop Kubernetes
- kubectl
- Metrics Server
- Horizontal Pod Autoscaler
- Git and GitHub

Kubernetes Components
---------------------

### Deployment

The Kubernetes Deployment manages application replicas and provides self-healing:

```bash
kubectl get deployment kubernetes-lite-deploy
```

### Service

A ClusterIP Service provides stable internal networking:

```text
Service port: 80
Target port: 5000
```

Test the application from inside the cluster:

```bash
kubectl run curl-test \
	--rm -it \
	--image=curlimages/curl \
	--restart=Never \
	-- curl -s http://kubernetes-lite-deploy
```

Expected response:

```json
{
	"application": "devops-health-api",
	"message": "Welcome to Kubernetes Lite Deploy",
	"version": "1.0.0"
}
```

### Health Checks

The application uses `/health` for the liveness probe and `/ready` for the readiness probe. These allow Kubernetes to determine whether each application pod is healthy and ready to receive traffic.

### Resource Management

Each pod defines CPU and memory requests and limits:

```yaml
resources:
	requests:
		cpu: "100m"
		memory: "128Mi"
	limits:
		cpu: "500m"
		memory: "256Mi"
```

Monitoring and Autoscaling
--------------------------

Metrics Server provides CPU and memory utilization:

```bash
kubectl top pods
kubectl top nodes
```

Example output:

```text
NAME                                  CPU     MEMORY
kubernetes-lite-deploy-xxxxx          15m     106Mi
kubernetes-lite-deploy-yyyyy          10m     113Mi
```

Prometheus and Grafana are also available for local application metrics. See [monitoring/README.md](monitoring/README.md) for setup instructions.

### Horizontal Pod Autoscaler

The HPA is configured with:

- Minimum replicas: 2
- Maximum replicas: 10
- CPU target: 60%

Check the HPA:

```bash
kubectl get hpa kubernetes-lite-deploy
```

### HPA Load Test

Use a temporary BusyBox pod to generate HTTP traffic:

```bash
kubectl run load-generator \
	--image=busybox:1.36 \
	--restart=Never \
	-- /bin/sh -c 'while true; do wget -q -O- http://kubernetes-lite-deploy >/dev/null; done'
```

Watch CPU utilization and replica changes:

```bash
kubectl get hpa kubernetes-lite-deploy --watch
kubectl get deployment kubernetes-lite-deploy --watch
```

After testing, remove the load generator:

```bash
kubectl delete pod load-generator
```

This demonstrates automatic scale-up under load and scale-down after the load is removed.

### Multi-Node Scheduling

Check pod placement across available Kubernetes nodes:

```bash
kubectl get pods -o wide
kubectl get nodes
```

When multiple worker nodes are available, this shows Kubernetes workload scheduling across nodes.

Key Learning Outcomes
---------------------

This project demonstrates practical experience with:

- Docker containerization
- Kubernetes Deployments
- Pods and ReplicaSets
- Kubernetes Services
- ClusterIP networking
- Health probes
- Resource requests and limits
- Metrics Server and `kubectl top`
- Horizontal Pod Autoscaling
- Multi-node scheduling
- Kubernetes self-healing
- Load testing
- DevOps troubleshooting

Future Improvements
-------------------

Potential next steps include:

- Kubernetes Ingress
- TLS/HTTPS
- NetworkPolicies
- Security scanning
- Helm packaging
- Cloud deployment

Author
------

**Ayo Oke**

DevOps | Kubernetes | Docker | Linux | Azure

