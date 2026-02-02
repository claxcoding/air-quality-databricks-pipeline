README.md (Phase 1 version)
Air Quality Data Pipeline on Databricks

This project is an end-to-end data engineering pipeline built on Databricks Community Edition.
It ingests, processes, and analyzes air-quality measurements from the Sensor.Community open environmental sensor network.

The pipeline follows the Medallion Architecture:

Bronze: Raw ingestion from API & monthly archives

Silver: Cleaning, normalization & deduplication

Gold: Aggregated analytics for dashboards

Technologies used:

Databricks (Community Edition)

Delta Lake

PySpark / Python 3.10+

Databricks Workflows (optional)

Type-hinted Python modules

Sensor.Community public API and CSV archives

The goal of this project is to showcase:

Scalable ingestion

Distributed data processing

Data modeling & quality checks

Documentation & engineering best practices

Repository structure (Phase 1):

air-quality-databricks-pipeline/
│
├── README.md
├── docs/
│   ├── architecture.png
│   ├── data-model.md
│   └── project-overview.md
│
├── src/
│   └── utils.py
│
├── notebooks/
│   └── 01_setup_environment.py
│
└── data/  (ignored)
