# ClusterPulse

**A Kubernetes Cluster Monitoring API built with Python, FastAPI, and Helm.**

ClusterPulse is a containerized REST API that provides visibility into Kubernetes cluster resources. It demonstrates practical experience with Kubernetes deployments, role-based access control (RBAC), containerization, Helm package management, and Linux-based development workflows.

## Project Overview

ClusterPulse communicates with the Kubernetes API to retrieve information about cluster nodes and pods.

The application is designed to run inside a Kubernetes cluster using a dedicated ServiceAccount with read-only permissions.

### Core Features

- REST API developed using Python and FastAPI
- Kubernetes node discovery
- Pod visibility across namespaces
- Kubernetes RBAC authorization
- Containerized application using Podman
- Helm chart for deployment and lifecycle management
- Health endpoint for Kubernetes readiness and liveness probes
- Local Kubernetes development using kind and WSL2

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | REST API framework |
| Kubernetes | Container orchestration |
| Helm | Kubernetes application packaging |
| Podman | Container image building |
| kind | Local Kubernetes cluster |
| RBAC | Kubernetes API authorization |
| Git / GitHub | Version control |
| Ubuntu / WSL2 | Development environment |

## Architecture

```text
Developer / API Client
          |
          v
     FastAPI Service
       ClusterPulse
          |
          v
 Kubernetes Python Client
          |
          v
 Kubernetes API Server
          |
          v
    Nodes and Pods
```

ClusterPulse uses a Kubernetes ServiceAccount and read-only RBAC permissions to query cluster resources.

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Application health status |
| `/api/nodes` | GET | Retrieve cluster node information |
| `/api/pods` | GET | Retrieve pod information across namespaces |
| `/docs` | GET | Interactive Swagger API documentation |

## Deployment

### Prerequisites

- A running Kubernetes cluster
- kubectl configured to access the cluster
- Helm 3
- A container image available to the cluster

### Install with Helm

From the repository root:

```bash
helm install clusterpulse ./helm/clusterpulse --namespace default
```

Verify deployment:

```bash
kubectl get pods -l app=clusterpulse
kubectl rollout status deployment/clusterpulse
```

### Access the API

Forward the Kubernetes Service to your local machine:

```bash
kubectl port-forward svc/clusterpulse 8080:8000
```

Then visit:

```text
http://localhost:8080/docs
```

### Upgrade the Application

```bash
helm upgrade clusterpulse ./helm/clusterpulse --namespace default
```

### View Helm Release History

```bash
helm history clusterpulse
```

## Repository Structure

```text
clusterpulse/
├── app/
│   └── main.py
├── helm/
│   └── clusterpulse/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
├── kubernetes/
│   └── clusterpulse.yaml
├── Containerfile
├── requirements.txt
└── README.md
```

## Engineering Concepts Demonstrated

This project provides hands-on practice with:

- Kubernetes Deployments and Services
- ServiceAccounts, ClusterRoles, and ClusterRoleBindings
- Helm installation, upgrades, and release history
- Container image packaging
- Kubernetes API integration
- Health probes and resource configuration
- Git-based source control and project documentation

## Roadmap

- [ ] Add automated API tests
- [ ] Implement structured logging and improved error handling
- [ ] Add a web-based cluster monitoring dashboard
- [ ] Integrate Prometheus metrics
- [ ] Add CI/CD using GitHub Actions
- [ ] Expand Kubernetes resource monitoring
- [ ] Create a technical demonstration video

## Project Status

**Active development — initial Kubernetes API and Helm deployment implemented.**

ClusterPulse is a personal engineering lab intended for learning, experimentation, and demonstrating practical Kubernetes development skills.
