---
published: true
type: workshop
title: Containers Fundamentals — From Zero to Confidence
short_title: Docker & Podman Lab
description: Master containerization. Build, secure, and operate containers using Docker CLI and Podman.
level: beginner
authors:
  - Abdoul-Hakim Afraitane
duration_minutes: 480
tags: docker, podman, containers, devops, microservices
navigation_levels: 2
navigation_numbering: true
sections_title:
  - "Kickoff: Why Containers"
  - "Setup: Podman Environment"
  - "Launch Your First Container"
  - "Concepts Deep Dive"
  - "Package Your Own API"
  - "Operate Containers"
  - "Connect Services (Networking)"
  - "Persist Data + Capstone Stack"
  - "Security Wrap + Next Steps"
  - "Appendix: Command Reference"
---

# Containers Fundamentals — From Zero to Confidence

Welcome! In this full-day workshop you will build, ship, and operate containers.
Each section drops you into a realistic scenario: a broken deployment, a missing database, a service that can't find its neighbor. You solve each one hands-on, and by the end of the day you walk out with the skills and the mental model to containerize your own projects.

## Learning Objectives

By the end of the day you will be able to:

- Explain container architecture (images, layers, isolation)
- Build container images with Dockerfiles
- Run, manage, and operate containers
- Wire up networking and storage across multiple services
- Apply security best practices (least privilege, minimal images, resource limits)

## Lab Overview

The story: you just joined a team that ships a small API. It runs fine on dev laptops but breaks everywhere else. Your mission: containerize it, wire it to a database and a cache, prove the data survives a crash, and lock it down — all before the end of the day.

Five hands‑on sections take you from zero to a working stack:

1. Launch your first container — images, containers, ports, inspect
2. Package your own API — Dockerfiles, layers, caching, non‑root, healthchecks
3. Operate containers — lifecycle, logs, resource limits
4. Connect services — custom networks, DNS, service discovery
5. Persist data + ship a mini‑stack — volumes, DB survival, capstone

> **Checkpoint rule:** every lab ends with a few questions. Take a minute to answer them — if you can't, re-read the section. This is where concepts stick.

---

# Kickoff: Why Containers

Before you touch a single command, let's understand why containers exist — and why every team you'll join is already using them (or about to).

## The problem

Environment‑related failures trace back to drift — different runtimes, libraries, OS versions, or configuration drifting silently across machines.

### The “works on my machine” gap

![It works on my machine](assets/it_works_on_my_machine.png)

> **Real-world impact:** this is the #1 reason production incidents happen in teams that don't use containers. A tiny version mismatch between dev and prod can cost hours of debugging.

## What is a container?

A container wraps everything your application needs into a standardized, self‑contained unit:

- Your application
- Dependencies (libraries, frameworks)
- Runtime (e.g., Python/Node/JDK)
- System libraries
- Configuration

Whatever runs inside the container on your laptop runs identically everywhere else — your colleague's laptop, the CI pipeline, the production server.

## Containers vs Virtual Machines

The question always comes up: *"How is this different from a VM?"* Short answer: containers are much lighter because they share the host kernel instead of running a full guest OS.

![Virtual Machines vs Containers](assets/_Virtual%20Machines%20vs%20Containers.png)

## Why Podman

In this workshop we use Podman — a modern, daemonless, rootless container engine that is fully CLI-compatible with Docker. Everything you learn here transfers directly to Docker, but you get a safer default setup and zero licensing concerns.

Podman gives you a safer, license‑free container experience:

- Daemonless — no privileged daemon running in the background
- Rootless by default — safer local development
- Docker‑CLI compatible — most commands are identical
- Enterprise‑friendly — no Docker Desktop licensing concerns

| Feature | Docker | Podman |
|---------|--------|--------|
| Architecture | Client → daemon (dockerd) | Direct fork/exec (no daemon) |
| Root required? | Daemon runs as root | Rootless by default |
| CLI compatibility | `docker ...` | `podman ...` (same syntax) |
| Systemd integration | Separate service | `podman generate systemd` |
| Desktop licensing | Paid for enterprise | Free |

> Every command in this workshop works with either `podman` or `docker` — set an alias and use whichever you prefer.

Now that you know why containers exist, let's get your environment ready.

---

# Setup: Podman Environment

This section gets your machine ready. Follow the steps for your OS, then run the verification script at the end. Do not skip this — every lab after this point assumes a working Podman installation.

## Prerequisites

- OS: Windows 10/11, macOS 12+, or Linux (Ubuntu 22.04+)
- Hardware: 8GB RAM (16GB recommended), ~25GB free disk
- VS Code + Docker extension recommended
- Basic command line familiarity

## Installation

### Windows

```powershell
# Option A — winget (recommended)
winget install -e --id RedHat.Podman
winget install -e --id RedHat.Podman-Desktop

# Option B — Chocolatey
choco install podman-cli podman-desktop

# Initialize the Podman VM (runs a small Linux instance under WSL2)
podman machine init
podman machine start
```

> **Tip (Windows):** if `podman machine start` fails, make sure WSL2 is installed and enabled. Run `wsl --install` in an elevated PowerShell if needed.

### macOS

```bash
# Option A — Homebrew
brew install podman
brew install --cask podman-desktop

# Option B — official installer from https://podman.io/

# Initialize the Podman VM (runs under Apple Virtualization)
podman machine init
podman machine start
```

> **Tip (macOS):** on Apple Silicon Macs, Podman creates an ARM64 Linux VM. Images tagged `amd64` may run slower under emulation — prefer `arm64` or multi-arch images when available.

### Linux (Ubuntu/Debian)

```bash
# Ubuntu 22.04+
sudo apt-get update
sudo apt-get install -y podman

# Verify cgroup & namespace support
podman info --format '{{.Host.CgroupsVersion}}'
```

## Setup goal

By the end of this section you should be able to:

- Run `podman --version` and see version 4.x or higher
- Pull and run a simple container (`hello-world`)
- Map a port and reach a service at `localhost:PORT`

Let's verify everything works.

### Verification script

Run each command below one by one. If any step fails, stop and fix it before continuing. This is your foundation for the rest of the day.

```bash
# 1 — Podman is installed
podman --version

# 2 — Podman can pull and run images
podman run --rm hello-world

# 3 — Port mapping works
podman run -d -p 9090:80 --name verify-nginx nginx:alpine
curl -I http://localhost:9090
podman rm -f verify-nginx

# 4 — You can build images
echo 'FROM alpine:3.19' | podman build -t test-build -
podman rmi test-build

echo "All checks passed — you're ready."
```

You should see output similar to:

```
podman version 4.x.x
Hello from Docker!  (or Podman equivalent)
HTTP/1.1 200 OK
All checks passed — you're ready.
```

> Trouble? If port mapping fails, check that no other service is using port 9090. Try `podman rm -f verify-nginx` and re-run with a different port (e.g., `-p 9091:80`).

### Docker CLI alias (optional)

These aliases let you type `docker` instead of `podman`:

- PowerShell: `Set-Alias -Name docker -Value podman`
- Bash/Zsh: `alias docker=podman`

### Installation checkpoint

| Check | Expected |
|-------|----------|
| `podman --version` | 4.x or higher |
| `podman run hello-world` | "Hello from Docker!" or equivalent |
| Port mapping test | HTTP 200 from Nginx |
| Build test | Image builds successfully |

> All green? Great — you're ready for the fun part. Let's run your first real container.

---

# Launch Your First Container

You’re set up and ready to go. Next, we’ll run a web server locally with Podman in seconds.

## Scenario

You need Nginx locally to test your app but don’t want to install it on your OS.

## Key concepts

Before we start, let's make sure we speak the same language:

- **Image** — a versioned, immutable (read‑only) artifact stored in a registry. It defines what will run, but is not running itself.
- **Container** — a running instance of an image, augmented with an isolated, writable layer that exists only for the lifetime of that container.
- **Ports** — services inside a container are isolated by default; they become accessible externally only when ports are explicitly published to the host (for example, using -p).
- **Tags vs digests** — tags (such as 1.25-alpine) are mutable references that may point to different builds over time, whereas digests uniquely identify and lock an exact image artifact.

### How images and containers relate

![How Images and Containers Relate](assets/How%20Images%20and%20Containers%20Relate.png)

## Lab

Let's run Nginx and observe what happens at every step. Follow along — don't just read the commands, run them.

### Step 1 — Pull a known version

```bash
podman pull nginx:1.25-alpine
```

You should see Podman downloading the image layers one by one. When it's done, the image is stored locally.

### Step 2 — Inspect the image before running it

Always look before you leap. Let's see what's inside:

```bash
# See how many layers make up this image
podman history nginx:1.25-alpine

# Check size, architecture, and creation date
podman inspect nginx:1.25-alpine --format '
  Size:    {{.Size}}
  Arch:    {{.Architecture}}
  Created: {{.Created}}'
```

> **Why inspect first?** In production, you want to know the exact size, architecture, and age of every image you run. This habit catches surprises early.

### Step 3 — Run it with a clear port mapping

```bash
podman run -d --name web -p 8080:80 nginx:1.25-alpine
```

Explanation:
- `-d` runs the container in the background (detached)
- `--name web` gives it a human-friendly name
- `-p 8080:80` maps port 8080 on your machine to port 80 inside the container (where Nginx listens)

### Step 4 — Validate it works

```bash
curl -I http://localhost:8080
```

You should see:

```
HTTP/1.1 200 OK
Server: nginx/1.25.x
...
```

If you get a `200 OK`, your container is live and serving traffic.

### Step 5 — Observe (rather than assume)

Now let's look under the hood. These commands are your daily toolkit:

```bash
# Which ports are mapped?
podman port web

# What happened at startup?
podman logs --tail 20 web

# What image is the container using?
podman inspect web --format '{{.Config.Image}}'

# What processes are running inside?
podman top web

# What files changed since the image was started?
podman diff web
```

> **Tip:** `podman diff` is underrated. It shows you every file the container has added, changed, or deleted compared to the original image. Very useful for debugging.

### Step 6 — Cleanup

```bash
podman rm -f web
```

The container is gone. The image stays — you can spin up a new container from it in under a second.

## Checkpoint

- What is an image vs a container?
- What does `-p 8080:80` do?
- What kind of information do `logs`, `inspect`, and `top` give you?
- How many layers does `nginx:1.25-alpine` have?

---

# Concepts Deep Dive

You've run your first container — now let's understand how it works under the hood. This section covers the internals you need to write efficient Dockerfiles and reason about performance.

## Layers and caching

Every Dockerfile instruction stacks a new layer onto the image. Podman caches unchanged layers, so the order of your instructions directly controls rebuild speed. Get this wrong and every code change triggers a full rebuild; get it right and rebuilds take seconds.

![Image Layers Deep Dive](assets/Image%20Layers%20Deep%20Dive.png)

These rules keep your builds fast and your images lean:

- Put stable steps (OS packages, dependencies) before your application code
- Copy `requirements.txt` before `COPY . .` so dependency installs are cached
- Use `.dockerignore` to reduce build context and avoid busting the cache

> **Pro tip:** add a `.dockerignore` file before your first build, not after. A large build context (e.g., `.git/`, `node_modules/`) is the #1 cause of slow builds.

## Copy-on-Write

This is the magic trick that makes containers lightweight. Containers share the same read-only image layers, and each one gets its own thin writable layer on top. Writes land in that top layer, leaving the underlying image untouched.

![Copy-on-Write (CoW)](assets/Copy-on-Write%20(CoW).png)

## Runtime stack

When you type `podman run`, here's the chain of components that actually starts your container:

```
CLI (podman/docker)
  ↓
High-level runtime (containerd / CRI-O / Podman)
  ↓
Low-level runtime (runc / crun)
  ↓
Linux kernel (namespaces, cgroups, overlay filesystems)
```

> **Why does this matter?** When something goes wrong, knowing which layer handles what helps you debug faster. Network issues? That's the kernel namespace layer. Permission denied? Check user namespaces.

## Namespaces — what each container sees

Each container sees its own isolated slice of the system through Linux namespaces.

![Linux Namespaces](assets/Linux%20Namespaces.png)

### Namespace breakdown

Each namespace isolates a specific aspect of the system. Here's what they do and why they matter:

| Namespace | Isolates | What the container sees | Real-world impact |
|-----------|----------|------------------------|-------------------|
| PID | Process IDs | Its own process tree starting at PID 1. Cannot see or signal host processes. | `ps aux` inside a container shows only that container's processes — not the hundreds running on the host. |
| NET | Network stack | Its own network interfaces, IP addresses, routing tables, and port space. | Two containers can both listen on port 80 without conflicting. Each gets its own `localhost`. |
| MNT | Filesystem mounts | Its own root filesystem (`/`) assembled from image layers. Cannot see the host's `/etc`, `/home`, etc. | Deleting `/usr` inside a container doesn't touch the host. Bind mounts explicitly punch through this boundary. |
| UTS | Hostname and domain | Its own hostname (defaults to the container ID). | `hostname` returns the container's name, not the host machine's — useful for logging and service discovery. |
| IPC | Inter-process communication | Its own shared memory segments, semaphores, and message queues. | Prevents one container's shared memory from leaking into another — critical for multi-tenant workloads. |
| USER | User and group IDs | `root` (UID 0) inside the container maps to an unprivileged user on the host. | Even if an attacker escapes the container as "root", they land as a nobody on the host. This is the foundation of rootless containers. |

## cgroups — what each container is allowed to use

Control Groups cap the CPU, memory, and I/O each container can consume.

![Control Groups (cgroups v2)](assets/CONTROL%20GROUPS%20(cgroups%20v2).png)

### Quick lab — see isolation in action

Let's prove this isn't just theory — run this command and see resource limits in action:

```bash
podman run --rm --memory=128m --cpus=0.5 alpine cat /sys/fs/cgroup/memory.max
```

This runs a container limited to 128 MB of RAM and half a CPU core, then reads the kernel's cgroup file to confirm the limit is enforced. You should see `134217728` (128 MB in bytes).

> **Key takeaway:** namespaces control what a container can see; cgroups control what it can use. Together, they create a lightweight sandbox without needing a full virtual machine.

### Concepts checkpoint

| Concept | One-line summary |
|---------|-----------------|
| Image layers | Each Dockerfile instruction creates an immutable, cacheable layer |
| Copy-on-Write | Containers share read-only layers; writes go to a thin writable layer |
| Namespaces | Isolation of PID, network, filesystem, hostname, IPC, users |
| cgroups | Limits on CPU, memory, PIDs, I/O |

---

# Package Your Own API

So far you've been running someone else's image (Nginx). Now it's time to create your own. This is where containers become truly powerful — you capture your entire application, dependencies included, in a single portable artifact.

## Scenario

Your team needs a portable artifact for a small Python API — one that runs identically no matter where it lands: your laptop, CI, staging, production.

## Key concepts

- A Dockerfile is the build recipe for your image — think of it as infrastructure-as-code for your container
- Layer ordering controls caching and rebuild speed
- Multi‑stage builds strip build tools from the final image, keeping it small and secure
- A non‑root user enforces least privilege — if someone breaks into your container, they don't get root
- A healthcheck signals when your container is actually ready to serve traffic

### Choosing a base image

| Base image | Size | Use case |
|-----------|------|----------|
| `python:3.11` | ~900 MB | Full toolchain, C extensions, maximum compatibility |
| `python:3.11-slim` | ~150 MB | Good default — most packages work, much smaller |
| `python:3.11-alpine` | ~50 MB | Smallest, but musl libc can break some C extensions |
| `gcr.io/distroless/python3` | ~30 MB | No shell, no package manager — hardened |

> Start with slim and move to alpine only after you confirm every dependency builds cleanly.


### Dockerfile optimization rules

![Dockerfile Optimization Rules](assets/Dockerfile%20Optimization%20Rules.png)

### Why each rule matters

| Rule | Problem it solves | What happens if you ignore it | Impact |
|------|-------------------|-------------------------------|--------|
| **Order matters for caching** | Every time a layer changes, all subsequent layers are rebuilt from scratch. If `COPY . .` comes before `pip install`, every single code edit — even a typo fix — triggers a full dependency reinstall. | A 30-second rebuild turns into a 5-minute rebuild. Multiply that by every developer on the team, every commit, every CI run. | Moving `COPY requirements.txt` before `pip install` means dependencies are only reinstalled when `requirements.txt` actually changes. Code-only edits rebuild in seconds. |
| **Minimize layers** | Each `RUN` instruction creates a new layer in the image. Temporary files created and deleted in separate `RUN` steps still occupy space in intermediate layers — they're never truly removed. | Three separate `RUN` for update, install, and cleanup produce three layers. The `apt` cache from the first two layers is still baked into the image even after the third layer "deletes" it. | Chaining commands with `&&` in a single `RUN` keeps the install and cleanup in one layer. Files deleted in the same layer never make it into the final image, reducing size by tens or hundreds of MB. |
| **Use specific tags** | `latest` is a moving target — it points to a different image every time the upstream publishes. Today your build works; tomorrow it breaks because `latest` jumped to a new major version with breaking changes. | Builds are no longer reproducible. Two teammates building the same Dockerfile on the same day can get different base images. Debugging becomes a nightmare. | Pinning to `python:3.11-slim-bookworm` guarantees the same OS, the same Python patch version, and the same system libraries every time — on every machine, in every pipeline. |
| **Use .dockerignore** | The Docker/Podman build context is everything in the directory you pass to `build`. Without `.dockerignore`, that includes `.git/` (often 100+ MB), `node_modules/`, test fixtures, local `.env` files with secrets, and IDE config. | Build context transfer is slow (you'll see "Sending build context to daemon... 500 MB"). Worse, secrets in `.env` or `.git/config` end up inside the image where anyone with access can extract them. | A well-crafted `.dockerignore` keeps the build context small (fast uploads) and prevents sensitive files from leaking into the image. Think of it as `.gitignore` for your container builds. |

> **Rule of thumb:** if your image is over 500 MB or your builds take more than 60 seconds, revisit these four rules — at least one is being violated.

## Lab: Build a Python API image

This is the most important lab of the workshop. You'll create four files, build a production-quality image, and understand every line of the Dockerfile.

> **Important:** create these files in a new empty directory — don't mix them with other projects.

### Artefacts

Set up these four files in your working directory:

`app.py`

```python
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
```

`requirements.txt`

```
flask==3.0.0
gunicorn==21.2.0
```

`Dockerfile` (multi-stage, non-root, healthcheck)

```dockerfile
# ── Stage 1: Install dependencies ──────────────────
FROM python:3.11-slim-bookworm AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ── Stage 2: Final image ───────────────────────────
FROM python:3.11-slim-bookworm
LABEL maintainer="workshop@example.com"
LABEL version="1.0.0"

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser/app

# Copy dependencies from builder (no compiler, no pip cache)
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appuser app.py .

# Environment
ENV PATH=/home/appuser/.local/bin:$PATH \
    APP_VERSION=1.0.0 \
    PYTHONUNBUFFERED=1

USER appuser
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
```

What's happening here?

| Instruction | Why |
|-------------|-----|
| `AS builder` | Creates a temporary stage — only its output (`/root/.local`) is copied into the final image |
| `--user` in pip install | Installs into `~/.local` so we can copy just the packages (no pip cache or build tools) |
| `useradd appuser` | The container runs as a non-root user — defense in depth |
| `COPY --from=builder` | Only the installed packages cross into the final image — no compiler, no pip, no cache |
| `HEALTHCHECK` | Podman (and orchestrators) will probe `/health` to know if the app is actually ready |
| `gunicorn` | Production WSGI server instead of Flask's dev server — handles concurrent requests |

> **Why multi-stage?** Without it, your final image contains pip, compilers, and build caches — hundreds of MB you don't need at runtime. Multi-stage keeps only what matters.

`.dockerignore`

```
__pycache__
*.pyc
.git
.env
README.md
```

### Build + run

Let's build the image and verify everything works:

```bash
podman build --format docker -t workshop-api:1.0.0 .
```

> Why `--format docker`? Podman defaults to the OCI image format, which does not support the `HEALTHCHECK` instruction. Adding `--format docker` tells Podman to produce a Docker-format image so the health check is preserved.

You should see each layer being built. The first build downloads the base image; subsequent builds are much faster thanks to caching.

```bash
# Check the image size — should be ~170 MB (not 900+ MB!)
podman images workshop-api:1.0.0

# Start the container
podman run -d --name api -p 8000:8000 workshop-api:1.0.0

# Test both endpoints
curl -s http://localhost:8000/ | head
curl -s http://localhost:8000/health
```

You should see JSON output like:

```json
{"hostname": "a1b2c3d4", "service": "Container Workshop API", "version": "1.0.0"}
{"status": "healthy"}
```

Now verify your security and optimization choices are working:

```bash
# Confirm non-root — should print "appuser", NOT "root"
podman exec api whoami

# Inspect layers — notice how few there are compared to a single-stage build
podman history workshop-api:1.0.0

podman rm -f api
```

### Dockerfile mastery checkpoint

| Best practice | Applied? |
|--------------|----------|
| Specific base image tag | ☐ `python:3.11-slim-bookworm` |
| Multi-stage build | ☐ Separate builder and runtime stages |
| Non-root user | ☐ `USER appuser` |
| Optimized layer order | ☐ COPY requirements before code |
| .dockerignore | ☐ Excludes .git, tests, etc. |
| Health check | ☐ `HEALTHCHECK CMD ...` |
| Labels | ☐ `LABEL version="1.0"` |

## Checkpoint

- Why did you choose your base image variant (slim/alpine/distroless)?
- How does your Dockerfile reduce rebuild time?
- How do you know you're not running as root?
- What is the size difference between single-stage and multi-stage builds?

---

# Operate Containers

You can build images and run containers. Now let's learn to manage them day-to-day. This section covers the commands you'll use most often: checking status, reading logs, setting resource limits, and cleaning up.

## Scenario

Your containers are running in a dev environment. A teammate reports that one service is eating all the memory on the shared machine. You need to find it, check its logs, and add resource limits.

## Key concepts

### Container lifecycle

![Container Lifecycle](assets/Container%20Lifecycle.png)

- **Lifecycle** — a container moves through created → running → stopped → removed
- **Health** — a passing HEALTHCHECK tells you the container is actually ready
- **Limits** — resource caps prevent a single container from starving the host

## Useful commands

These are the commands you'll reach for every day. Bookmark this section — you'll come back to it.

```bash
podman ps                                 # Running containers
podman ps -a                              # All containers (including stopped)
podman logs <container>                   # View logs
podman logs --tail 20 <container>         # Last N lines
podman exec -it <container> /bin/sh       # Interactive shell
podman inspect <container>                # Full JSON details
podman stats --no-stream                  # One-time resource snapshot
```

## Lab: Resource limits

Let's see resource limits in action. Without limits, a single runaway container can bring down an entire host.

```bash
# Run with memory and CPU limits
podman run -d --name limited \
  --memory=256m \
  --cpus=1 \
  nginx:alpine

# Check stats — notice the MEM LIMIT column
podman stats --no-stream limited
```

You should see output like:

```
NAME      CPU %   MEM USAGE / LIMIT   ...
limited   0.00%   2.5MB / 256MB       ...
```

The container can never exceed 256 MB. If it tries, the OOM killer terminates it.

```bash
# Cleanup
podman rm -f limited
```

> **Real-world rule:** always set memory limits on production containers. A container without limits can consume all available memory and crash every other service on the host.

## Checkpoint

- What lifecycle states can a container be in?
- Why set memory and CPU limits on containers?
- How do resource limits protect the host?

---

# Connect Services (Networking)

So far every container you've run was alone. In the real world, services talk to each other: an API calls a database, a web app hits a cache. This section teaches you how containers find and communicate with each other — safely, by name, on an isolated network.

## Scenario

Your API needs a database and a cache. All three services need to discover each other by name — no hardcoded IP addresses, no manual configuration.

## Key concepts

### Network types

![Container Network Types](assets/Container%20Network%20Types.png)

- **Custom bridge** — your go-to for multi-service setups, giving you DNS by container name
- **Default bridge** — no DNS here; containers must hardcode IP addresses
- **Host** — the container shares your host’s network stack directly, with no isolation
- **None** — cuts off all networking, useful for processing-only containers

> **Beyond Bridge, Host, and None:** these three modes cover the vast majority of local development scenarios and are the ones used throughout this workshop. However, container networking goes much further — runtimes support additional modes like Macvlan, IPvlan, and container-to-container sharing, while orchestrators (Kubernetes, Docker Swarm, Nomad) and cloud platforms introduce overlay networks, service meshes, and their own CNI plugins. The networking options available to you ultimately depend on the container runtime, the orchestrator, and the platform on which you deploy.

### DNS & service discovery

Custom networks give you something magical: automatic DNS. Every container on the network can reach any other container by its `--name`:

```
podman exec api ping postgres    ← works on custom network
```

No `/etc/hosts` editing. No IP address hunting. Just use the container name.

### Port mapping strategies

Not every container needs to be reachable from your host. Only the "front door" (e.g., the API or web server) needs a published port:

```bash
podman run -d -p 8080:80 nginx                 # Map to all interfaces
podman run -d -p 127.0.0.1:8080:80 nginx       # Localhost only (more secure)
podman run -d -p 80:80 -p 443:443 nginx        # Multiple ports
podman run -d -p 80 nginx                       # Random host port
podman port <container>                          # See assigned port
```

## Lab: Multi-service network

Let's put this into practice. You'll spin up three services on an isolated network and prove they can reach each other by name.

```bash
# Create isolated network
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

# Show network topology
echo -e "\n=== Network Topology ==="
podman network inspect shop-network --format '{{range $id, $info := .Containers}}{{$info.Name}}: {{range $iface, $net := $info.Interfaces}}{{range $net.Subnets}}{{.IPNet}}{{end}}{{end}}{{"\n"}}{{end}}'

# Cleanup
podman rm -f shop-db shop-cache shop-api
podman network rm shop-network
```

What you should see:

- The `ping` commands succeed — each container resolves the other's name via DNS
- `curl localhost:8080` returns the Nginx welcome page — only the API's port is published
- The network topology shows three containers with internal IPs (e.g., `10.89.0.2/24`, `10.89.0.3/24`, `10.89.0.4/24`)

> **Notice:** neither the database nor Redis has a `-p` flag. They are only reachable from inside `shop-network` — which is exactly what you want in production. Only the front-facing service exposes a port.

## Checkpoint

- Why is a custom network better than the default bridge?
- Which services need port mapping to the host? Which don't?
- How does DNS resolution work on a custom network?

---

# Persist Data + Capstone Stack

Here's the thing about containers: they're ephemeral by design. When a container stops, its writable layer vanishes. That's great for reproducibility — terrible if your database was inside it. This section teaches you how to make data survive the container lifecycle, and then puts everything together in a capstone exercise.

## Part A — Persistence (Volumes)

### Scenario

Imagine your Postgres container crashes at 3 AM. It restarts automatically — but all your customer data is gone because it was stored inside the container's writable layer. Let's make sure that never happens.

### Key concepts

![Container Storage Options](assets/Container%20Storage%20Options.png)

> **Beyond Volumes, Bind Mounts, and tmpfs:** these three storage types are universal concepts supported by every major container runtime and cover the vast majority of local development scenarios — which is why this workshop focuses on them. However, container storage goes much further once you move to orchestrated environments. Kubernetes, for example, introduces PersistentVolumes, PersistentVolumeClaims, and StorageClasses that decouple storage provisioning from the application entirely. Cloud platforms add their own managed options — Azure Disks, AWS EBS, GCE Persistent Disks — while distributed filesystems like NFS, Ceph, and Longhorn provide storage across clusters. The storage options available to you ultimately depend on the container runtime, the orchestrator, and the infrastructure on which you deploy.

### Lab: Prove database persistence

#### The business context

A common operational pattern with containerized databases is **immutable infrastructure**: instead of patching a running container in place, you pull a new image, destroy the old container, and start a fresh one from the updated image. This approach guarantees reproducibility — but it introduces a critical risk: any data stored inside the container's writable layer is lost when that container is removed.

Consider a product catalog service backed by PostgreSQL. During a routine version upgrade, the operations pipeline replaces the database container. If the data directory (`/var/lib/postgresql/data`) lives inside the container, the entire catalog — products, prices, inventory — is destroyed with it. The replacement container initializes a blank database. From the application's perspective, the catalog is empty. From the business's perspective, the service is down.

This class of incident is well-documented and entirely preventable. The solution is to **decouple the container lifecycle from the data lifecycle** by mounting the database data directory on an external named volume. The volume is managed by the container runtime independently of any container: it persists across container removals, can be backed up, and can be attached to any new container.

#### What this lab demonstrates

You will reproduce the exact upgrade scenario described above — with the correct architecture already in place:

1. **Provision a named volume** (`pg-data`) to hold the database files externally.
2. **Start a PostgreSQL container** with the volume mounted at `/var/lib/postgresql/data`.
3. **Insert structured data** — a table and a record representing a catalog entry.
4. **Remove the container** — simulating a crash, a version upgrade, or a scheduled teardown.
5. **Start a new container** attached to the same volume and verify the data is intact.

The key principle: **separating compute from state** allows containers to remain disposable while data remains durable.

```bash
# Provision a named volume for database files
podman volume create pg-data

# Start PostgreSQL with the volume mounted at its data directory
podman run -d \
  --name pg \
  -e POSTGRES_PASSWORD=workshop \
  -v pg-data:/var/lib/postgresql/data \
  postgres:15-alpine

sleep 5

# Insert structured data — a catalog entry
podman exec pg psql -U postgres -c "
CREATE TABLE workshop (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
INSERT INTO workshop (name) VALUES ('Container Workshop');
SELECT * FROM workshop;
"

# Remove the container — simulating a version upgrade or crash
podman rm -f pg
echo "Container removed."

# Start a new container attached to the same volume
podman run -d \
  --name pg2 \
  -e POSTGRES_PASSWORD=workshop \
  -v pg-data:/var/lib/postgresql/data \
  postgres:15-alpine

sleep 5

# Verify data durability
echo -e "\n=== Verifying data persistence ==="
podman exec pg2 psql -U postgres -c "SELECT * FROM workshop;"

# Cleanup
podman rm -f pg2
podman volume rm pg-data
```

**Expected result:** the `SELECT` query returns the row inserted earlier (`Container Workshop`), confirming that the data persisted across container destruction. The volume — not the container — owns the state.

> **Key takeaway:** in production, every stateful service — databases, message brokers, file stores — must have its data directory mounted on an external volume. Containers are ephemeral by design; volumes are not. Without this separation, any container removal, intentional or not, results in irreversible data loss.

### Checkpoint

- Why is persistence important?
- What survives: container? image? volume?
- When would you use a bind mount instead of a named volume?

## Part B — Capstone: Mini E‑Commerce Backend (Postgres + Redis + API)

This is the grand finale. Everything you've learned — images, Dockerfiles, networking, volumes, health checks — comes together in one working application.

### Scenario

You're building a minimal e-commerce backend from scratch:

- Postgres — stores product and order data
- Redis — caches visit counts for fast reads
- Flask API — exposes endpoints that talk to both

### Key concepts

- Services share one custom network and discover each other by container name (DNS)
- Health checks signal when each service is actually ready — not just "running"
- Each container runs exactly one process — the Unix philosophy applied to containers

### Lab: Build the full stack

This is a longer lab, but take your time. Each block builds on the previous one. By the end you'll have a three-service application running and talking to each other.

This lab ties together everything from the workshop — images, networking, volumes, and health checks — into one running stack.

```bash
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

# Wait for services to become ready
echo "Waiting for database..."
sleep 10

# ═══════════════════════════════════════════════════
# CREATE THE API
# ═══════════════════════════════════════════════════

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

# ═══════════════════════════════════════════════════
# BUILD AND RUN THE API
# ═══════════════════════════════════════════════════

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

What you should see:

```json
{"database": "PostgreSQL 15.x on x86_64...", "service": "E-Commerce API", "visits": "1"}
{"database": "PostgreSQL 15.x on x86_64...", "service": "E-Commerce API", "visits": "2"}
{"database": "PostgreSQL 15.x on x86_64...", "service": "E-Commerce API", "visits": "3"}
```

The visit counter increments on each request (stored in Redis). The database version comes from Postgres. Three services talking to each other by name, on an isolated network, with persistent storage.

> **Congratulations!** You just built a multi-service application from scratch using only containers. This is the same architecture pattern used by real microservices in production.

### Cleanup script

```bash
#!/bin/bash
podman rm -f ecom-postgres ecom-redis ecom-api
podman network rm ecommerce-net
podman volume rm ecommerce-db ecommerce-redis
podman rmi ecom-api:1.0
echo "Cleanup complete!"
```

### Checkpoint

- How does the API find the database? (hint: DNS)
- What data survives if you destroy and recreate the containers?
- Which container needs a port published to the host? Why not the others?

---

# Security Wrap + Next Steps

You've built and deployed a multi-service stack. Before you go to production, there's one more topic: security. Most container breaches happen because of simple misconfigurations — running as root, exposing unnecessary ports, or baking secrets into images. This checklist keeps you safe.

## Container security checklist

![Container Security Checklist](assets/Container%20Security%20Checklist.png)

> **Beyond local runtime flags:** the security principles in this checklist are universal — they apply whether you run containers locally with Podman or Docker, or at scale on Kubernetes, Nomad, or a managed platform. In orchestrated environments, enforcement shifts from CLI flags to declarative manifests: Pod Security Standards replace `--cap-drop`, NetworkPolicies replace custom bridge networks, and Kubernetes Secrets or external vaults (Azure Key Vault, AWS Secrets Manager, HashiCorp Vault) replace runtime secret injection. The controls are the same — only the mechanism changes.

## Secure container launch

Here's what a production-hardened container launch looks like with a local runtime. Every flag has a purpose:

```bash
# Local runtime — production-secure launch
podman run \
  --name secure-app \
  --user 1000:1000 \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --memory 256m \
  --cpus 1 \
  --pids-limit 50 \
  --network custom-net \
  -p 127.0.0.1:8080:8080 \
  myapp:1.0
```

Each flag hardens the container in a specific way:

| Flag | Purpose |
|------|---------|
| `--user 1000:1000` | Run as non-root |
| `--read-only` | Prevent filesystem writes |
| `--tmpfs /tmp` | Allow temp files in memory |
| `--cap-drop ALL` | Remove all Linux capabilities |
| `--security-opt no-new-privileges` | Block privilege escalation |
| `--memory 256m` | Hard memory limit |
| `--cpus 1` | CPU limit |
| `--pids-limit 50` | Prevent fork bombs |
| `-p 127.0.0.1:8080:8080` | Bind to localhost only |

The same hardening expressed as a Kubernetes `securityContext` — the concepts map one-to-one:

```yaml
# Kubernetes — equivalent security controls in a Pod spec
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  containers:
    - name: app
      image: myapp:1.0
      securityContext:
        runAsNonRoot: true              # --user / non-root
        readOnlyRootFilesystem: true    # --read-only
        allowPrivilegeEscalation: false # --security-opt no-new-privileges
        capabilities:
          drop: ["ALL"]                 # --cap-drop ALL
      resources:
        limits:
          memory: "256Mi"               # --memory 256m
          cpu: "1"                       # --cpus 1
      ports:
        - containerPort: 8080
```

> **Tip:** On Kubernetes, cluster-level controls such as Pod Security Admission (Baseline / Restricted profiles), RBAC, and NetworkPolicies enforce these rules across every workload — no need to remember flags on every launch.

## What you've mastered

| Skill | Status |
|-------|--------|
| Container concepts & architecture | ✅ |
| Building images with Dockerfile | ✅ |
| Running and configuring containers | ✅ |
| Container networking | ✅ |
| Data persistence | ✅ |
| Multi-container apps | ✅ |
| Security best practices | ✅ |
| Troubleshooting | ✅ |

## Resources

Keep these bookmarked — you'll come back to them often:

- Podman Documentation: <https://docs.podman.io/>
- Kubernetes: <https://kubernetes.io/docs/>
- Container Security: <https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html>
- Azure Kubernetes Service: <https://azure.microsoft.com/en-us/services/kubernetes-service/>

---

# Appendix: Command Reference

This appendix is your cheat sheet. Print it, bookmark it, or keep it open in a second tab. Every command from the workshop is listed here, organized by category.

## Core commands

```bash
podman run -d -p 8080:80 nginx          # Run container detached with port mapping
podman ps                                 # List running containers
podman ps -a                              # List ALL containers (including stopped)
podman logs <container>                   # View container logs
podman logs -f <container>                # Follow logs (live)
podman logs --tail 50 <container>         # Last 50 lines
podman exec -it <container> /bin/sh       # Interactive shell
podman exec <container> ls -la /app       # Run single command
podman stop <container>                   # Graceful stop
podman rm <container>                     # Remove container
podman rm -f <container>                  # Force remove (stop + rm)
podman images                             # List images
podman rmi <image>                        # Remove image
podman build -t name:tag .                # Build image
```

## Inspect & copy

```bash
podman inspect <container>                        # Full JSON details
podman stats --no-stream <container>              # Resource usage
podman cp <container>:/app/logs ./logs            # Container → Host
podman cp ./config.json <container>:/app/         # Host → Container
```

## Networking essentials

```bash
podman network create <name>                      # Create custom network
podman network create --subnet 10.10.0.0/24 <name> # With specific subnet
podman network ls                                  # List networks
podman network inspect <name>                      # Network details
podman network rm <name>                           # Remove network
podman port <container>                            # Show port mappings
```

## Storage essentials

```bash
podman volume create <name>                        # Create volume
podman volume ls                                   # List volumes
podman volume inspect <name>                       # Volume details
podman volume rm <name>                            # Remove volume
podman volume prune                                # Remove unused volumes
```

## System diagnostics

```bash
podman info                                        # System-wide information
podman system df                                   # Disk usage summary
podman events --since 1h                           # Recent events
podman system prune -a --volumes                   # Full cleanup (caution!)
```

## Complete cleanup script

```bash
#!/bin/bash
# Stop all containers
podman stop $(podman ps -aq) 2>/dev/null

# Remove all containers
podman rm $(podman ps -aq) 2>/dev/null

# Remove workshop images
podman rmi $(podman images -q) 2>/dev/null

# Remove volumes and networks
podman volume prune -f
podman network prune -f

# Full cleanup
podman system prune -a --volumes -f

echo "Cleanup complete!"
```

## Congratulations

You started the day with zero container experience. Now you've:

- Built production-quality images with multi-stage Dockerfiles
- Wired up multi-service architectures with DNS-based discovery
- Proven data survives container destruction
- Applied security hardening techniques used in real production environments

You walk away with a solid mental model and the hands‑on skills to containerize your own projects. The natural next step? Pick one of your team's services and containerize it this week.
