# WeatherPipe
Airflow + PostgreSQL + dbt (Docker Compose)

This repository contains a local data orchestration setup using Apache Airflow, PostgreSQL, and dbt, all running with Docker Compose.

This setup is intended for local development and testing only.

---

Services Overview

1. PostgreSQL (db)
- Acts as the primary database
- Used by Airflow and dbt
- Initialized using a SQL script
- Persists data on the host machine
- Image: postgres:15.15-bookworm
- Port: localhost:5000 → 5432

2. Apache Airflow (af)
- Runs Airflow in standalone mode
- Uses LocalExecutor
- Loads DAGs from the host filesystem
- Can run Docker containers using DockerOperator
- Image: apache/airflow:3.1.7
- Web UI: http://localhost:8000

3. dbt (dbt)
- Runs dbt models against PostgreSQL
- Uses official dbt Postgres image
- Executes dbt run on startup
- Image: ghcr.io/dbt-labs/dbt-postgres:1.9.latest

---

Project Structure

.
├── docker-compose.yml
├── airflow/
│   └── dags/
│       └── dbt_orchestrator.py
├── api-request/
│   └── insert_record.py
├── postgres/
│   ├── data/
│   └── airflow_init.sql
├── dbt/
│   ├── my_project/
│   └── profiles.yml
└── README.txt

---

Networking

All services use the same Docker bridge network: my-network

Containers can communicate using service names (e.g., db).

---

PostgreSQL Configuration

Environment variables:
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
POSTGRES_DB=db

Initialization script: ./postgres/airflow_init.sql

Persistent data directory: ./postgres/data

---

Airflow Configuration

DAGs: ./airflow/dags → /opt/airflow/dags
Custom Python code: ./api-request → /opt/airflow/api-request
DockerOperator support: /var/run/docker.sock → /var/run/docker.sock

---

dbt Configuration

Project directory: ./dbt/my_project → /usr/app
Profiles directory: ./dbt → /root/.dbt
Command executed: dbt run

---

Running the Project

Start all services: docker compose up -d
Stop all services: docker compose down
Rebuild images: docker compose build

---

Useful Commands

View Airflow logs: docker compose logs -f af
Open a shell in Airflow container: docker exec -it airflow_container bash
Verify Docker access: docker exec -it airflow_container docker ps

---

Notes

- Local development only
- Docker socket gives Airflow full Docker access
- Credentials are not secure
- Not for production

---

Requirements

- Docker Desktop
- Docker Compose v2
- WSL2 (recommended on Windows)

---

License

MIT
