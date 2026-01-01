# VaxChain

**Secure Vaccine Cold-Chain & Distribution Tracking System for Resource-Limited Settings**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![C#](https://img.shields.io/badge/C%23-.NET%208-512BD4?logo=dotnet)](https://dotnet.microsoft.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?logo=postgresql)](https://www.postgresql.org/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-ff4b4b?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

##  Project Overview

VaxChain is a full-stack health-tech application designed to ensure vaccine integrity from manufacturer to last-mile delivery, with a strong focus on resource-limited settings like Nigeria. It addresses the critical issue of cold-chain failures — responsible for up to **50% vaccine wastage** (NPHCDA estimates) — through real-time monitoring, tamper-evident logging, and actionable analytics.

This project demonstrates:
- **Python** for health-data analytics and interactive dashboards
- **C#/.NET 8** for secure, enterprise-grade medical registry APIs
- **PostgreSQL** for reliable, auditable data storage
- Full-stack systems architecture with cross-language integration

## Problem Statement

- High vaccine loss due to temperature excursions in the cold chain (2–8°C)
- Manual/paper-based tracking leads to errors, stock-outs, and poor traceability
- Lack of transparent, auditable systems erodes trust in immunization programs
- Existing solutions are often expensive and unsuitable for low-resource environments

##  Key Features

- **Batch Registration** – Track vaccine origin, lot number, expiry, and initial conditions
- **Temperature & Location Logging** – Real-time or manual sensor updates
- **Cold-Chain Breach Alerts** – Automatic detection and notification of temperature violations
- **Tamper-Evident Audit Trail** – Chained SHA-256 hashing + immutable logs
- **Secure Role-Based Access** – JWT authentication and granular permissions
- **Vaccine Administration Recording** – Link doses to patients with lot traceability
- **Interactive Dashboard** – Visualize batches, alerts, trends, and coverage using Streamlit
- **Analytics & Reporting** – Wastage trends, geographic insights, exportable reports

## Architecture

```
[Streamlit Dashboard (Python)]
          ↕️ (REST API - JWT Secured)
[C#/.NET 8 Secure Registry API]
          ↕️
[PostgreSQL Database]
          ↕️ (Read-only analytics queries)
[Python Analytics Engine]
```

##  Technology Stack

| Layer              | Technology                          | Purpose                                      |
|--------------------|-------------------------------------|----------------------------------------------|
| Database           | PostgreSQL 15+                      | ACID-compliant storage, JSONB logs, constraints |
| Secure Backend     | C#/.NET 8 Web API                   | Authentication, validation, audit logging    |
| Analytics & Dashboard | Python (Pandas, Plotly, Streamlit) | Data analysis, breach detection, visualization |
| Auth & Security    | JWT, RBAC                           | Role-based access control                    |
| Deployment         | Docker, Render/Heroku (free tier)   | Easy local and cloud deployment              |

##  Quick Start

### Prerequisites
- Python 3.10+
- .NET 8 SDK
- PostgreSQL 15+
- Docker (optional)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/VaxChain.git
   cd VaxChain
   ```

2. **Set up PostgreSQL**
   - Create a database: `vaxchain_db`
   - Update connection string in both apps (see `appsettings.json` and `.env`)

3. **Run the C# API**
   ```bash
   cd VaxChain.Api
   dotnet restore
   dotnet run
   ```
   API runs on `https://localhost:7001`

4. **Run the Python Dashboard & Analytics**
   ```bash
   cd VaxChain.Dashboard
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

5. **Docker (Optional)**
   ```bash
   docker-compose up --build
   ```

##  Development Roadmap (Completed MVP)

| Week | Milestone                    | Status |
|------|------------------------------|--------|
| 1    | Database Schema & Setup      |  Done  |
| 2    | Core Tracking & Hashing      |  Done  |
| 3    | Alerts, Auth & Analytics     |  Done  |
| 4    | Dashboard & Deployment       |  Done  |

## 🔮 Future Vision (Post-Capstone / Startup Roadmap)

This MVP is production-ready for demonstration and pilot deployments. The long-term vision includes:

- React + Mobile PWA frontend
- Real IoT sensor integration
- Predictive analytics (demand forecasting, outbreak correlation)
- National IIS & EHR integration (HL7 FHIR)
- Scalable cloud deployment (Kubernetes, Redis caching)
- Full regulatory compliance (HIPAA/GDPR equivalents)

Target impact: **30–50% reduction in vaccine wastage** across deployed regions.

##  Contributing

Contributions are welcome! Please open an issue first to discuss major changes.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

**VaxChain** – Building trust in immunization, one secure batch at a time. 💉🌍

*ALX Africa Health-Tech Capstone Project – January 2023*