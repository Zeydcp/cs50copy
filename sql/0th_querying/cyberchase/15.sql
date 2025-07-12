SELECT SUBSTR("air_date", 1, 4) AS year, MIN(SUBSTR("air_date", 6, 5)) AS day
FROM "episodes" GROUP BY "year";
