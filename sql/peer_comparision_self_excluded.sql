
-- Demonstrates: CTEs, SUM/COUNT OVER (window aggregates), PARTITION BY, 
-- self-exclusion peer average, CASE WHEN, NULLIF null-safe division

-- Returns: A comparison of the fare paid by each passenger compared to the 
-- average-fare paid by their peer-group. The average-fare of this peer-group
-- excludes the passenger's own fare. The peers are grouped by sex and class.


WITH total_fare_per_sex_per_pclass AS(
    SELECT  *, 
        SUM(fare) OVER (PARTITION BY sex, pclass) total_fare, 
        COUNT(*) OVER (PARTITION BY sex, pclass) category_count
    FROM titanic
),
avg_fare_excl_own AS(
    SELECT *, (sib_sp + parch + 1) AS family_size,
        (total_fare-fare)/NULLIF(category_count-1,0) AS peer_avg_fare
    FROM total_fare_per_sex_per_pclass
)
SELECT name, pclass, sex, fare, family_size, 
    CASE 
        WHEN fare > peer_avg_fare THEN 'above'
        WHEN fare < peer_avg_fare THEN 'below'
        ELSE 'at par'
    END AS fare_comparison
FROM avg_fare_excl_own
WHERE family_size>=3
ORDER BY pclass, (fare-peer_avg_fare) DESC;