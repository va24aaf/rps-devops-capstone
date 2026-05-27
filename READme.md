# RPS Devops Capstone Project

A cloud-native Rock,Paper Scissors application demonstrating a complete devops CI/CD pipeline using docker,GITHub Actions, Trivy, Kubernetes, ArgoCD, Prometheus and Grafana.

---

# Project Overview

This project showcases a production-syle DevOps workflow using a simple Flask-based Rock Paper Scissors game.

The primary focus is not the game itself,but the automation,security,deployment,monitoring and GitOps practices around the application lifecycle.

---

# Architecture
Developer
   ↓
GitHub Repository
   ↓
GitHub Actions CI Pipeline
   ↓
Docker Image Build
   ↓
Trivy Security Scan
   ↓
Azure Container Registry (ACR)
   ↓
ArgoCD GitOps Deployment
   ↓
Azure Kubernetes Service (AKS)
   ↓
Prometheus + Grafana Monitoring

---

# Technologies Used
Category	          Tools
Backend	               Flask
Version Control	       GitHub
CI/CD	               GitHub Actions
Containerization	   Docker
Security Scanning	   Trivy
Container Registry	   Azure Container Registry (ACR)
Orchestration	       Kubernetes (AKS)
GitOps	               ArgoCD
Monitoring	           Prometheus
Visualization	       Grafana

---

# Project Progress

---

# DAY 1 - Flask Application Development
 # Objectives
- Build a simple Rock Paper Scissors web application
- Add health monitoring endpoint
- Add Prometheus metrics endpoint
- Initialize Git repository

  # Features Implemented 
# 1. Rock Paper Scissors Gameplay
- User selects:
               Rock
               Paper
               Scissors
- Backend ramdomly generates computer choice
- Winner determination logic implemented

# 2. Monitoring Endpoints 
 # /health
- Used for:
           Kubernetes liveness probes
           Kubernetes readiness probes
- Example response

{
  "status": "healthy"
}

  # /metrics
- Prometheus metrics endpoint exposing:
        request count 
        request latency
- Implemented using:
        prometheus_client

---

# Project Structure
rps-devops-capstone/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
└── .gitignore

---
# Git Configuration
- Created .gitignore to exude:
          Virtual environments
          Python cache files
          OS-generated files
        
---

# Day 2 - Docker Containerzation

---
# Objectives
- Containerize the Flask Application
- Create Docker image
- Run application inside Docker container 

---

# Dockerfile
- Implemented production-style Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

---

# Docker Features
- Lightweight Python image
- Isolated runtime environment
- Port exposure for Flask app
- Dependency installation from requirements.txt

---

# .dockerignore
Create .dockerignore to reduce image size and exclude:
  - venv/
  - .git/
  - cache files

---

# Docker Testing
- Successfully:
   Built Docker image
   Ran container locaaly
   Verified:
           application endpoint
           /health
           /metrics

---

# Day 3 - GitHub Actions CI Pipeline 

---

# Objectives
- Automate Docker builds
- Intergrate security scanning
- Implement Continuous Integration workflow

---

# GitHub Actions Workflow 
Created CI Pipeline using: .github/workflows/ci.yml

---

# Pipeline Stages
1. Checkout Repository
Downloads source code into GitHub Actions runnner.
2. Docker Image Build 
Builds container image automatically on push.
3. Trivy Vulnerability Scan
Scans images for:
      OS vulnerabilities
      Library vulnerablities
Pipeline fails automatically on:
      CRITICAL vulnerabilities
---

# Security Scanning
- Implemented using: Aqua Security Trivy
- Security policy:
    Fails on CRITICAL vulnerabilities
    Ignore unfixed vulnerabilities 

---

# Image Tagging Strategy
- Implemented Commit SHA image tagging: rps-app:${{ github.sha }}
- Benefits:
           Immutable image versions
           Deployment traceability
           Rollback capability

---

# Branch Strategy
- CI pipeline triggers on:
  main
  develop

# Local Development 
 - Run flask app
        python app.py
 - Application
        http://localhost:5000
 - Run Docker Container 
    - Build image 
         docker build -t rps-app:v1 .
    - Run container
         docker run -p 5000:5000 rps-app:v1 

---

# Monitoring Endpoints
Endpoint	    Purpose
/health	        Application health check
/metrics	    Prometheus metrics

---

# Author 
 Vivian 








