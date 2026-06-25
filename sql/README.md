# SQL Queries

Analytical SQL written against a Postgres database loaded with the Titanic
dataset (891 passenger records). Built while learning SQL, progressing from
basic aggregation to window functions and multi-CTE analytics.

## Setup

These queries run against a Postgres instance with a `titanic` table. To
reproduce:

```bash
docker run --name learning-postgres -e POSTGRES_PASSWORD=learnsql \
  -e POSTGRES_DB=titanic -p 5432:5432 -d postgres:16
docker cp titanic.csv learning-postgres:/tmp/titanic.csv
# then \copy the CSV into a titanic table (see schema in load.sql)
```

## Queries

| File | Demonstrates |
|------|--------------|
| `peer_comparison_self_excluded.sql` | CTEs, window aggregates, self-exclusion peer average, CASE WHEN, NULLIF |

## Notes

Each file has a header comment describing what it demonstrates and returns.
Queries use the Titanic dataset purely as a learning vehicle — the techniques
(peer comparison, top-N-per-group, ranking) map directly to real analytical
work like anomaly detection and cohort benchmarking.