DROP TABLE IF EXISTS "ciphers";
DROP VIEW IF EXISTS "message";

CREATE TABLE "ciphers" (
    "sentence_id" INTEGER,
    "character" INTEGER,
    "length" INTEGER,
    FOREIGN KEY("sentence_id") REFERENCES "sentences"("id")
);

INSERT INTO "ciphers"
VALUES
    (14, 98, 4),
    (114, 3, 5),
    (618, 72, 9),
    (630, 7, 3),
    (932, 12, 5),
    (2230, 50, 7),
    (2346, 44, 10),
    (3041, 14, 5);

CREATE VIEW "message" AS
SELECT substr("sentence", "character", "length") AS "phrase"
FROM "sentences" JOIN "ciphers"
ON "sentences"."id" = "ciphers"."sentence_id";
