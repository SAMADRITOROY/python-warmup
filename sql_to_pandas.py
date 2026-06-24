from sqlalchemy import create_engine
import pandas as pd

conn = create_engine("postgresql://postgres:learnsql@localhost:5432/titanic")
query = """
WITH fare_ranks_per_port AS (
    SELECT pclass, name, embarked, fare, 
        DENSE_RANK() OVER (PARTITION BY embarked ORDER BY fare desc) AS dense_rank 
    FROM titanic
),
fare_ranks_per_port_with_avg_fare AS (
    SELECT pclass, name, embarked, fare, dense_rank,
        AVG(fare) OVER (PARTITION BY embarked) AS avg_fare
    FROM fare_ranks_per_port
)
SELECT pclass, name, embarked, fare
FROM fare_ranks_per_port_with_avg_fare 
WHERE avg_fare>20 AND dense_rank=1 
ORDER BY fare DESC;
"""
df = pd.read_sql(query, conn)
print(df)