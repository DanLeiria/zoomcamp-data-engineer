# Module 1 - Data Ingestion

NYC Taxi data ingestion pipeline using Docker, PostgreSQL, and Python.

## Setup

**Start PostgreSQL and pgAdmin:**
```bash
docker-compose up
```

**Build ingestion image:**
```bash
docker build -t taxi-ingestion .
```

**Run ingestion:**
```bash
docker run -it --rm \
  --network module-1_default \
  taxi-ingestion \
  --pg-host=pgdatabase \
  --pg-user=root \
  --pg-pass=root \
  --pg-db=ny_taxi \
  --target-table=green_taxi_data
```

## Access

- **PostgreSQL**: `localhost:5432`
- **pgAdmin**: `http://localhost:8085` (admin@admin.com / root)

## Data

- Green taxi trips: `data/green_tripdata_2025-11.parquet`
- Zone lookup: `data/taxi_zone_lookup.csv` (Added separately using jupyter notebook)
