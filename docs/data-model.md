# Data Model – Air Quality Data Pipeline

This document describes the logical and physical data model used in the
Bronze → Silver → Gold architecture of the air quality data pipeline.

---

## Bronze Layer

### Table: `air_quality_bronze.live_sensor_raw`

**Purpose**
- Store raw, unmodified JSON payloads from the sensor.community API
- Append-only ingestion for traceability and replayability

**Grain**
- One row per sensor record per ingestion batch

| Column Name   | Data Type   | Description |
|--------------|------------|-------------|
| raw_json     | STRING     | Raw JSON payload from the API |
| ingested_at  | TIMESTAMP  | UTC timestamp of ingestion |
| source       | STRING     | Data source identifier |
| batch_id     | STRING     | Unique batch identifier |

---

## Silver Layer

### Table: `air_quality_silver.sensor_measurements`

**Purpose**
- Structured, deduplicated, and validated sensor measurements
- Preserve invalid records using quality metadata

**Grain**
- One row per `(sensor_id, measurement_ts, measurement_type)`

| Column Name        | Data Type   | Description |
|-------------------|------------|-------------|
| sensor_id         | STRING     | Unique sensor identifier |
| sensor_type       | STRING     | Sensor model/type |
| location_id       | STRING     | Logical location identifier |
| country           | STRING     | Country code |
| latitude          | DOUBLE     | Latitude |
| longitude         | DOUBLE     | Longitude |
| measurement_type  | STRING     | Measurement type (`P1`, `P2`) |
| measurement_value | DOUBLE     | Measured PM value |
| measurement_ts    | TIMESTAMP  | Measurement timestamp |
| ingested_at       | TIMESTAMP  | Ingestion timestamp |
| quality_flag      | STRING     | `OK` or `BAD` |
| quality_reason    | STRING     | Reason for quality classification |

**Quality Rules Applied**
- Non-negative PM values
- PM2.5 ≤ 1.2 × PM10
- Upper physical bounds
- Deterministic deduplication (latest ingested record wins)

---

## Gold Layer

### Table: `air_quality_gold.daily_air_quality`

**Purpose**
- Daily, location-level aggregates for Python analytics
- Uses only physically plausible (`quality_flag = 'OK'`) data

**Grain**
- One row per `(date, location_id)`

| Column Name   | Data Type | Description |
|--------------|----------|-------------|
| date         | DATE     | Aggregation date |
| location_id | STRING   | Location identifier |
| country     | STRING   | Country code |
| latitude    | DOUBLE   | Latitude |
| longitude   | DOUBLE   | Longitude |
| pm10_avg    | DOUBLE   | Average PM10 |
| pm25_avg    | DOUBLE   | Average PM2.5 |
| pm10_count  | BIGINT   | Count of PM10 records |
| pm25_count  | BIGINT   | Count of PM2.5 records |
| sensors     | BIGINT   | Distinct sensors contributing |
| measurements| BIGINT   | Total contributing measurements |

---

### Table: `air_quality_gold.latest_sensor_snapshot`

**Purpose**
- Latest valid measurement per sensor
- Optimized for dashboard visualization

**Grain**
- One row per sensor

| Column Name    | Data Type | Description |
|---------------|----------|-------------|
| sensor_id     | STRING   | Sensor identifier |
| sensor_type   | STRING   | Sensor model/type |
| location_id   | STRING   | Location identifier |
| country       | STRING   | Country |
| latitude      | DOUBLE   | Latitude |
| longitude     | DOUBLE   | Longitude |
| pm10          | DOUBLE   | Latest PM10 value |
| pm25          | DOUBLE   | Latest PM2.5 value |
| measurement_ts| TIMESTAMP| Timestamp of latest measurement |
| ingested_at   | TIMESTAMP| Ingestion timestamp |
| date          | DATE     | Measurement date |

---

## Design Principles

- **Immutability in Bronze**
- **Validation, not deletion, in Silver**
- **Analytics-optimized modeling in Gold**
- **Clear separation of historical analytics vs. real-time snapshots**
