---
published: true
type: workshop
title: Containers Masterclass - From Zero to Production
short_title: Docker & Podman Lab
description: An intensive hands-on workshop to master containerization. Learn to build, secure, and deploy production-ready containers using real-world scenarios from Netflix, Spotify, and Fortune 500 companies. Master Docker CLI with Podman as your container engine.
level: beginner
authors:
  - Abdoul-Hakim Afraitane
contacts:
  - https://www.linkedin.com/in/abdoul-hakim-afraitane/
duration_minutes: 480
tags: docker, podman, containers, devops, kubernetes, microservices
banner_url: assets/banner.png
navigation_levels: 2
navigation_numbering: true
sections_title:
  - Why Containers Changed Everything
  - Podman Installation & Setup
  - Container Architecture Internals
  - Mastering Container Images
  - Running Production Containers
  - Crafting Perfect Dockerfiles
  - Container Operations & Debugging
  - Network Engineering for Containers
  - Persistent Storage Strategies
  - Real-World Multi-Container Apps
  - Security Hardening
  - Production Troubleshooting
  - Graduation & Next Steps
---

# Containers Masterclass: From Zero to Production

Welcome to this intensive container workshop! You're about to learn the technology that powers **Netflix** (serving 247 million subscribers), **Spotify** (100 million daily users), and **95% of Fortune 500 companies**.

> **"Containers are the most significant advancement in application deployment since virtual machines."**  
> — Kelsey Hightower, Google Cloud

## 🚀 Why This Workshop Will Transform Your Career

By mastering containers, you'll be able to:

| Skill | Career Impact |
|-------|---------------|
| Build containerized apps | **+35% salary premium** for DevOps roles |
| Deploy to Kubernetes | Required by **85%** of cloud job postings |
| Debug production issues | Stand out in technical interviews |
| Implement security best practices | Lead enterprise containerization projects |

## 🎯 What Makes This Workshop Different

Unlike generic tutorials, this workshop uses **real scenarios** from:

- 🎬 **Netflix**: How they deploy 1,000+ microservices
- 🎵 **Spotify**: Container orchestration for 500M users  
- 🏦 **Goldman Sachs**: Secure container pipelines in finance
- 🛒 **Amazon**: Container patterns for e-commerce at scale

## 📅 Full-Day Intensive Agenda

| Time | Topic | Real-World Scenario |
|------|-------|---------------------|
| 09:00 - 09:45 | Why Containers Changed Everything | The Netflix transformation story |
| 09:45 - 10:30 | Podman Installation & Setup | Enterprise-grade local environment |
| 10:30 - 10:45 | ☕ **Break** | |
| 10:45 - 11:45 | Container Architecture Internals | How Google runs 4 billion containers/week |
| 11:45 - 12:45 | Mastering Container Images | Spotify's image optimization strategy |
| 12:45 - 13:45 | 🍽️ **Lunch Break** | |
| 13:45 - 14:45 | Running Production Containers | Amazon's deployment patterns |
| 14:45 - 15:45 | Crafting Perfect Dockerfiles | Goldman Sachs security standards |
| 15:45 - 16:00 | ☕ **Break** | |
| 16:00 - 16:45 | Network Engineering | Istio service mesh concepts |
| 16:45 - 17:30 | Persistent Storage | Stateful apps like PostgreSQL |
| 17:30 - 18:15 | Multi-Container Applications | Complete e-commerce stack |
| 18:15 - 18:30 | Graduation & Next Steps | Your container certification path |

## 📋 Prerequisites

| Requirement | Details |
|-------------|---------|
| **Operating System** | Windows 10/11, macOS 12+, or Linux (Ubuntu 22.04+) |
| **Hardware** | 8GB RAM minimum, 16GB recommended, 25GB free disk |
| **Software** | VS Code with Docker extension |
| **Knowledge** | Basic command line familiarity |
| **Mindset** | Ready to build something real! |

---

## 1. Why Containers Changed Everything

### 1.1 The $1.5 Billion Problem

**Real Story: Knight Capital Group (2012)**

On August 1st, 2012, Knight Capital deployed new trading software to production. Within 45 minutes:
- ❌ A configuration mismatch between servers caused erratic trades
- 💸 The company lost **$440 million** 
- 📉 Stock dropped 75% in two days
- 🏚️ Company was sold at a massive loss

**The Root Cause?** Inconsistent deployment environments. What worked in testing failed catastrophically in production.

> **This single incident could have been prevented with containers.**

### 1.2 The "Works on My Machine" Crisis

Every developer has experienced this:

```
┌─────────────────────────────────────────────────────────────────┐
│                  THE DEPLOYMENT NIGHTMARE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Developer's Laptop          Production Server                 │
│   ─────────────────          ──────────────────                │
│   • Python 3.11              • Python 3.9 😱                   │
│   • Node 20.x                • Node 16.x 😱                    │
│   • PostgreSQL 15            • PostgreSQL 12 😱                │
│   • Ubuntu 22.04             • RHEL 8 😱                       │
│   • OpenSSL 3.0              • OpenSSL 1.1 😱                  │
│                                                                 │
│   Result: "It works on my machine!" → Production crash 💥       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Industry Statistics:**
- 🔥 **62%** of outages are caused by deployment issues (Gartner)
- ⏱️ **Average MTTR** (Mean Time To Recovery): 4.2 hours
- 💵 **Cost of downtime**: $5,600 per minute (average enterprise)

### 1.3 How Netflix Solved This Problem

**Before Containers (2008-2012):**
- 🐌 Deployments took weeks
- 🔥 Frequent production failures
- 😰 Engineers feared Friday deployments

**After Containers (2013-Present):**
- 🚀 **Thousands of deployments per day**
- ⚡ Changes go live in minutes
- 🎯 99.99% uptime SLA

```
┌─────────────────────────────────────────────────────────────────┐
│             NETFLIX CONTAINER ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│     ┌──────────────────────────────────────────────────┐       │
│     │              Netflix Platform                     │       │
│     │     247 Million Subscribers Worldwide             │       │
│     └──────────────────────────────────────────────────┘       │
│                            │                                    │
│              ┌─────────────┼─────────────┐                     │
│              │             │             │                      │
│         ┌────┴────┐  ┌────┴────┐  ┌────┴────┐                 │
│         │ Content │  │  User   │  │ Payment │                  │
│         │ Service │  │ Service │  │ Service │                  │
│         │ (1000+  │  │ (500+   │  │ (200+   │                  │
│         │ contain-│  │ contain-│  │ contain-│                  │
│         │  ers)   │  │  ers)   │  │  ers)   │                  │
│         └─────────┘  └─────────┘  └─────────┘                  │
│                                                                 │
│     Each microservice runs in isolated containers              │
│     Auto-scales based on demand (Black Friday = 3x traffic)    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.4 What Exactly Is a Container?

A container is a **standardized unit of software** that packages:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ANATOMY OF A CONTAINER                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌───────────────────────────────────────────────────┐       │
│    │                YOUR APPLICATION                    │       │
│    │   • Source code (app.py, index.js, Main.java)     │       │
│    │   • Business logic                                │       │
│    ├───────────────────────────────────────────────────┤       │
│    │               DEPENDENCIES                         │       │
│    │   • Libraries (Flask, Express, Spring)            │       │
│    │   • Frameworks & packages                         │       │
│    ├───────────────────────────────────────────────────┤       │
│    │                 RUNTIME                            │       │
│    │   • Python 3.11, Node 20, JDK 21                  │       │
│    ├───────────────────────────────────────────────────┤       │
│    │              SYSTEM LIBRARIES                      │       │
│    │   • glibc, OpenSSL, libcurl                       │       │
│    ├───────────────────────────────────────────────────┤       │
│    │              CONFIGURATION                         │       │
│    │   • Environment variables                         │       │
│    │   • Config files                                  │       │
│    └───────────────────────────────────────────────────┘       │
│                                                                 │
│    All of this ships together → Runs identically everywhere    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**The Container Promise:**

> **"If it runs in a container on my laptop, it will run exactly the same in production."**

### 1.5 Containers vs. Virtual Machines: The Technical Truth

```
┌─────────────────────────────────────────────────────────────────┐
│                    VIRTUAL MACHINES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │  App A   │  │  App B   │  │  App C   │                      │
│  │  200MB   │  │  150MB   │  │  300MB   │                      │
│  ├──────────┤  ├──────────┤  ├──────────┤                      │
│  │ Guest OS │  │ Guest OS │  │ Guest OS │   ← 3 copies!        │
│  │   5GB    │  │   5GB    │  │   5GB    │   = 15GB wasted      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌─────────────────────────────────────────────────────┐       │
│  │                   Hypervisor                        │       │
│  └─────────────────────────────────────────────────────┘       │
│  │                    Host OS                          │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                 │
│  Total: ~16GB RAM, 60 seconds to boot, 15% CPU overhead        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

                            vs

┌─────────────────────────────────────────────────────────────────┐
│                       CONTAINERS                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │  App A   │  │  App B   │  │  App C   │                      │
│  │  200MB   │  │  150MB   │  │  300MB   │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌─────────────────────────────────────────────────────┐       │
│  │              Container Runtime                      │       │
│  │         (containerd/Podman) ~50MB                   │       │
│  └─────────────────────────────────────────────────────┘       │
│  │              Host OS (shared kernel)                │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                 │
│  Total: ~700MB RAM, milliseconds to start, near-native perf   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Quantified Comparison:**

| Metric | Virtual Machines | Containers | Improvement |
|--------|-----------------|------------|-------------|
| **Startup Time** | 30-60 seconds | 50-500 ms | **60-1000x faster** |
| **Memory Overhead** | 1-2 GB per VM | 10-100 MB per container | **10-100x less** |
| **Disk Space** | 5-50 GB per VM | 10-500 MB per container | **10-100x smaller** |
| **Density** | 10-20 per host | 100-1000 per host | **10-50x more** |
| **CPU Overhead** | 5-15% | <1% | **Near-native** |

### 1.6 The Container Ecosystem: Tools You'll Work With

```
┌─────────────────────────────────────────────────────────────────┐
│              THE CONTAINER ECOSYSTEM (2026)                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BUILD & DEVELOP           REGISTRIES              RUNTIMES     │
│  ───────────────          ──────────              ─────────     │
│  • Docker CLI ⭐          • Docker Hub ⭐         • containerd  │
│  • Podman ⭐              • GitHub GHCR ⭐        • CRI-O       │
│  • Buildah               • Azure ACR            • Podman ⭐    │
│  • Kaniko                • AWS ECR              • gVisor       │
│  • Docker Compose        • Google Artifact      • Kata         │
│                            Registry                             │
│                                                                 │
│  ORCHESTRATION            SECURITY               NETWORKING     │
│  ─────────────           ─────────              ───────────     │
│  • Kubernetes ⭐         • Trivy ⭐             • CNI plugins  │
│  • Docker Swarm          • Snyk                 • Cilium       │
│  • Amazon ECS            • Falco                • Calico       │
│  • Azure Container Apps  • cosign               • Istio        │
│  • Google Cloud Run      • SBOM                 • Envoy        │
│                                                                 │
│  ⭐ = What we'll use in this workshop                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.7 Docker vs Podman: Why We're Using Podman

| Feature | Docker | Podman |
|---------|--------|--------|
| **Architecture** | Daemon-based (dockerd) | Daemonless |
| **Root Required** | Yes (by default) | No (rootless by default) |
| **Security** | Good | Excellent (no root daemon) |
| **Docker Compatible** | Native | 100% compatible CLI |
| **License** | Docker Desktop requires license for enterprise | Free & Open Source |
| **Kubernetes** | Requires additional tools | Native pod support |
| **SystemD Integration** | Limited | Native |

**Why Podman for this workshop:**
1. ✅ **Free for everyone** - No licensing concerns
2. ✅ **More secure** - Rootless by design
3. ✅ **Same commands** - `docker` = `podman` (alias)
4. ✅ **Future-proof** - Native Kubernetes pod support
5. ✅ **Enterprise-ready** - Used by Red Hat, IBM, and US Government

> **Note:** All `docker` commands in this workshop work identically with `podman`. We'll set up an alias so you can use either!

### 1.8 Real-World Success Stories

**Spotify: 500 Million Users**
```
┌─────────────────────────────────────────────────────────────────┐
│                    SPOTIFY'S CONTAINER STACK                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Before (2014):                 After (2018+):                  │
│  • 2-week deployment cycles     • 1000+ deployments/day         │
│  • Manual server provisioning   • Auto-scaling Kubernetes       │
│  • Frequent outages            • 99.95% uptime                  │
│  • 100 engineers on infra      • 15 platform engineers          │
│                                                                 │
│  Their secret: Containerized microservices with automated CI/CD │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Goldman Sachs: Financial Services**
- 🔒 **10,000+ containers** running trading systems
- ⚡ **Microsecond latency** requirements met
- 🛡️ **Zero security breaches** from container isolation
- 📊 **90% cost reduction** in infrastructure

### 1.9 🧪 Pre-Lab: Test Your Understanding

Before we install anything, let's ensure you understand the concepts:

**Scenario Analysis:**

Your team manages an e-commerce platform. Black Friday is coming, and you expect 10x normal traffic.

**Question 1:** With VMs, how would you handle the traffic spike?
<details>
<summary>Show Analysis</summary>

With VMs:
- Pre-provision 10x servers (expensive, wasteful on normal days)
- Wait 5-10 minutes per VM to boot
- Hope the load balancer catches up
- Pay for unused capacity year-round

**Cost estimate:** $50,000/month in unused VM capacity

</details>

**Question 2:** How would containers change this?
<details>
<summary>Show Analysis</summary>

With containers:
- Auto-scale from 10 to 100 containers in seconds
- Each container boots in milliseconds
- Scale down automatically after the peak
- Pay only for what you use

**Cost estimate:** $5,000/month (scale on demand)
**Savings:** $540,000/year

</details>

### 1.10 ✅ Section Checkpoint

Before continuing, verify you understand:

| Concept | Check |
|---------|-------|
| Why containers exist | ☐ Solve deployment inconsistency |
| Container vs VM difference | ☐ Shared kernel, lightweight, fast |
| When to use containers | ☐ Microservices, CI/CD, scaling |
| Why Podman | ☐ Rootless, free, Docker-compatible |
| Business value | ☐ Faster deploys, lower costs, reliability |

---

## 2. Podman Installation & Setup

### 2.1 Understanding Podman Architecture

Unlike Docker, Podman uses a **daemonless architecture**:

```
┌─────────────────────────────────────────────────────────────────┐
│                  DOCKER ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    REST     ┌──────────────┐                 │
│  │ Docker CLI   │───────────▶│ Docker Daemon │                 │
│  │ (as user)    │    API     │ (runs as ROOT)│ ← Security risk │
│  └──────────────┘            └──────┬───────┘                  │
│                                     │                           │
│                                     ▼                           │
│                              ┌─────────────┐                    │
│                              │ Containers  │                    │
│                              └─────────────┘                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                  PODMAN ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐         ┌──────────────┐                     │
│  │ Podman CLI   │────────▶│  Container   │                     │
│  │ (as user)    │ direct  │ (as user)    │ ← Rootless!         │
│  └──────────────┘         └──────────────┘                     │
│                                                                 │
│  No daemon running = No attack surface                          │
│  User runs containers = No privilege escalation                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Installing Podman Desktop (Windows)

**Step 1: System Prerequisites**

```powershell
# Open PowerShell as Administrator

# Check Windows version (need Windows 10 build 19041+ or Windows 11)
winver

# Enable WSL 2
wsl --install

# If already installed, update WSL
wsl --update

# Set WSL 2 as default
wsl --set-default-version 2

# Restart your computer after this step
```

**Step 2: Download and Install Podman Desktop**

1. Go to [podman-desktop.io](https://podman-desktop.io/)
2. Click **"Download for Windows"**
3. Run the installer `podman-desktop-x.x.x-setup.exe`
4. Follow the installation wizard:
   - Accept the license agreement
   - Choose installation directory (default is fine)
   - Click "Install"
5. Launch Podman Desktop when installation completes

**Step 3: Initialize Podman Machine**

When Podman Desktop launches for the first time:

1. Click **"Install Podman"** if prompted
2. Wait for Podman CLI to be installed
3. Click **"Create Podman Machine"**
4. Configure the machine:
   - **Name:** `podman-machine-default`
   - **CPUs:** 4 (or more)
   - **Memory:** 6GB (or more)
   - **Disk:** 50GB (or more)
5. Click **"Create"** and wait for the machine to initialize
6. Click **"Start"** to start the machine

**Step 4: Verify Installation**

Open a new PowerShell terminal:

```powershell
# Check Podman version
podman --version
# Expected: podman version 4.x.x or higher

# Check machine status
podman machine list
# Should show "Running"

# Set up Docker alias (so all docker commands work)
Set-Alias -Name docker -Value podman

# Test with hello-world
podman run hello-world

# Or use docker command (thanks to alias)
docker run hello-world
```

**Step 5: Make Docker Alias Permanent**

```powershell
# Add alias to PowerShell profile
Add-Content -Path $PROFILE -Value 'Set-Alias -Name docker -Value podman'

# Create the profile if it doesn't exist
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value 'Set-Alias -Name docker -Value podman'
```

### 2.3 Installing Podman Desktop (macOS)

**Step 1: Download Podman Desktop**

**Option A - Direct Download:**
1. Go to [podman-desktop.io](https://podman-desktop.io/)
2. Click "Download for macOS"
3. Choose your architecture:
   - **Apple Silicon** (M1/M2/M3/M4)
   - **Intel**
4. Open the downloaded `.dmg` file
5. Drag "Podman Desktop" to Applications

**Option B - Using Homebrew:**
```bash
# Install Homebrew if you haven't
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Podman Desktop
brew install --cask podman-desktop

# Or just Podman CLI
brew install podman
```

**Step 2: Initialize Podman Machine**

```bash
# Initialize a new Podman machine
podman machine init --cpus 4 --memory 6144 --disk-size 50

# Start the machine
podman machine start

# Verify it's running
podman machine list
```

**Step 3: Set Up Docker Compatibility**

```bash
# Add alias to your shell profile
echo 'alias docker=podman' >> ~/.zshrc  # for Zsh (default on modern macOS)
# or
echo 'alias docker=podman' >> ~/.bash_profile  # for Bash

# Reload shell
source ~/.zshrc

# Verify
docker --version  # Should show podman version
```

**Step 4: Test Installation**

```bash
# Run hello-world
podman run hello-world

# Run interactive Ubuntu
podman run -it ubuntu:22.04 bash
cat /etc/os-release
exit

# Run Nginx with port mapping
podman run -d -p 8080:80 --name test-nginx nginx:alpine
curl http://localhost:8080
podman stop test-nginx && podman rm test-nginx
```

### 2.4 Installing Podman (Linux - Ubuntu/Debian)

**Step 1: Update System and Install Podman**

```bash
# Update package index
sudo apt-get update

# Install Podman (Ubuntu 22.04+)
sudo apt-get install -y podman

# For older versions, add the repository first
# Ubuntu 20.04:
. /etc/os-release
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
curl -L "https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/Release.key" | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y podman
```

**Step 2: Verify Installation**

```bash
# Check version
podman --version

# Test rootless container
podman run hello-world

# Show system info
podman info
```

**Step 3: Set Up Docker Alias**

```bash
# Add docker alias
echo 'alias docker=podman' >> ~/.bashrc
source ~/.bashrc

# Verify
docker --version
docker run hello-world
```

**Step 4: (Optional) Install Podman Desktop**

```bash
# Download Podman Desktop AppImage
wget https://github.com/containers/podman-desktop/releases/latest/download/podman-desktop-x.x.x.AppImage

# Make it executable
chmod +x podman-desktop-*.AppImage

# Run it
./podman-desktop-*.AppImage
```

### 2.5 Installing Podman (Fedora/RHEL)

```bash
# Fedora - Podman comes pre-installed!
podman --version

# If not, install it
sudo dnf install -y podman

# RHEL 8+
sudo dnf install -y podman

# Set up docker alias
echo 'alias docker=podman' >> ~/.bashrc
source ~/.bashrc

# Optional: Install Podman Desktop
flatpak install -y flathub io.podman_desktop.PodmanDesktop
```

### 2.6 Comprehensive Verification

Run this verification script to ensure everything is working:

**PowerShell (Windows):**
```powershell
Write-Host "=== PODMAN VERIFICATION ===" -ForegroundColor Cyan

# 1. Version check
Write-Host "`n1. Podman Version:" -ForegroundColor Yellow
podman --version

# 2. Machine check (Windows/macOS)
Write-Host "`n2. Podman Machine Status:" -ForegroundColor Yellow
podman machine list

# 3. Run hello-world
Write-Host "`n3. Running hello-world:" -ForegroundColor Yellow
podman run --rm hello-world

# 4. Test port mapping
Write-Host "`n4. Testing port mapping:" -ForegroundColor Yellow
podman run -d -p 9090:80 --name verify-nginx nginx:alpine
Start-Sleep -Seconds 2
try {
    Invoke-WebRequest -Uri "http://localhost:9090" -UseBasicParsing | Select-Object -ExpandProperty StatusCode
    Write-Host "Port mapping: SUCCESS" -ForegroundColor Green
} catch {
    Write-Host "Port mapping: FAILED" -ForegroundColor Red
}
podman stop verify-nginx; podman rm verify-nginx

# 5. Test volume mounting
Write-Host "`n5. Testing volume mounting:" -ForegroundColor Yellow
$testContent = "Hello from Podman!"
$testContent | Out-File -FilePath "$env:TEMP\podman-test.txt"
$result = podman run --rm -v "${env:TEMP}:/test:ro" alpine cat /test/podman-test.txt
if ($result -eq "Hello from Podman!") {
    Write-Host "Volume mounting: SUCCESS" -ForegroundColor Green
} else {
    Write-Host "Volume mounting: FAILED" -ForegroundColor Red
}

Write-Host "`n=== VERIFICATION COMPLETE ===" -ForegroundColor Cyan
```

**Bash (Linux/macOS):**
```bash
#!/bin/bash
echo "=== PODMAN VERIFICATION ==="

# 1. Version check
echo -e "\n1. Podman Version:"
podman --version && echo "✅ Version check passed" || echo "❌ Version check failed"

# 2. Machine check (macOS only)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "\n2. Podman Machine Status:"
    podman machine list
fi

# 3. Run hello-world
echo -e "\n3. Running hello-world:"
podman run --rm hello-world && echo "✅ Hello-world passed" || echo "❌ Hello-world failed"

# 4. Test port mapping
echo -e "\n4. Testing port mapping:"
podman run -d -p 9090:80 --name verify-nginx nginx:alpine
sleep 2
if curl -s http://localhost:9090 > /dev/null; then
    echo "✅ Port mapping passed"
else
    echo "❌ Port mapping failed"
fi
podman stop verify-nginx && podman rm verify-nginx

# 5. Test volume mounting
echo -e "\n5. Testing volume mounting:"
echo "Hello from Podman!" > /tmp/podman-test.txt
if podman run --rm -v /tmp:/test:ro alpine cat /test/podman-test.txt | grep -q "Hello from Podman"; then
    echo "✅ Volume mounting passed"
else
    echo "❌ Volume mounting failed"
fi
rm /tmp/podman-test.txt

echo -e "\n=== VERIFICATION COMPLETE ==="
```

### 2.7 Podman Desktop Tour

Explore the Podman Desktop interface:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PODMAN DESKTOP                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📦 CONTAINERS                                                  │
│     • View running/stopped containers                           │
│     • Start/stop/restart with one click                        │
│     • Open terminal in container                               │
│     • View logs in real-time                                   │
│                                                                 │
│  🖼️ IMAGES                                                      │
│     • Browse local images                                       │
│     • Pull from registries                                     │
│     • Build from Dockerfile                                    │
│     • Push to registries                                       │
│                                                                 │
│  📁 VOLUMES                                                     │
│     • Manage persistent storage                                │
│     • Inspect volume data                                      │
│                                                                 │
│  🏗️ PODS (Unique to Podman!)                                   │
│     • Group containers like Kubernetes                         │
│     • Export as Kubernetes YAML                                │
│                                                                 │
│  ☸️ KUBERNETES                                                  │
│     • Connect to clusters                                      │
│     • Deploy pods directly                                     │
│                                                                 │
│  ⚙️ SETTINGS                                                    │
│     • Machine resources (CPU/Memory)                           │
│     • Registry authentication                                  │
│     • Proxy configuration                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.8 Setting Up the Workshop Environment

Create your organized workspace:

**PowerShell:**
```powershell
# Create workshop directory
$workshopDir = "$HOME\container-workshop"
New-Item -ItemType Directory -Path $workshopDir -Force
Set-Location $workshopDir

# Create structured directories
$dirs = @(
    "01-basics",
    "02-images", 
    "03-containers",
    "04-dockerfile",
    "05-networking",
    "06-volumes",
    "07-multi-container",
    "08-security",
    "projects\ecommerce",
    "projects\api-gateway"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
}

# Create a quick reference file
@"
# Container Workshop - Quick Reference

## Essential Commands (work with both podman and docker)
podman run -d -p 8080:80 nginx        # Run container in background
podman ps                              # List running containers
podman ps -a                           # List all containers
podman logs <container>                # View container logs
podman exec -it <container> bash       # Shell into container
podman stop <container>                # Stop container
podman rm <container>                  # Remove container
podman images                          # List images
podman rmi <image>                     # Remove image
podman build -t name:tag .             # Build image
podman system prune -a                 # Clean up everything

## Workshop Directories
01-basics/        - Getting started exercises
02-images/        - Image management
03-containers/    - Container operations
04-dockerfile/    - Building images
05-networking/    - Container networking
06-volumes/       - Data persistence
07-multi-container/ - Multi-container apps
08-security/      - Security practices
projects/         - Real-world projects
"@ | Out-File -FilePath "README.md" -Encoding UTF8

Write-Host "Workshop environment ready at: $workshopDir" -ForegroundColor Green
Get-ChildItem -Recurse -Depth 1 | Format-Table Name, Mode
```

**Bash:**
```bash
# Create workshop directory
WORKSHOP_DIR="$HOME/container-workshop"
mkdir -p "$WORKSHOP_DIR"
cd "$WORKSHOP_DIR"

# Create structured directories
mkdir -p {01-basics,02-images,03-containers,04-dockerfile,05-networking,06-volumes,07-multi-container,08-security,projects/{ecommerce,api-gateway}}

# Create quick reference
cat > README.md << 'EOF'
# Container Workshop - Quick Reference

## Essential Commands (work with both podman and docker)
podman run -d -p 8080:80 nginx        # Run container in background
podman ps                              # List running containers
podman ps -a                           # List all containers
podman logs <container>                # View container logs
podman exec -it <container> bash       # Shell into container
podman stop <container>                # Stop container
podman rm <container>                  # Remove container
podman images                          # List images
podman rmi <image>                     # Remove image
podman build -t name:tag .             # Build image
podman system prune -a                 # Clean up everything

## Workshop Directories
01-basics/        - Getting started exercises
02-images/        - Image management
03-containers/    - Container operations
04-dockerfile/    - Building images
05-networking/    - Container networking
06-volumes/       - Data persistence
07-multi-container/ - Multi-container apps
08-security/      - Security practices
projects/         - Real-world projects
EOF

echo "Workshop environment ready at: $WORKSHOP_DIR"
tree -L 2 . 2>/dev/null || ls -la
```

### 2.9 VS Code Setup

Install these essential extensions:

1. **Docker** (ms-azuretools.vscode-docker)
   - Syntax highlighting for Dockerfiles
   - Container management sidebar
   - Works with Podman!

2. **Remote - Containers** (ms-vscode-remote.remote-containers)
   - Develop inside containers
   - Dev container support

3. **YAML** (redhat.vscode-yaml)
   - Kubernetes manifest support
   - Docker Compose syntax

**Configure VS Code to use Podman:**

Add to your `settings.json`:
```json
{
    "docker.dockerPath": "podman",
    "docker.environment": {
        "DOCKER_HOST": ""
    }
}
```

### 2.10 ✅ Installation Checkpoint

Verify everything is working:

| Check | Command | Expected |
|-------|---------|----------|
| Podman installed | `podman --version` | Version 4.x+ |
| Machine running | `podman machine list` | Status: Running |
| Can pull images | `podman pull alpine` | Success |
| Can run containers | `podman run alpine echo "OK"` | Prints "OK" |
| Port mapping works | See verification script | HTTP 200 |
| Volumes work | See verification script | File content |
| Docker alias | `docker --version` | Shows podman |

---

## 3. Container Architecture Internals

### 3.1 How Google Runs 4 Billion Containers Per Week

To understand containers deeply, let's see how they work at scale:

```
┌─────────────────────────────────────────────────────────────────┐
│          GOOGLE'S CONTAINER INFRASTRUCTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   📊 Scale: 4 BILLION containers started per week               │
│                                                                 │
│   How it works:                                                 │
│   ┌─────────────────────────────────────────────────────┐      │
│   │                Borg / Kubernetes                     │      │
│   │         (Container Orchestration Layer)              │      │
│   └────────────────────────┬────────────────────────────┘      │
│                            │                                    │
│    ┌─────────────┬─────────┴─────────┬─────────────┐           │
│    │             │                   │             │            │
│    ▼             ▼                   ▼             ▼            │
│  ┌─────┐     ┌─────┐             ┌─────┐     ┌─────┐           │
│  │Node │     │Node │     ...     │Node │     │Node │           │
│  │ 1   │     │ 2   │             │ N-1 │     │ N   │           │
│  └──┬──┘     └──┬──┘             └──┬──┘     └──┬──┘           │
│     │           │                   │           │               │
│     ▼           ▼                   ▼           ▼               │
│  [100s of   [100s of            [100s of   [100s of            │
│   contain.] contain.]            contain.] contain.]           │
│                                                                 │
│   Each node runs containers using:                              │
│   • Linux namespaces (isolation)                                │
│   • cgroups (resource limits)                                   │
│   • Union filesystems (image layers)                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 The Container Runtime Stack

```
┌─────────────────────────────────────────────────────────────────┐
│               CONTAINER RUNTIME HIERARCHY                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   USER LEVEL                                                    │
│   ──────────                                                    │
│   ┌─────────────────────────────────────────────────────┐      │
│   │         CLI: podman / docker / nerdctl              │      │
│   │    What you type: podman run nginx                  │      │
│   └────────────────────────┬────────────────────────────┘      │
│                            │                                    │
│   HIGH-LEVEL RUNTIME       ▼                                    │
│   ──────────────────                                            │
│   ┌─────────────────────────────────────────────────────┐      │
│   │           containerd / CRI-O / Podman               │      │
│   │    • Image pull & storage                           │      │
│   │    • Container lifecycle management                 │      │
│   │    • Network setup                                  │      │
│   │    • Volume mounting                                │      │
│   └────────────────────────┬────────────────────────────┘      │
│                            │                                    │
│   LOW-LEVEL RUNTIME        ▼                                    │
│   ─────────────────                                             │
│   ┌─────────────────────────────────────────────────────┐      │
│   │                    runc / crun                      │      │
│   │    • Creates actual container process               │      │
│   │    • Sets up namespaces                            │      │
│   │    • Configures cgroups                            │      │
│   │    • Starts container PID 1                        │      │
│   └────────────────────────┬────────────────────────────┘      │
│                            │                                    │
│   LINUX KERNEL             ▼                                    │
│   ────────────                                                  │
│   ┌─────────────────────────────────────────────────────┐      │
│   │              Linux Kernel Features                  │      │
│   │   • namespaces: pid, net, mnt, uts, ipc, user      │      │
│   │   • cgroups: cpu, memory, io, pids                 │      │
│   │   • seccomp: syscall filtering                     │      │
│   │   • capabilities: fine-grained permissions         │      │
│   │   • OverlayFS: layered filesystem                  │      │
│   └─────────────────────────────────────────────────────┘      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Linux Namespaces: The Isolation Foundation

Namespaces provide the **illusion of isolation** for containers:

```
┌─────────────────────────────────────────────────────────────────┐
│                    LINUX NAMESPACES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   PID Namespace                                                 │
│   ─────────────                                                 │
│   Host:      Container A:     Container B:                      │
│   PID 1      PID 1            PID 1                            │
│   PID 2      PID 2            PID 2                            │
│   PID 3      ...              ...                              │
│   ...                                                           │
│                                                                 │
│   Each container thinks it has PID 1 (init process)            │
│   Containers cannot see each other's processes                  │
│                                                                 │
│   ─────────────────────────────────────────────────────        │
│                                                                 │
│   NET Namespace                                                 │
│   ─────────────                                                 │
│   Host:              Container A:        Container B:           │
│   eth0: 10.0.0.1     eth0: 172.17.0.2    eth0: 172.17.0.3     │
│   lo: 127.0.0.1      lo: 127.0.0.1       lo: 127.0.0.1        │
│                                                                 │
│   Each container has its own network stack                      │
│                                                                 │
│   ─────────────────────────────────────────────────────        │
│                                                                 │
│   MNT Namespace                                                 │
│   ─────────────                                                 │
│   Container sees only its own filesystem tree:                  │
│   /                                                             │
│   ├── bin/  (from image)                                       │
│   ├── etc/  (from image)                                       │
│   ├── app/  (your code)                                        │
│   └── data/ (mounted volume)                                   │
│                                                                 │
│   Cannot access host filesystem unless explicitly mounted       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.4 cgroups: Resource Control

cgroups prevent any container from hogging resources:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CGROUPS IN ACTION                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Total Host Resources: 8 CPUs, 32GB RAM                        │
│   ─────────────────────────────────────────────────            │
│                                                                 │
│   Container A:        Container B:        Container C:          │
│   ┌─────────────┐    ┌─────────────┐     ┌─────────────┐       │
│   │ CPU: 2      │    │ CPU: 4      │     │ CPU: 2      │       │
│   │ Memory: 4GB │    │ Memory: 8GB │     │ Memory: 2GB │       │
│   │ PID limit:  │    │ PID limit:  │     │ User quota:  │      │
│   │   100       │    │   500       │     │   200       │       │
│   └─────────────┘    └─────────────┘     └─────────────┘       │
│                                                                 │
│   If Container A tries to use more:                             │
│   - More CPU → throttled                                        │
│   - More memory → OOM killed                                    │
│   - More PIDs → fork fails                                      │
│                                                                 │
│   Demonstrating resource limits:                                │
│   podman run --memory=512m --cpus=1 nginx                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.5 Image Layers Deep Dive

Understanding layers is crucial for optimization:

```
┌─────────────────────────────────────────────────────────────────┐
│                 IMAGE LAYER ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Dockerfile:                      Image Layers:                │
│   ───────────                      ─────────────                │
│                                                                 │
│   FROM python:3.11-slim      ┌─────────────────┐               │
│                              │ Layer 1: 120MB  │ ← base image  │
│                              │ debian + python │               │
│   ─────────────────────      └────────┬────────┘               │
│   WORKDIR /app                       │                         │
│                              ┌───────┴────────┐                │
│                              │ Layer 2: 0 KB  │ ← metadata     │
│                              │ workdir /app   │                │
│   ─────────────────────      └────────┬───────┘                │
│   COPY requirements.txt .            │                         │
│                              ┌───────┴────────┐                │
│                              │ Layer 3: 2 KB  │ ← your deps   │
│                              │ requirements   │                │
│   ─────────────────────      └────────┬───────┘                │
│   RUN pip install -r                 │                         │
│       requirements.txt       ┌───────┴────────┐                │
│                              │ Layer 4: 50MB  │ ← pip install  │
│                              │ site-packages  │                │
│   ─────────────────────      └────────┬───────┘                │
│   COPY . .                           │                         │
│                              ┌───────┴────────┐                │
│                              │ Layer 5: 5 MB  │ ← your code    │
│                              │ application    │                │
│   ─────────────────────      └────────┬───────┘                │
│   CMD ["python", "app.py"]           │                         │
│                              ┌───────┴────────┐                │
│                              │ Layer 6: 0 KB  │ ← startup cmd  │
│                              │ metadata only  │                │
│                              └────────────────┘                │
│                                                                 │
│   Total: ~177MB (5 layers with actual content)                 │
│                                                                 │
│   KEY INSIGHT: Change requirements.txt → layers 4,5,6 rebuilt  │
│               Change code only → only layer 5,6 rebuilt         │
│               Order matters for caching!                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.6 Copy-on-Write (CoW) Mechanism

```
┌─────────────────────────────────────────────────────────────────┐
│                  COPY-ON-WRITE EXPLAINED                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   100 containers running the same nginx image:                  │
│                                                                 │
│   Container 1 ─┐                                                │
│   Container 2 ─┤                                                │
│   Container 3 ─┼──▶ SHARED IMAGE LAYERS (read-only)            │
│   ...         │     ~150MB on disk (not 15GB!)                  │
│   Container 100┘                                                │
│                                                                 │
│   When Container 5 modifies /etc/nginx/nginx.conf:             │
│                                                                 │
│   ┌─────────────────────────────────────────────────────┐      │
│   │                   Container 5                        │      │
│   │   ┌────────────────────────────────┐                │      │
│   │   │ WRITABLE LAYER (this container)│                │      │
│   │   │ /etc/nginx/nginx.conf (COPIED)│◀─── modified   │      │
│   │   └────────────────────────────────┘                │      │
│   └─────────────────────┬───────────────────────────────┘      │
│                         │                                       │
│   ┌─────────────────────▼───────────────────────────────┐      │
│   │              SHARED IMAGE LAYERS                     │      │
│   │   /etc/nginx/nginx.conf (ORIGINAL) ← unchanged      │      │
│   │   Other containers still see original                │      │
│   └─────────────────────────────────────────────────────┘      │
│                                                                 │
│   Benefits:                                                     │
│   • 100 containers share 150MB base (not 15GB)                 │
│   • Container changes are isolated                              │
│   • Fast container startup (no copying)                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.7 🔬 Lab: Exploring Container Internals

**Exercise 3.1: Namespace Exploration**

```bash
# Run a container in the background
podman run -d --name ns-demo nginx:alpine
sleep 2

# Get the container's PID on the host (Linux only)
# For Podman, use podman inspect
podman inspect ns-demo --format '{{.State.Pid}}'

# See processes from inside the container
podman exec ns-demo ps aux
# Notice: Container sees PID 1 as nginx master

# See hostname isolation
podman exec ns-demo hostname
# Different from host!

# See network isolation
podman exec ns-demo ip addr
# Container has its own network interface

# Compare with another container
podman run -d --name ns-demo2 nginx:alpine
podman exec ns-demo hostname
podman exec ns-demo2 hostname
# Different hostnames!

# Cleanup
podman rm -f ns-demo ns-demo2
```

**Exercise 3.2: cgroups Resource Limits**

```bash
# Run container with strict memory limit
podman run -d --name mem-test --memory=100m nginx:alpine

# Check the limits applied
podman stats mem-test --no-stream

# Try to exceed the limit (this container will be OOM-killed)
podman run --rm --memory=50m alpine sh -c '
    echo "Allocating memory..."
    # Try to allocate 100MB
    dd if=/dev/zero of=/tmp/bigfile bs=1M count=100 2>&1
' || echo "Container was OOM-killed as expected!"

# CPU limit demonstration
podman run -d --name cpu-test --cpus=0.5 nginx:alpine
podman stats cpu-test --no-stream
# Notice: CPU limit is 50%

# Combined limits
podman run -d --name limited \
  --memory=256m \
  --cpus=1 \
  --pids-limit=50 \
  nginx:alpine

podman inspect limited --format '
Memory: {{.HostConfig.Memory}} bytes
CPUs: {{.HostConfig.NanoCpus}} nanocpus  
PIDs: {{.HostConfig.PidsLimit}}'

# Cleanup
podman rm -f mem-test cpu-test limited
```

**Exercise 3.3: Layer Visualization**

```bash
# Pull images and examine layers
podman pull python:3.11
podman pull python:3.11-slim
podman pull python:3.11-alpine

# Compare sizes
echo "=== Image Size Comparison ==="
podman images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}" | grep python

# View layer history
echo -e "\n=== Python Slim Layers ==="
podman history python:3.11-slim --format "table {{.Size}}\t{{.CreatedBy}}" | head -10

echo -e "\n=== Python Alpine Layers ==="
podman history python:3.11-alpine --format "table {{.Size}}\t{{.CreatedBy}}" | head -10

# Count layers
echo -e "\n=== Layer Count ==="
echo "python:3.11 layers: $(podman history python:3.11 -q | wc -l)"
echo "python:3.11-slim layers: $(podman history python:3.11-slim -q | wc -l)"
echo "python:3.11-alpine layers: $(podman history python:3.11-alpine -q | wc -l)"

# Check disk usage
echo -e "\n=== Disk Usage ==="
podman system df
```

**Exercise 3.4: Copy-on-Write Demonstration**

```bash
# Start container
podman run -d --name cow-demo alpine sleep 3600

# Check initial size
echo "Initial container size:"
podman ps -s --format "table {{.Names}}\t{{.Size}}"

# Create a 50MB file inside the container
podman exec cow-demo dd if=/dev/zero of=/bigfile bs=1M count=50

# Check size again - container layer grew!
echo -e "\nAfter adding 50MB file:"
podman ps -s --format "table {{.Names}}\t{{.Size}}"

# The base image is unchanged
echo -e "\nBase image size (unchanged):"
podman images alpine

# Start another container from same image - starts instantly
time podman run --rm alpine echo "I started fast because I share layers!"

# Cleanup
podman rm -f cow-demo
```

### 3.8 ✅ Knowledge Check: Architecture

| Question | Your Answer |
|----------|-------------|
| What Linux feature provides process isolation? | ☐ Namespaces |
| What prevents a container from using all host memory? | ☐ cgroups |
| Why do 100 nginx containers not need 100x the disk space? | ☐ Shared layers |
| What happens when a container modifies a base image file? | ☐ Copy-on-Write |
| Why does changing code rebuild fewer layers than changing dependencies? | ☐ Layer ordering |

---

## 4. Mastering Container Images

### 4.1 The Spotify Image Optimization Strategy

Spotify reduced their container images from **1.2GB to 45MB**:

```
┌─────────────────────────────────────────────────────────────────┐
│           SPOTIFY'S IMAGE OPTIMIZATION JOURNEY                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   BEFORE                        AFTER                           │
│   ──────                        ─────                           │
│   Base: Ubuntu 20.04            Base: distroless/java           │
│   JDK: Full Oracle JDK          JDK: JRE only                   │
│   Build tools: included         Build tools: multi-stage        │
│   Debug tools: included         Debug tools: separate image     │
│                                                                 │
│   Result:                                                       │
│   ┌──────────────────────┐     ┌──────────────────────┐        │
│   │      1.2 GB          │     │       45 MB          │        │
│   │                      │ ──▶ │                      │        │
│   │ 15 sec pull time     │     │  1 sec pull time     │        │
│   │ Large attack surface │     │ Minimal CVEs         │        │
│   └──────────────────────┘     └──────────────────────┘        │
│                                                                 │
│   Impact: 96% smaller, 15x faster deployments                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Image Search & Selection Strategy

**Finding the Right Base Image:**

```bash
# Search official images
podman search --filter=is-official=true python

# Search by stars (popularity)
podman search --filter=stars=1000 node

# Compare image variants
podman pull python:3.11
podman pull python:3.11-slim  
podman pull python:3.11-alpine

# See the size difference
podman images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}" | grep python
```

**Base Image Selection Guide:**

| Base | Size | Use Case | Trade-offs |
|------|------|----------|------------|
| **alpine** | ~5MB | APIs, microservices | musl libc (some compatibility issues) |
| **slim** | ~80MB | Most applications | Good balance |
| **bullseye/bookworm** | ~150MB | Full Debian | All packages available |
| **distroless** | ~20MB | Production | No shell, minimal |
| **scratch** | 0MB | Go binaries | Nothing included |

### 4.3 Professional Image Operations

```bash
# ═══════════════════════════════════════════════════
# PULLING IMAGES
# ═══════════════════════════════════════════════════

# Basic pull
podman pull nginx:1.25-alpine

# Pull specific platform (for cross-platform builds)
podman pull --platform linux/amd64 nginx:alpine
podman pull --platform linux/arm64 nginx:alpine

# Pull by exact digest (immutable, reproducible)
podman pull nginx@sha256:abc123...

# Pull from alternative registries
podman pull ghcr.io/owner/image:tag
podman pull quay.io/organization/image:tag
podman pull mcr.microsoft.com/dotnet/aspnet:8.0

# ═══════════════════════════════════════════════════
# INSPECTING IMAGES
# ═══════════════════════════════════════════════════

# Full JSON inspection
podman inspect nginx:alpine

# Specific fields
podman inspect nginx:alpine --format '{{.Config.ExposedPorts}}'
podman inspect nginx:alpine --format '{{.Config.Env}}'
podman inspect nginx:alpine --format '{{.Os}}/{{.Architecture}}'

# Image labels (metadata)
podman inspect nginx:alpine --format '{{json .Config.Labels}}' | jq

# View history (reverse-engineer Dockerfile)
podman history nginx:alpine
podman history nginx:alpine --no-trunc

# Security scanning (find vulnerabilities)
# Requires trivy: https://github.com/aquasecurity/trivy
# trivy image nginx:alpine

# ═══════════════════════════════════════════════════
# TAGGING STRATEGY
# ═══════════════════════════════════════════════════

# Semantic versioning tags
podman tag myapp:latest myapp:1.0.0
podman tag myapp:latest myapp:1.0
podman tag myapp:latest myapp:1

# Environment tags  
podman tag myapp:latest myapp:dev
podman tag myapp:1.0.0 myapp:staging
podman tag myapp:1.0.0 myapp:production

# Git SHA tags (CI/CD best practice)
podman tag myapp:latest myapp:$(git rev-parse --short HEAD)

# ═══════════════════════════════════════════════════
# CLEANUP & MAINTENANCE
# ═══════════════════════════════════════════════════

# Remove specific image
podman rmi nginx:alpine

# Remove all unused images
podman image prune -a

# Full system cleanup
podman system prune -a --volumes

# Check disk usage
podman system df
podman system df -v  # Verbose
```

### 4.4 🔬 Lab: Image Mastery

**Exercise 4.1: Base Image Comparison (15 min)**

```bash
cd ~/container-workshop/02-images

# Pull multiple variants
echo "Pulling Python variants..."
podman pull python:3.11
podman pull python:3.11-slim
podman pull python:3.11-alpine

# Create comparison report
cat > image-comparison.md << 'EOF'
# Python Base Image Comparison

| Variant | Size | Layers | Best For |
|---------|------|--------|----------|
EOF

for tag in "3.11" "3.11-slim" "3.11-alpine"; do
    size=$(podman images python:$tag --format "{{.Size}}")
    layers=$(podman history python:$tag -q | wc -l)
    echo "| python:$tag | $size | $layers | |" >> image-comparison.md
done

cat image-comparison.md

# Test compatibility - alpine uses musl
echo -e "\n=== Testing Alpine compatibility ==="
podman run --rm python:3.11-alpine python -c "
import sys
print(f'Python: {sys.version}')
print(f'Platform: {sys.platform}')
"
```

**Exercise 4.2: Security Analysis (15 min)**

```bash
# Check image for known issues
echo "=== Inspecting Image Security ==="

# View image age
podman inspect python:3.11-slim --format '{{.Created}}'

# Check for setuid binaries (security risk)
podman run --rm python:3.11-slim find / -perm /4000 2>/dev/null

# Count installed packages
podman run --rm python:3.11-slim dpkg --list | wc -l
podman run --rm python:3.11-alpine apk list --installed | wc -l

# Check running user
podman run --rm python:3.11-slim whoami

echo -e "\n=== Best Practice: Always use specific tags! ==="
echo "BAD:  python:latest (changes unpredictably)"
echo "GOOD: python:3.11.7-slim-bookworm (specific)"
```

**Exercise 4.3: Transfer Images Without Registry (10 min)**

```bash
# Scenario: Transfer image to air-gapped server

# Save image to file
podman save nginx:alpine | gzip > nginx-alpine.tar.gz
ls -lh nginx-alpine.tar.gz

# See what's inside
tar tzf nginx-alpine.tar.gz | head -20

# Load it back (simulating different machine)
podman rmi nginx:alpine
podman load < nginx-alpine.tar.gz
podman images | grep nginx

# Cleanup
rm nginx-alpine.tar.gz
```

### 4.5 ✅ Image Mastery Checkpoint

| Skill | Demonstrate |
|-------|-------------|
| Find official images | `podman search --filter=is-official=true <name>` |
| Compare image sizes | `podman images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}"` |
| View layer history | `podman history <image>` |
| Create semantic tags | `podman tag myapp:latest myapp:1.0.0` |
| Export image | `podman save <image> \| gzip > image.tar.gz` |

---

## 5. Running Production Containers

### 5.1 Amazon's Container Deployment Patterns

Amazon runs millions of containers for their e-commerce platform:

```
┌─────────────────────────────────────────────────────────────────┐
│            AMAZON'S CONTAINER PATTERNS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Pattern 1: ALWAYS EXPLICIT                                    │
│   ─────────────────────────                                     │
│                                                                 │
│   ❌ BAD:  podman run nginx                                     │
│   ✅ GOOD: podman run \                                         │
│              --name product-service \             # Named        │
│              --memory 512m \                      # Memory limit │
│              --cpus 1 \                           # CPU limit    │
│              --publish 8080:80 \                  # Port mapping │
│              --restart unless-stopped \           # Auto-restart │
│              --health-cmd "curl -f localhost" \   # Health check │
│              --detach \                           # Background   │
│              nginx:1.25.3-alpine                  # Specific tag │
│                                                                 │
│   Pattern 2: IMMUTABLE INFRASTRUCTURE                           │
│   ───────────────────────────────────                           │
│                                                                 │
│   • Never modify running containers                             │
│   • Build new image → Deploy new container                      │
│   • Roll back = run previous image version                      │
│                                                                 │
│   Pattern 3: ONE PROCESS PER CONTAINER                          │
│   ─────────────────────────────────────                         │
│                                                                 │
│   • Web server: one container                                   │
│   • Database: separate container                                │
│   • Cache: separate container                                   │
│   • Allows independent scaling                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 The Production-Ready `podman run` Command

```bash
# ═══════════════════════════════════════════════════
# COMPLETE PRODUCTION CONTAINER LAUNCH
# ═══════════════════════════════════════════════════

podman run \
  # IDENTIFICATION
  --name api-gateway \                    # Human-readable name
  --hostname api-gateway \                # Hostname inside container
  
  # RESOURCE LIMITS (prevent runaway processes)
  --memory 512m \                         # Memory limit
  --memory-reservation 256m \             # Soft limit  
  --cpus 2 \                              # CPU limit
  --pids-limit 100 \                      # Prevent fork bombs
  
  # NETWORKING
  --publish 8080:8080 \                   # Map port
  --network app-network \                 # Custom network
  
  # ENVIRONMENT
  --env NODE_ENV=production \             # Environment variable
  --env-file .env.production \            # From file
  
  # STORAGE
  --volume app-data:/data:rw \            # Named volume
  --volume ./config:/config:ro \          # Read-only bind mount
  
  # SECURITY
  --user 1000:1000 \                      # Run as non-root
  --read-only \                           # Read-only filesystem
  --cap-drop ALL \                        # Drop all capabilities
  --security-opt no-new-privileges \      # Prevent privilege escalation
  
  # RELIABILITY
  --restart unless-stopped \              # Auto-restart policy
  --health-cmd "curl -f http://localhost:8080/health" \
  --health-interval 30s \
  --health-timeout 10s \
  --health-retries 3 \
  
  # RUN DETACHED
  --detach \
  
  # IMAGE (always use specific tag)
  mycompany/api-gateway:1.2.3
```

### 5.3 Container Lifecycle Management

```
┌─────────────────────────────────────────────────────────────────┐
│                 CONTAINER LIFECYCLE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────┐  podman create  ┌─────────┐                      │
│   │  Image  │────────────────▶│ Created │                      │
│   └─────────┘                 └────┬────┘                      │
│                                    │ podman start               │
│                                    ▼                            │
│                    podman pause ┌─────────┐                     │
│                         ┌──────▶│ Running │◀──────┐            │
│                         │       └────┬────┘       │             │
│                         │            │            │             │
│                     podman          │        podman             │
│                     unpause         │        restart            │
│                         │            │            │             │
│                         │       ┌────▼────┐      │             │
│                         └───────│ Paused  │──────┘             │
│                                 └────┬────┘                     │
│                                      │ podman stop               │
│                                      │ (or process exits)        │
│                                      ▼                          │
│                                 ┌─────────┐                     │
│                                 │ Stopped │                     │
│                                 └────┬────┘                     │
│                                      │ podman rm                 │
│                                      ▼                          │
│                                 ┌─────────┐                     │
│                                 │ Removed │                     │
│                                 └─────────┘                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

```bash
# Lifecycle commands
podman create --name myapp nginx:alpine  # Create but don't start
podman start myapp                        # Start container
podman pause myapp                        # Freeze processes
podman unpause myapp                     # Resume processes
podman stop myapp                         # Graceful shutdown (SIGTERM)
podman kill myapp                         # Force kill (SIGKILL)
podman restart myapp                      # Stop + start
podman rm myapp                           # Remove stopped container
podman rm -f myapp                        # Force remove running container
```

### 5.4 🔬 Lab: Running Containers Like a Pro

**Exercise 5.1: Production-Style Container Launch (15 min)**

```bash
cd ~/container-workshop/03-containers

# Create a production-ready nginx deployment
podman run \
  --name prod-nginx \
  --hostname web-server \
  --memory 256m \
  --cpus 0.5 \
  --publish 8080:80 \
  --env NGINX_VERSION=1.25 \
  --read-only \
  --tmpfs /var/run:rw \
  --tmpfs /var/cache/nginx:rw \
  --health-cmd "curl -sf http://localhost/ || exit 1" \
  --health-interval 10s \
  --restart unless-stopped \
  --detach \
  nginx:1.25-alpine

# Verify it's running properly
echo "=== Container Status ==="
podman ps --filter name=prod-nginx

echo -e "\n=== Health Status ==="
sleep 15  # Wait for health check
podman inspect prod-nginx --format '{{.State.Health.Status}}'

echo -e "\n=== Resource Usage ==="
podman stats --no-stream prod-nginx

echo -e "\n=== Test HTTP ==="
curl -s http://localhost:8080 | head -5

# Check the enforced limits
echo -e "\n=== Enforced Limits ==="
podman inspect prod-nginx --format '
Memory Limit: {{.HostConfig.Memory}}
CPU Limit: {{.HostConfig.NanoCpus}} nanocpus
Read-Only Root: {{.HostConfig.ReadonlyRootfs}}'

# Cleanup
podman rm -f prod-nginx
```

**Exercise 5.2: Environment Variables (10 min)**

```bash
# Method 1: -e flag
podman run --rm \
  -e DATABASE_URL="postgres://localhost:5432/mydb" \
  -e API_KEY="secret123" \
  alpine printenv | grep -E "(DATABASE|API)"

# Method 2: --env-file
cat > app.env << 'EOF'
DATABASE_URL=postgres://localhost:5432/mydb
API_KEY=secret123
DEBUG=true
LOG_LEVEL=info
EOF

podman run --rm --env-file app.env alpine printenv | grep -E "(DATABASE|API|DEBUG|LOG)"

# Method 3: Pass from host
export HOST_VAR="from-host"
podman run --rm -e HOST_VAR alpine printenv HOST_VAR

rm app.env
```

**Exercise 5.3: Resource Limits (10 min)**

```bash
# Memory limit test
echo "=== Memory Limit Demo ==="
podman run --rm --memory=50m alpine sh -c '
echo "Memory limit: 50MB"
# Try to allocate 60MB (will fail)
dd if=/dev/zero of=/tmp/test bs=1M count=60 2>&1 || echo "Failed: OOM limit"
'

# CPU limit test  
echo -e "\n=== CPU Limit Demo ==="
# Run CPU stress test with limit
podman run --rm --cpus=0.5 --name cpu-test alpine sh -c '
echo "Running with 0.5 CPU limit"
# Calculate pi to stress CPU
time (i=0; while [ $i -lt 1000 ]; do echo "scale=10; 4*a(1)" | bc -l > /dev/null 2>&1 || true; i=$((i+1)); done)
' 2>&1 | head -5

# Show container with tight limits
echo -e "\n=== Tightly Limited Container ==="
podman run -d \
  --name limited-app \
  --memory=128m \
  --cpus=0.25 \
  --pids-limit=20 \
  nginx:alpine

podman stats --no-stream limited-app
podman rm -f limited-app
```

### 5.5 ✅ Container Operations Checkpoint

| Command | Purpose |
|---------|---------|
| `podman run -d` | Run detached (background) |
| `podman run --rm` | Auto-remove when stopped |
| `podman run -it` | Interactive with terminal |
| `podman run -p 8080:80` | Map host:container port |
| `podman run -e VAR=value` | Set environment variable |
| `podman run --memory=512m` | Limit memory |
| `podman run --cpus=2` | Limit CPU |
| `podman stop/start/restart` | Lifecycle control |

---

## 6. Crafting Perfect Dockerfiles

### 6.1 Goldman Sachs Security Standards

Financial services require the highest security standards:

```
┌─────────────────────────────────────────────────────────────────┐
│         GOLDMAN SACHS DOCKERFILE REQUIREMENTS                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ✅ REQUIRED                        ❌ PROHIBITED              │
│   ─────────                          ────────────               │
│   • Specific base image tags         • :latest tags             │
│   • Non-root user                    • Root execution           │
│   • Multi-stage builds               • Build tools in prod      │
│   • No secrets in image              • Hardcoded credentials    │
│   • Minimal packages                 • Unnecessary packages     │
│   • Health checks                    • No monitoring            │
│   • Labels (metadata)                • Anonymous images         │
│   • Fixed package versions           • Unpinned dependencies    │
│                                                                 │
│   Their standard Dockerfile template:                           │
│                                                                 │
│   # syntax=docker/dockerfile:1.4                                │
│   FROM base:version AS builder                                  │
│   # Build stage...                                              │
│                                                                 │
│   FROM distroless/base-debian12:nonroot                        │
│   LABEL org.opencontainers.image.source="..."                  │
│   COPY --from=builder --chown=nonroot:nonroot /app /app        │
│   USER nonroot                                                  │
│   HEALTHCHECK ...                                               │
│   ENTRYPOINT ["/app/binary"]                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Dockerfile Best Practices: Complete Guide

```dockerfile
# ═══════════════════════════════════════════════════
# PRODUCTION PYTHON DOCKERFILE - COMPLETE EXAMPLE
# ═══════════════════════════════════════════════════

# Enable BuildKit features
# syntax=docker/dockerfile:1.4

# ───────────────────────────────────────────────────
# STAGE 1: Build Stage
# ───────────────────────────────────────────────────
FROM python:3.11-slim-bookworm AS builder

# Labels for build stage
LABEL stage="builder"

# Set environment variables for build
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
# (This layer is cached unless requirements.txt changes)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ───────────────────────────────────────────────────
# STAGE 2: Production Stage
# ───────────────────────────────────────────────────
FROM python:3.11-slim-bookworm AS production

# OCI-compliant labels
LABEL org.opencontainers.image.title="My API Service" \
      org.opencontainers.image.description="Production API service" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.vendor="MyCompany" \
      org.opencontainers.image.source="https://github.com/mycompany/api" \
      org.opencontainers.image.authors="team@mycompany.com"

# Runtime environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    APP_HOME=/app \
    APP_USER=appuser \
    APP_GROUP=appgroup

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create non-root user
RUN groupadd --gid 1000 ${APP_GROUP} \
    && useradd --uid 1000 --gid ${APP_GROUP} --shell /bin/bash --create-home ${APP_USER}

# Set up application directory
WORKDIR ${APP_HOME}

# Copy Python packages from builder
COPY --from=builder /root/.local /home/${APP_USER}/.local

# Copy application code
COPY --chown=${APP_USER}:${APP_GROUP} ./src ./src
COPY --chown=${APP_USER}:${APP_GROUP} ./config ./config

# Update PATH for user packages
ENV PATH=/home/${APP_USER}/.local/bin:$PATH

# Switch to non-root user
USER ${APP_USER}

# Expose port (documentation)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8000/health || exit 1

# Default command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "src.main:app"]
```

### 6.3 The Golden Rules of Dockerfile Optimization

```
┌─────────────────────────────────────────────────────────────────┐
│              DOCKERFILE OPTIMIZATION RULES                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   RULE 1: ORDER MATTERS FOR CACHING                            │
│   ──────────────────────────────────                            │
│                                                                 │
│   ❌ BAD (busts cache on every code change):                    │
│   COPY . .                                                      │
│   RUN pip install -r requirements.txt                          │
│                                                                 │
│   ✅ GOOD (dependencies cached unless changed):                 │
│   COPY requirements.txt .                                       │
│   RUN pip install -r requirements.txt                          │
│   COPY . .                                                      │
│                                                                 │
│   ─────────────────────────────────────────────────            │
│                                                                 │
│   RULE 2: MINIMIZE LAYERS                                       │
│   ───────────────────────                                       │
│                                                                 │
│   ❌ BAD (3 layers):                                            │
│   RUN apt-get update                                           │
│   RUN apt-get install -y curl                                  │
│   RUN rm -rf /var/lib/apt/lists/*                              │
│                                                                 │
│   ✅ GOOD (1 layer):                                            │
│   RUN apt-get update \                                         │
│       && apt-get install -y --no-install-recommends curl \     │
│       && rm -rf /var/lib/apt/lists/*                           │
│                                                                 │
│   ─────────────────────────────────────────────────            │
│                                                                 │
│   RULE 3: USE SPECIFIC TAGS                                     │
│   ─────────────────────────                                     │
│                                                                 │
│   ❌ BAD:  FROM python:latest                                   │
│   ❌ MEH:  FROM python:3.11                                     │
│   ✅ GOOD: FROM python:3.11.7-slim-bookworm                    │
│                                                                 │
│   ─────────────────────────────────────────────────            │
│                                                                 │
│   RULE 4: USE .dockerignore                                     │
│   ─────────────────────────                                     │
│                                                                 │
│   # .dockerignore                                               │
│   .git                                                          │
│   .env                                                          │
│   __pycache__                                                   │
│   node_modules                                                  │
│   *.md                                                          │
│   tests/                                                        │
│   Dockerfile                                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.4 🔬 Lab: Building Production Images

**Exercise 6.1: Build a Production Python API (20 min)**

```bash
cd ~/container-workshop/04-dockerfile
mkdir -p python-api && cd python-api

# Create the application
cat > app.py << 'EOF'
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'service': 'Container Workshop API',
        'version': os.environ.get('APP_VERSION', '1.0.0'),
        'hostname': socket.gethostname()
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
EOF

cat > requirements.txt << 'EOF'
flask==3.0.0
gunicorn==21.2.0
EOF

# Create production Dockerfile
cat > Dockerfile << 'EOF'
# Multi-stage production build
FROM python:3.11-slim-bookworm AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim-bookworm
LABEL maintainer="workshop@example.com"
LABEL version="1.0.0"

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser/app

# Copy dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appuser app.py .

# Set environment
ENV PATH=/home/appuser/.local/bin:$PATH \
    APP_VERSION=1.0.0 \
    PYTHONUNBUFFERED=1

USER appuser
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
EOF

# Create .dockerignore
cat > .dockerignore << 'EOF'
__pycache__
*.pyc
.git
.env
README.md
EOF

# Build
echo "Building production image..."
podman build -t workshop-api:1.0.0 .

# Check size
echo -e "\n=== Image Size ==="
podman images workshop-api:1.0.0

# Run
podman run -d -p 8000:8000 --name api-test workshop-api:1.0.0

# Test
sleep 3
echo -e "\n=== Testing API ==="
curl -s http://localhost:8000/
echo ""
curl -s http://localhost:8000/health
echo ""

# Verify non-root
echo -e "\n=== Verify Non-Root User ==="
podman exec api-test whoami

# Cleanup
podman rm -f api-test
```

**Exercise 6.2: Multi-Stage Build Comparison (15 min)**

```bash
cd ~/container-workshop/04-dockerfile
mkdir -p go-app && cd go-app

# Create simple Go application
cat > main.go << 'EOF'
package main

import (
    "encoding/json"
    "log"
    "net/http"
    "os"
)

type Response struct {
    Message  string `json:"message"`
    Hostname string `json:"hostname"`
}

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        hostname, _ := os.Hostname()
        resp := Response{
            Message:  "Hello from Go in a container!",
            Hostname: hostname,
        }
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(resp)
    })
    
    log.Println("Server starting on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
EOF

# Single-stage Dockerfile (BAD)
cat > Dockerfile.single << 'EOF'
FROM golang:1.21
WORKDIR /app
COPY main.go .
RUN go build -o server main.go
EXPOSE 8080
CMD ["./server"]
EOF

# Multi-stage Dockerfile (GOOD)
cat > Dockerfile.multi << 'EOF'
# Build stage
FROM golang:1.21-alpine AS builder
WORKDIR /build
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o server main.go

# Production stage - using scratch (zero-size base)
FROM scratch
COPY --from=builder /build/server /server
EXPOSE 8080
ENTRYPOINT ["/server"]
EOF

# Build both
echo "Building single-stage (includes entire Go toolchain)..."
podman build -f Dockerfile.single -t go-single:1.0 .

echo -e "\nBuilding multi-stage (minimal binary only)..."
podman build -f Dockerfile.multi -t go-multi:1.0 .

# Compare
echo -e "\n=== SIZE COMPARISON ==="
podman images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}" | grep go-

# Test multi-stage
podman run -d -p 8080:8080 --name go-test go-multi:1.0
sleep 1
curl -s http://localhost:8080/
podman rm -f go-test

echo -e "\n=== SAVINGS ==="
single_size=$(podman images go-single:1.0 --format "{{.Size}}")
multi_size=$(podman images go-multi:1.0 --format "{{.Size}}")
echo "Single-stage: $single_size"
echo "Multi-stage: $multi_size"
echo "Reduction: ~99%!"
```

### 6.5 ✅ Dockerfile Mastery Checkpoint

| Best Practice | Applied? |
|--------------|----------|
| Specific base image tag | ☐ `python:3.11.7-slim-bookworm` |
| Multi-stage build | ☐ Separate builder and production stages |
| Non-root user | ☐ `USER appuser` |
| Optimized layer order | ☐ COPY requirements before code |
| .dockerignore | ☐ Excludes .git, tests, etc. |
| Health check | ☐ `HEALTHCHECK CMD ...` |
| Labels | ☐ `LABEL version="1.0"` |

---

## 7. Container Operations & Debugging

### 7.1 Production Debugging Toolkit

```bash
# ═══════════════════════════════════════════════════
# LOGS
# ═══════════════════════════════════════════════════

# View logs
podman logs <container>

# Follow logs (live)
podman logs -f <container>

# Last N lines
podman logs --tail 100 <container>

# With timestamps
podman logs -t <container>

# Since time
podman logs --since 5m <container>
podman logs --since "2024-01-01T00:00:00" <container>

# ═══════════════════════════════════════════════════
# EXEC - Run Commands in Containers
# ═══════════════════════════════════════════════════

# Interactive shell
podman exec -it <container> /bin/bash
podman exec -it <container> /bin/sh  # For Alpine

# Run single command
podman exec <container> ls -la /app

# Run as root (in rootless container)
podman exec -u 0 <container> whoami

# With environment variable
podman exec -e DEBUG=true <container> python debug.py

# ═══════════════════════════════════════════════════
# INSPECT & DEBUG
# ═══════════════════════════════════════════════════

# Full inspection
podman inspect <container>

# Specific fields
podman inspect <container> --format '{{.State.Status}}'
podman inspect <container> --format '{{.NetworkSettings.IPAddress}}'
podman inspect <container> --format '{{json .Config.Env}}'

# View processes
podman top <container>

# File changes from image
podman diff <container>

# ═══════════════════════════════════════════════════
# COPY FILES
# ═══════════════════════════════════════════════════

# Copy from container to host
podman cp <container>:/app/logs ./logs

# Copy from host to container
podman cp ./config.json <container>:/app/config.json

# ═══════════════════════════════════════════════════
# STATS & MONITORING
# ═══════════════════════════════════════════════════

# Real-time stats
podman stats

# One-time snapshot
podman stats --no-stream

# Formatted output
podman stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

### 7.2 🔬 Lab: Debugging Containers

**Exercise 7.1: Debug a Failing Container (15 min)**

```bash
cd ~/container-workshop/05-debugging

# Create a buggy application
cat > broken-app.py << 'EOF'
import os
import sys

# BUG 1: Missing environment variable
database_url = os.environ['DATABASE_URL']  # Will crash if not set

# BUG 2: Wrong port
port = 9999  # But Dockerfile exposes 8000

print(f"Starting on port {port}")
EOF

cat > Dockerfile << 'EOF'
FROM python:3.11-alpine
WORKDIR /app
COPY broken-app.py .
EXPOSE 8000
CMD ["python", "broken-app.py"]
EOF

# Build and try to run
podman build -t broken-app:1.0 .
echo "=== Attempting to run (will fail) ==="
podman run --name broken broken-app:1.0 2>&1 || true

# Debug: Check logs
echo -e "\n=== Container Logs ==="
podman logs broken 2>&1 || echo "Container failed to start"

# Debug: Inspect exit code
echo -e "\n=== Exit Information ==="
podman inspect broken --format '
Status: {{.State.Status}}
Exit Code: {{.State.ExitCode}}
Error: {{.State.Error}}'

# Debug: Run interactively to investigate
echo -e "\n=== Interactive Debug Session ==="
podman run --rm -it --entrypoint /bin/sh broken-app:1.0 -c '
echo "Python version:"
python --version
echo ""
echo "Environment variables:"
env | head -10
echo ""
echo "File contents:"
cat broken-app.py
'

# Fix: Provide the required environment variable
echo -e "\n=== Running with fix ==="
podman rm broken 2>/dev/null
podman run --rm -e DATABASE_URL="postgres://localhost/db" broken-app:1.0

echo "Container ran but on wrong port - check EXPOSE vs actual port in code!"
```

**Exercise 7.2: Performance Analysis (10 min)**

```bash
# Run a load-generating container
podman run -d --name perf-test \
  --memory=256m \
  --cpus=1 \
  nginx:alpine

# Watch stats in real-time
echo "Watching stats for 10 seconds..."
timeout 10 podman stats perf-test 2>/dev/null || podman stats --no-stream perf-test

# Generate some load
echo -e "\n=== Generating Load ==="
for i in {1..100}; do
  curl -s http://localhost:8080 > /dev/null 2>&1 &
done
wait

# Check stats after load
podman stats --no-stream perf-test

# Cleanup
podman rm -f perf-test
```

---

## 8. Network Engineering for Containers

### 8.1 Container Networking Models

```
┌─────────────────────────────────────────────────────────────────┐
│               CONTAINER NETWORK TYPES                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   BRIDGE (Default)           HOST                 NONE          │
│   ───────────────           ────                 ────           │
│                                                                 │
│   ┌─────────────┐         ┌─────────────┐    ┌─────────────┐   │
│   │ Container A │         │ Container   │    │ Container   │   │
│   │ 172.17.0.2  │         │ Uses host   │    │ No network  │   │
│   └──────┬──────┘         │ network     │    │ Isolated    │   │
│   ┌──────┴──────┐         │ directly    │    │             │   │
│   │ Container B │         └─────────────┘    └─────────────┘   │
│   │ 172.17.0.3  │                                              │
│   └──────┬──────┘         Use case:           Use case:        │
│          │                • High perf         • Security       │
│   ┌──────┴──────┐         • No port mapping   • Processing     │
│   │   bridge0   │           needed                              │
│   │  (docker0)  │                                              │
│   └──────┬──────┘                                              │
│          │                                                      │
│   ┌──────┴──────┐                                              │
│   │  Host      │                                               │
│   │  Network   │                                               │
│   └─────────────┘                                              │
│                                                                 │
│   Use case: Most common, containers can communicate            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 8.2 Custom Networks & Service Discovery

```bash
# ═══════════════════════════════════════════════════
# CREATE CUSTOM NETWORKS
# ═══════════════════════════════════════════════════

# Create custom bridge network
podman network create app-network

# Create with specific subnet
podman network create --subnet 10.10.0.0/24 custom-net

# List networks
podman network ls

# Inspect network
podman network inspect app-network

# ═══════════════════════════════════════════════════
# CONTAINER DNS (Automatic Service Discovery)
# ═══════════════════════════════════════════════════

# On custom networks, containers can reach each other BY NAME!

# Create network
podman network create microservices

# Start "database" 
podman run -d \
  --name postgres \
  --network microservices \
  -e POSTGRES_PASSWORD=secret \
  postgres:15-alpine

# Start "api" that connects to database BY NAME
podman run -d \
  --name api \
  --network microservices \
  -e DATABASE_HOST=postgres \
  python:3.11-alpine sleep infinity

# Test DNS resolution
podman exec api ping -c 2 postgres
# PING postgres (10.89.0.2): 56 data bytes ← Works!

# ═══════════════════════════════════════════════════
# PORT MAPPING STRATEGIES
# ═══════════════════════════════════════════════════

# Map to all interfaces (0.0.0.0)
podman run -d -p 8080:80 nginx

# Map to localhost only (more secure)
podman run -d -p 127.0.0.1:8080:80 nginx

# Multiple ports
podman run -d -p 80:80 -p 443:443 nginx

# Random host port
podman run -d -p 80 nginx
podman port <container>  # See assigned port

# UDP ports
podman run -d -p 53:53/udp dns-server
```

### 8.3 🔬 Lab: Container Networking

**Exercise 8.1: Multi-Service Network (20 min)**

```bash
cd ~/container-workshop/05-networking

# Create isolated network for our "microservices"
podman network create shop-network

# Start backend services
echo "=== Starting Backend Services ==="

# Database
podman run -d \
  --name shop-db \
  --network shop-network \
  -e POSTGRES_USER=shop \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=shopdb \
  postgres:15-alpine

# Redis cache
podman run -d \
  --name shop-cache \
  --network shop-network \
  redis:alpine

# Wait for services
sleep 5

# Start application that connects to both
echo -e "\n=== Starting Application ==="
podman run -d \
  --name shop-api \
  --network shop-network \
  -p 8080:80 \
  -e DB_HOST=shop-db \
  -e CACHE_HOST=shop-cache \
  nginx:alpine

# Test internal connectivity
echo -e "\n=== Testing Internal DNS Resolution ==="
podman exec shop-api sh -c '
echo "Pinging database..."
ping -c 1 shop-db
echo ""
echo "Pinging cache..."
ping -c 1 shop-cache
'

# Test external access
echo -e "\n=== Testing External Access ==="
curl -s http://localhost:8080 | head -3

# Show network details
echo -e "\n=== Network Topology ==="
podman network inspect shop-network --format '{{range .Containers}}{{.Name}}: {{.IPv4Address}}{{"\n"}}{{end}}'

# Cleanup
podman rm -f shop-db shop-cache shop-api
podman network rm shop-network
```

---

## 9. Persistent Storage Strategies

### 9.1 Volume Types & Use Cases

```
┌─────────────────────────────────────────────────────────────────┐
│                    STORAGE OPTIONS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   NAMED VOLUMES (Recommended for data)                          │
│   ────────────────────────────────────                          │
│   podman volume create mydata                                   │
│   podman run -v mydata:/data app                               │
│                                                                 │
│   ✅ Managed by Podman                                          │
│   ✅ Easy backup/restore                                        │
│   ✅ Survives container removal                                 │
│   ✅ Can be shared between containers                           │
│                                                                 │
│   ─────────────────────────────────────────────────            │
│                                                                 │
│   BIND MOUNTS (For development)                                 │
│   ─────────────────────────────                                 │
│   podman run -v ./code:/app:ro app                             │
│                                                                 │
│   ✅ Direct host filesystem access                              │
│   ✅ Real-time code changes                                     │
│   ⚠️ Platform-specific paths                                    │
│   ⚠️ Can modify host files                                      │
│                                                                 │
│   ─────────────────────────────────────────────────            │
│                                                                 │
│   TMPFS (Temporary data)                                        │
│   ──────────────────────                                        │
│   podman run --tmpfs /tmp app                                  │
│                                                                 │
│   ✅ In-memory (fast)                                           │
│   ✅ Secure (not persisted)                                     │
│   ⚠️ Limited by RAM                                             │
│   ⚠️ Lost when container stops                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 9.2 🔬 Lab: Data Persistence

**Exercise 9.1: Database Persistence (15 min)**

```bash
cd ~/container-workshop/06-volumes

# Create named volume for database
podman volume create postgres-data

# Start PostgreSQL with persistent storage
podman run -d \
  --name persist-db \
  -e POSTGRES_PASSWORD=workshop \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:15-alpine

sleep 5

# Create some data
podman exec persist-db psql -U postgres -c "
CREATE TABLE workshop (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
INSERT INTO workshop (name) VALUES ('Container Workshop');
SELECT * FROM workshop;
"

# Stop and REMOVE the container
podman rm -f persist-db
echo "Container destroyed!"

# Start a NEW container with SAME volume
podman run -d \
  --name persist-db-new \
  -e POSTGRES_PASSWORD=workshop \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:15-alpine

sleep 5

# Data is still there!
echo -e "\n=== Data Survived Container Destruction! ==="
podman exec persist-db-new psql -U postgres -c "SELECT * FROM workshop;"

# Cleanup
podman rm -f persist-db-new
podman volume rm postgres-data
```

---

## 10. Real-World Multi-Container Applications

### 10.1 Building an E-Commerce Stack

Let's build a complete e-commerce backend without Docker Compose:

```bash
cd ~/container-workshop/projects/ecommerce

# ═══════════════════════════════════════════════════
# CREATE INFRASTRUCTURE
# ═══════════════════════════════════════════════════

# Network for all services
podman network create ecommerce-net

# Volumes for persistent data
podman volume create ecommerce-db
podman volume create ecommerce-redis

# ═══════════════════════════════════════════════════
# START DATABASE
# ═══════════════════════════════════════════════════

podman run -d \
  --name ecom-postgres \
  --network ecommerce-net \
  -e POSTGRES_USER=ecom \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=ecommerce \
  -v ecommerce-db:/var/lib/postgresql/data \
  --health-cmd "pg_isready -U ecom" \
  --health-interval 10s \
  postgres:15-alpine

# ═══════════════════════════════════════════════════
# START CACHE
# ═══════════════════════════════════════════════════

podman run -d \
  --name ecom-redis \
  --network ecommerce-net \
  -v ecommerce-redis:/data \
  redis:alpine redis-server --appendonly yes

# ═══════════════════════════════════════════════════
# WAIT FOR SERVICES
# ═══════════════════════════════════════════════════

echo "Waiting for database..."
sleep 10

# ═══════════════════════════════════════════════════
# START API
# ═══════════════════════════════════════════════════

# Create API directory and files
mkdir -p api
cat > api/app.py << 'PYEOF'
from flask import Flask, jsonify
import os
import psycopg2
import redis

app = Flask(__name__)

# Connect to services by NAME (DNS)
db_conn = psycopg2.connect(
    host='ecom-postgres',
    database='ecommerce',
    user='ecom',
    password='secret'
)
cache = redis.Redis(host='ecom-redis', port=6379)

@app.route('/')
def index():
    # Test database
    cur = db_conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()[0]
    
    # Test cache
    cache.incr('visits')
    visits = cache.get('visits').decode()
    
    return jsonify({
        'service': 'E-Commerce API',
        'database': db_version[:30],
        'visits': visits
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
PYEOF

cat > api/requirements.txt << 'EOF'
flask==3.0.0
psycopg2-binary==2.9.9
redis==5.0.1
gunicorn==21.2.0
EOF

cat > api/Dockerfile << 'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
EOF

# Build and run API
podman build -t ecom-api:1.0 ./api

podman run -d \
  --name ecom-api \
  --network ecommerce-net \
  -p 5000:5000 \
  --health-cmd "curl -f http://localhost:5000/health" \
  --health-interval 10s \
  ecom-api:1.0

# ═══════════════════════════════════════════════════
# TEST THE STACK
# ═══════════════════════════════════════════════════

echo "Waiting for API..."
sleep 5

echo -e "\n=== Testing E-Commerce Stack ==="
curl http://localhost:5000/
echo ""

echo -e "\n=== Visit Counter (refresh increments) ==="
for i in {1..3}; do
    curl -s http://localhost:5000/ | grep visits
done

echo -e "\n=== All Services Running ==="
podman ps --filter "name=ecom-" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

**Cleanup Script:**
```bash
# Save as cleanup-ecommerce.sh
#!/bin/bash
podman rm -f ecom-postgres ecom-redis ecom-api
podman network rm ecommerce-net
podman volume rm ecommerce-db ecommerce-redis
podman rmi ecom-api:1.0
echo "Cleanup complete!"
```

---

## 11. Security Hardening

### 11.1 Container Security Checklist

```
┌─────────────────────────────────────────────────────────────────┐
│              CONTAINER SECURITY CHECKLIST                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   IMAGE SECURITY                                                │
│   ──────────────                                                │
│   ☐ Use specific image tags (not :latest)                      │
│   ☐ Use official or verified images                            │
│   ☐ Scan images for vulnerabilities                            │
│   ☐ Use minimal base images (alpine, distroless)               │
│   ☐ Remove unnecessary packages                                │
│   ☐ Don't include secrets in images                            │
│                                                                 │
│   RUNTIME SECURITY                                              │
│   ────────────────                                              │
│   ☐ Run as non-root user                                       │
│   ☐ Use read-only root filesystem                              │
│   ☐ Drop unnecessary capabilities                              │
│   ☐ Set resource limits                                        │
│   ☐ Use security profiles (seccomp, AppArmor)                  │
│                                                                 │
│   NETWORK SECURITY                                              │
│   ────────────────                                              │
│   ☐ Use custom networks (not default bridge)                   │
│   ☐ Expose only necessary ports                                │
│   ☐ Bind to localhost when possible                            │
│   ☐ Use TLS for inter-container communication                  │
│                                                                 │
│   SECRETS MANAGEMENT                                            │
│   ──────────────────                                            │
│   ☐ Use environment variables (not files in images)            │
│   ☐ Never commit secrets to git                                │
│   ☐ Use Podman secrets or external vaults                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 11.2 Secure Container Example

```bash
# Production-secure container launch
podman run \
  --name secure-app \
  --user 1000:1000 \                    # Non-root
  --read-only \                         # Read-only filesystem
  --tmpfs /tmp:rw,noexec,nosuid \      # Temp storage
  --cap-drop ALL \                      # Drop all capabilities
  --security-opt no-new-privileges \    # Prevent privilege escalation
  --memory 256m \                       # Memory limit
  --cpus 1 \                            # CPU limit
  --pids-limit 50 \                     # Prevent fork bombs
  --network custom-net \                # Isolated network
  -p 127.0.0.1:8080:8080 \             # Localhost only
  myapp:1.0
```

---

## 12. Production Troubleshooting

### 12.1 Quick Troubleshooting Guide

| Problem | Diagnosis | Solution |
|---------|-----------|----------|
| Container won't start | `podman logs <name>` | Check error message |
| Port already in use | `ss -tlnp \| grep :8080` | Use different port |
| Out of disk space | `podman system df` | `podman system prune -a` |
| Container OOM killed | `podman inspect --format '{{.State.OOMKilled}}'` | Increase memory limit |
| Network unreachable | `podman exec <c> ping <target>` | Check network config |
| Permission denied | Check file permissions | Run as correct user |

### 12.2 Debug Commands

```bash
# View all container info
podman inspect <container>

# Check why container exited
podman inspect <container> --format '{{.State.ExitCode}}'

# View events
podman events --since 1h

# System diagnostics
podman info
podman system df

# Debug networking
podman exec <container> ping <hostname>
podman exec <container> nslookup <service>
podman network inspect <network>
```

---

## 13. Graduation & Next Steps

### 13.1 What You've Mastered

| Skill | Confidence Level |
|-------|-----------------|
| Container concepts & architecture | ⭐⭐⭐⭐⭐ |
| Building images with Dockerfile | ⭐⭐⭐⭐⭐ |
| Running production containers | ⭐⭐⭐⭐⭐ |
| Container networking | ⭐⭐⭐⭐⭐ |
| Data persistence | ⭐⭐⭐⭐⭐ |
| Multi-container apps | ⭐⭐⭐⭐⭐ |
| Security best practices | ⭐⭐⭐⭐⭐ |
| Troubleshooting | ⭐⭐⭐⭐⭐ |

### 13.2 Your Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                YOUR CONTAINER JOURNEY                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   TODAY                                                         │
│   ─────                                                         │
│   ✅ Docker/Podman fundamentals                                 │
│   ✅ Images & Dockerfiles                                       │
│   ✅ Networking & Volumes                                       │
│   ✅ Multi-container apps                                       │
│                                                                 │
│   NEXT 2 WEEKS                                                  │
│   ────────────                                                  │
│   → Docker Compose                                              │
│   → CI/CD with containers (GitHub Actions)                      │
│   → Container registries (GHCR, ACR)                           │
│                                                                 │
│   NEXT MONTH                                                    │
│   ──────────                                                    │
│   → Kubernetes fundamentals                                     │
│   → Helm charts                                                 │
│   → Cloud containers (Azure Container Apps, AWS ECS)           │
│                                                                 │
│   3 MONTHS                                                      │
│   ────────                                                      │
│   → CKA/CKAD certification                                     │
│   → Service mesh (Istio)                                       │
│   → GitOps (ArgoCD, Flux)                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 13.3 Complete Cleanup

```bash
# Stop all containers
podman stop $(podman ps -aq) 2>/dev/null

# Remove all containers
podman rm $(podman ps -aq) 2>/dev/null

# Remove workshop images
podman rmi $(podman images -q) 2>/dev/null

# Remove volumes
podman volume prune -f

# Remove networks  
podman network prune -f

# Full cleanup
podman system prune -a --volumes -f

echo "Cleanup complete!"
```

### 13.4 Resources

- **Podman Documentation:** https://docs.podman.io/
- **Docker Documentation:** https://docs.docker.com/
- **Kubernetes:** https://kubernetes.io/docs/
- **Container Security:** https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html

---

## 🎓 Congratulations!

You've completed the Container Masterclass! You now have the skills that power Netflix, Spotify, and 95% of Fortune 500 companies.

**Remember:** The best way to learn is to build. Start containerizing your own projects today!

*Workshop created for hands-on learning*
