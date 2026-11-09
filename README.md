```markdown
# SEN 401: Software Configuration Management and Maintenance

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-teal.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Comprehensive laboratory practical project demonstrating full-lifecycle **Software Configuration Management (SCM)**, version control workflows, maintenance taxonomy, status accounting, configuration auditing, system re-engineering, data migration, and containerized deployment using modern engineering tools.

---

## 📂 Repository Directory Structure

```text
sen401-scm-project/
├── Lab1_2/                     # Labs 1 & 2: Baseline SCM Setup & Maintenance
│   ├── app.py                  # Main student analytics demo script
│   ├── students.py             # Pydantic v2 data models & validation
│   ├── requirements.txt        # Project dependencies (pydantic, fastapi, etc.)
│   └── utils/
│       └── helpers.py          # Statistical helper functions (highest, lowest, median)
├── Lab3/                       # Lab 3: Status Accounting & Auditing
│   ├── app.py                  # Inventory asset valuation dashboard
│   ├── inventory.py            # Warehouse stock data module
│   ├── changelog.txt           # Automated Git commit logs and version history
│   └── utils/
│       └── helpers.py          # Stock sorting and bounds checking utilities
├── Lab4/                       # Lab 4: Re-Engineering, Migration & Containerization
│   ├── Dockerfile              # Container image configuration for FastAPI service
│   ├── docker-compose.yml      # Multi-container orchestration manifest
│   ├── requirements.txt        # FastAPI and SQLAlchemy dependencies
│   └── app/
│       ├── __init__.py         # Package initialization
│       ├── database.py         # SQLite connection and session management
│       ├── models.py           # SQLAlchemy ORM database models
│       └── main.py             # FastAPI RESTful endpoints (CRUD operations)
└── README.md                   # Project documentation

```

---

## 🚀 Lab Overview & Implementation Details

### Lab 1: SCM Setup & Baseline Creation (`v1.0`)

* **Objective:** Establish a robust Software Configuration Management environment.
* **Key Deliverables:** Modular Python script structure (`app.py`, `students.py`, `utils/helpers.py`), private GitHub repository setup, branch creation (`main`, `dev`, `feature/*`), and release tagging (`v1.0`).

### Lab 2: Software Maintenance Tasks (`v1.1`)

* **Objective:** Execute systematic software maintenance across four key dimensions:
1. **Corrective:** Added robust bounds checking and error handling for empty student lists.
2. **Adaptive:** Upgraded codebase for Python 3.12 compatibility and integrated Pydantic v2 for data validation.
3. **Perfective:** Enhanced console formatting and added cohort median score calculation.
4. **Preventive:** Refactored module logic, added comprehensive docstrings, and tagged release `v1.1`.



### Lab 3: Status Accounting & Auditing

* **Objective:** Track and document changes using Git configuration status accounting (CSA).
* **Key Deliverables:** Inventory asset valuation script (`inventory.py`), structured Git change logs (`changelog.txt`), and configuration item (CI) traceability mapping commits to maintenance milestones.

### Lab 4: Re-Engineering & Migration

* **Objective:** Modernize and re-engineer legacy script storage into a scalable architecture.
* **Key Deliverables:**
* Migrated flat file storage to a relational **SQLite database** using **SQLAlchemy ORM**.
* Re-architected local logic into a high-performance **FastAPI RESTful web service**.
* Created a production-ready **`Dockerfile`** and **`docker-compose.yml`** for reproducible container orchestration.



---

## ⚙️ Quickstart & Local Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/sen401-scm-project.git](https://github.com/YOUR_USERNAME/sen401-scm-project.git)
cd sen401-scm-project

```


2. **Run Labs 1 & 2 (Student Analytics):**
```bash
cd Lab1_2
pip install -r requirements.txt
python app.py

```


3. **Run Lab 3 (Inventory Accounting):**
```bash
cd ../Lab3
python app.py

```


4. **Run Lab 4 (FastAPI Service):**
```bash
cd ../Lab4
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

```


* Access interactive API documentation at: `http://localhost:8000/docs`



---

## 👥 Author

* **Marvelous Kalu**
* **Institution:** Miva Open University
