SELECT "name", "unsatisfactory"
FROM "districts"
JOIN "staff_evaluations" ON "districts"."id" = "staff_evaluations"."district_id"
ORDER BY "unsatisfactory" DESC
LIMIT 10;
