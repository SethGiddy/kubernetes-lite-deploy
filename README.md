# Kubernetes-Lite Deploy

A lightweight web-based deployment management platform for developers and small teams to build, package, deploy, and monitor containerised applications without needing to manage the full complexity of Kubernetes.

## 🚀 What is Kubernetes-Lite Deploy?

Kubernetes-Lite Deploy is a web application designed to simplify common container deployment workflows.

The idea is simple:

> **Build your application → package it as a container → deploy it → monitor its status from one place.**

In a real-world environment, a tool like this could help small development teams standardise application deployments without requiring every developer to become a Kubernetes expert.

The project is currently being developed as a practical DevOps engineering project, with the long-term goal of evolving it into a useful deployment and operations platform.

---

## 💡 Real-World Use Cases

Kubernetes-Lite Deploy could eventually be used by:

- **Small development teams** that need a simple deployment platform.
- **Startups** that want to deploy containerised applications without managing a large Kubernetes environment.
- **Development teams** that need repeatable application deployment workflows.
- **Training organisations** that want a practical environment for teaching containerisation and DevOps.
- **Internal engineering teams** that want a lightweight interface around their existing container infrastructure.

Potential future capabilities include:

- Application deployment
- Container image management
- Deployment status
- Application health monitoring
- Deployment history
- Environment management
- Rollback support
- Logs and troubleshooting
- CI/CD integration
- Role-based access control

---

## 🏗️ Current Architecture

The application currently uses a containerised Python web application and is being developed around modern DevOps practices.

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Automated Tests
    ├── Docker Build
    └── Container Image
          │
          ▼
     Azure Container Registry
          │
          ▼
   Azure Container Apps
          │
          ▼
   Kubernetes-Lite Deploy
```

---

## 🛠️ Technology Stack

### Application

- Python
- Flask
- Gunicorn
- Pytest

### Containerisation

- Docker
- Docker Buildx
- Docker Compose

### Cloud & Deployment

- Microsoft Azure
- Azure Container Registry
- Azure Container Apps
- Azure CLI

### CI/CD

- GitHub Actions
- Automated testing
- Automated Docker image builds
- GitHub Actions OIDC authentication with Azure

### Development

- Git
- GitHub
- VS Code
- Linux / WSL
- Windows

---

## 🔄 Current CI/CD Workflow

The project currently follows this workflow:

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ├── Checkout source
   ├── Setup Python
   ├── Install dependencies
   ├── Run tests
   ├── Build Docker image
   └── Authenticate with Azure using OIDC
          │
          ▼
      Azure
```

The GitHub Actions pipeline uses **OIDC authentication** rather than storing a long-lived Azure client secret in GitHub.

This provides a more secure authentication model for CI/CD.

---

## 🔐 Security Approach

Security is treated as a core part of the project rather than something added at the end.

Current practices include:

- GitHub Actions OIDC authentication
- No Azure credentials stored directly in the repository
- Azure identity-based authentication
- Containerised application deployment
- Azure Container Registry for container images
- Repository secrets and variables for environment-specific configuration
- Least-privilege permissions where practical

Sensitive information such as subscription IDs, tenant IDs, service-principal object IDs, credentials, tokens and secrets should **never be committed to this repository**.

---

## 📦 Container Image

The application is packaged as a Docker image and stored in Azure Container Registry.

Example image:

```text
kubeliteacr1933.azurecr.io/kubernetes-lite-deploy
```

The image can then be consumed by the deployment environment.

---

## ☁️ Azure Deployment

The application is currently deployed using **Azure Container Apps**.

Azure Container Apps provides a managed container runtime while avoiding the operational overhead of maintaining a Kubernetes cluster for this stage of the project.

The application is configured to expose the web service through Azure Container Apps ingress.

---

## 🧪 Testing

Tests are executed automatically through GitHub Actions.

The current pipeline runs:

```bash
pip install -r requirements.txt
pytest -q
```

A deployment should only progress after the application passes its automated tests.

---

## 🎯 Project Goals

The project is being developed incrementally with the following goals:

1. Build a working web application.
2. Containerise the application.
3. Automate testing.
4. Automate image creation.
5. Implement secure cloud authentication.
6. Deploy the application to Azure.
7. Introduce automated deployments.
8. Add deployment and application monitoring.
9. Improve reliability and security.
10. Evolve the project toward a practical deployment management platform.

---

## 🗺️ Roadmap

### Phase 1 — Application

- [x] Python web application
- [x] Application testing
- [x] Docker containerisation

### Phase 2 — Cloud

- [x] Azure Container Registry
- [x] Azure Container Apps
- [x] Application ingress
- [x] Container deployment

### Phase 3 — CI/CD

- [x] GitHub Actions
- [x] Automated testing
- [x] Docker image build
- [x] Azure OIDC authentication
- [x] GitHub Actions Azure authentication
- [ ] Automated deployment to Azure
- [ ] Deployment verification

### Phase 4 — Platform Features

- [ ] Deployment dashboard
- [ ] Deployment history
- [ ] Application health status
- [ ] Container logs
- [ ] Environment management
- [ ] Rollback capability
- [ ] Monitoring and alerts

### Phase 5 — Production Readiness

- [ ] Improved application security
- [ ] Infrastructure as Code
- [ ] Observability
- [ ] Error handling
- [ ] Performance testing
- [ ] Production deployment strategy

---

## 📚 Project Purpose

Kubernetes-Lite Deploy is being developed as a practical DevOps project to demonstrate how a software application can move from source code to a secure, automated cloud deployment.

The project focuses on **real engineering practices**, including:

- Software development
- Testing
- Git workflows
- Containerisation
- CI/CD
- Cloud infrastructure
- Identity and authentication
- Deployment automation
- Security
- Monitoring

The goal is not simply to build another demo application, but to progressively develop a system that reflects how modern engineering teams build and operate cloud applications.

---

## 🤝 Contributing

Contributions, suggestions and improvements are welcome.

For major changes, please open an issue first to discuss the proposed change.

---

## 📄 License

This project is currently maintained as a personal development project.