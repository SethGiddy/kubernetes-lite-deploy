# Kubernetes Lite Deploy

A production-style mini DevOps project demonstrating how to containerise, deploy, monitor, and automatically scale a Python web application using Kubernetes.

The project deploys a lightweight Flask/Gunicorn health API to a local Kubernetes cluster running on Docker Desktop. Kubernetes manages multiple application replicas, distributes workloads across worker nodes, exposes the application through a ClusterIP Service, monitors application health, collects resource metrics, and automatically scales the application using a Horizontal Pod Autoscaler (HPA).

---

## Project Overview

The goal of this project is to demonstrate practical Kubernetes and DevOps concepts using a small but realistic application.

The application is a simple health API called:

`devops-health-api`

When accessed, it returns:

```json
{
  "application": "devops-health-api",
  "message": "Welcome to Kubernetes Lite Deploy",
  "version": "1.0.0"
}