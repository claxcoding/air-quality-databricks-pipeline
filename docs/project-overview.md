Project Overview

This project builds a Databricks-based data pipeline to ingest, clean, and analyze air-quality data from Sensor.Community — an open network of citizen-operated environmental sensors.

Core Objectives

Ingest live sensor readings from the /data.json endpoint

Ingest historical monthly CSV archives

Store raw data in Bronze Delta tables

Clean and standardize sensor data in Silver tables

Produce aggregated metrics in Gold tables

Enable interactive exploratory analysis and visualization

Pipeline Architecture Overview

Ingestion Layer (Bronze)

Live JSON API data (PM2.5, PM10, temperature, humidity)

Historical CSVs (per month, per sensor type)

Processing Layer (Silver)

Schema enforcement

Deduplication

Timestamp normalization

Null handling

Analytics Layer (Gold)

Daily averages

Sensor reliability metrics

Location-based aggregation

SLA checks and data completeness