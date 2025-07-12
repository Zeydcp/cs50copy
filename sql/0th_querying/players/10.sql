SELECT "first_name", "last_name", ("weight"*703/"height"/"height")
AS "BMI" FROM "players"
WHERE "birth_country" = 'USA' AND "height" IS NOT NULL
AND "weight" IS NOT NULL ORDER BY "BMI" DESC LIMIT 10;
