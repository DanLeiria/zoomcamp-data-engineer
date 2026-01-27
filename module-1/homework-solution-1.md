
## Question 1. Understanding Docker images

Open Docker in the terminal:
```bash
open -a Docker
```

Run the image with bash as entrypoint:
```bash
docker run -it \
    --rm \
    --entrypoint=bash \
    python:3.13-slim
```
Check pip version:
```bash
pip --version

pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```

Exit the container in the terminal (and it is automatically removed):
```bash
exit
```

**Answer: 25.3**

## Question 2. Understanding Docker networking and docker-compose

The `hostname` used to connect to the postgres database is `db`, and the `port` is 5432 referenced in the db.

**Answer: db:5432**

## Question 3. Counting short trips

```sql
SELECT COUNT(*)
FROM public.green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
```

**Answer: 8,007**

## Question 4. Longest trip for each day

```sql
SELECT 
    DATE(lpep_pickup_datetime) AS pickup_day,
    MAX(trip_distance) AS longest_trip
FROM public.green_taxi_trips
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY longest_trip DESC
LIMIT 1;
```

**Answer: 2025-11-14**

## Question 5. Biggest pickup zone

```sql
SELECT 
    tz."Zone",
    SUM(gt.total_amount) AS total_revenue
FROM public.green_taxi_trips gt
JOIN public.taxi_zones tz ON gt."PULocationID" = tz."LocationID"
WHERE DATE(gt.lpep_pickup_datetime) = '2025-11-18'
GROUP BY tz."Zone"
ORDER BY total_revenue DESC
LIMIT 1;
```

**Answer: East Harlem North**

## Question 6. Largest tip

```sql
SELECT 
    tz_dropoff."Zone" AS dropoff_zone,
    MAX(gt.tip_amount) AS largest_tip
FROM public.green_taxi_trips gt
JOIN public.taxi_zones tz_pickup ON gt."PULocationID" = tz_pickup."LocationID"
JOIN public.taxi_zones tz_dropoff ON gt."DOLocationID" = tz_dropoff."LocationID"
WHERE tz_pickup."Zone" = 'East Harlem North'
  AND gt.lpep_pickup_datetime >= '2025-11-01'
  AND gt.lpep_pickup_datetime < '2025-12-01'
GROUP BY tz_dropoff."Zone"
ORDER BY largest_tip DESC
LIMIT 1;
```

**Answer: Yorkville West**

## Question 7. Terraform Workflow

**Answer: terraform init, terraform apply -auto-approve, terraform destroy**
