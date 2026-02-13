# Containers Fundamentals — From Zero to Confidence

[![Open in MOAW](https://img.shields.io/badge/Open%20in-MOAW-blue)](https://moaw.dev/workshop/?src=gh:akafraitane/docker-for-beginners-lab/main/docs/)

A hands-on workshop that takes you from zero container experience to confidently building, shipping, and operating multi-service applications with **Podman** (and Docker). Every section drops you into a realistic scenario — you learn by solving real problems.

## 🎯 Workshop Overview

**The story:** You just joined a team that ships a small API. It runs fine on dev laptops but breaks everywhere else. Your mission: containerize it, wire it to a database and a cache, prove the data survives a crash, and lock it down — all before the end of the day.

### What You'll Learn

- Container architecture — images, layers, namespaces, cgroups
- Building production-quality images — multi-stage builds, non-root, healthchecks
- Running, inspecting, and operating containers
- Container networking — custom bridges, DNS-based service discovery
- Data persistence — named volumes, bind mounts, database survival
- Multi-container stacks — Postgres + Redis + Flask API capstone
- Security best practices — least privilege, read-only root, capability drops

### Duration

**Full day** — ~8 hours

### Target Audience

- Developers new to containers
- DevOps beginners
- System administrators
- Anyone wanting to learn container fundamentals

## 📋 Prerequisites

- **OS:** Windows 10/11, macOS 12+, or Linux (Ubuntu 22.04+)
- **Hardware:** 8 GB RAM (16 GB recommended), ~25 GB free disk
- **Tools:** VS Code + Docker extension recommended
- **Skills:** Basic command-line familiarity

## 🚀 Getting Started

### Option 1: View Online (Recommended)

Open the workshop in MOAW (Microsoft OpenSource Academy Workshops):

👉 [**Open Workshop**](https://moaw.dev/workshop/?src=gh:akafraitane/docker-for-beginners-lab/main/docs/)

### Option 2: Run Locally

```bash
git clone https://github.com/akafraitane/docker-for-beginners-lab.git
cd docker-for-beginners-lab
```

Open `docs/workshop.md` in your favorite Markdown viewer.

## 📁 Repository Structure

```
docker-for-beginners-lab/
├── docs/
│   ├── workshop.md          # Full workshop content (all labs inline)
│   └── assets/              # Images and diagrams
├── LICENSE
└── README.md
```

> All exercise code (Dockerfiles, Python files, scripts) is created inline during the labs — no separate exercise folders needed.

## 📖 Workshop Agenda

| Time | Topic |
|------|-------|
| 09:00 – 09:30 | Kickoff: Why Containers |
| 09:30 – 10:00 | Setup: Podman Environment |
| 10:00 – 10:45 | Launch Your First Container |
| 10:45 – 11:00 | ☕ Break |
| 11:00 – 11:30 | Concepts Deep Dive |
| 11:30 – 12:30 | Package Your Own API |
| 12:30 – 13:30 | 🍽️ Lunch |
| 13:30 – 14:15 | Operate Containers |
| 14:15 – 15:15 | Connect Services (Networking) |
| 15:15 – 15:30 | ☕ Break |
| 15:30 – 16:30 | Persist Data + Capstone Stack |
| 16:30 – 17:00 | Security Wrap + Next Steps |
| 17:00 – 17:30 | Q&A & Wrap-up |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This workshop is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👨‍🏫 Author

**Abdoul-Hakim Afraitane** — Microsoft Cloud Solution Architect · [LinkedIn](https://www.linkedin.com/in/abdoul-hakim-afraitane/)

---