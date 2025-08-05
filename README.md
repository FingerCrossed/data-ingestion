# Supply Chain Ingestion Pipeline

This project simulates a scalable ingestion pipeline for global supply chain data. It covers ingestion, validation, and observability across the full path from raw CSV/JSON files to a data warehouse.

---

## 🔧 Tech Stack

- **Kafka** for streaming ingestion
- **Apache Spark (PySpark)** for ETL transformation
- **Apache Airflow** for orchestration and SLA monitoring
- **Snowflake** as the data warehouse
- **FastAPI** for exposing lineage and SLA metadata
- **Databricks** for local notebook testing and job runs

---

## 📁 Project Structure


supply-chain-ingestion-pipeline/

├── dags/                   ← Airflow DAGs

├── kafka_producer/        ← Kafka producer scripts

├── spark_jobs/            ← ETL with PySpark

├── api/                   ← Lineage APIs with FastAPI

├── data/                  ← Sample input files (CSV/JSON)

├── ingestion_log/         ← Log schema, data, and queries

├── config/                ← Region-based config files

├── notebooks/             ← Databricks notebooks for testing


---

## ✅ Features

- Multi-region file-based ingestion (SAP / Teradata to S3)
- Real-time Kafka publishing + ingestion logs
- PySpark validation and deduplication
- SLA breach monitoring via Airflow and Slack
- Lineage API for pipeline health and metadata

---

## 📦 Python Requirements


kafka-python
pyspark
fastapi
uvicorn
pydantic
snowflake-connector-python
sqlalchemy
python-dotenv
slack_sdk
