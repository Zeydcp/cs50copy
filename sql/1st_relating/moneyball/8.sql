SELECT "salary"
FROM "salaries" JOIN "performances"
ON "salaries"."player_id" = "performances"."player_id"
AND "salaries"."year" = "performances"."year"
WHERE "salaries"."year" = 2001
ORDER BY "HR" DESC
LIMIT 1;
