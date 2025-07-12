CREATE VIEW "june_vacancies" AS
SELECT "listings"."id", "property_type", "host_name", COUNT(*) AS "days_vacant"
FROM "listings" JOIN "availabilities"
ON "listings"."id" = "listing_id"
WHERE "date" LIKE '2023-06-__' AND "available" = 'TRUE'
GROUP BY "listing_id";
