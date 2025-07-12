SELECT "japanese_title"
AS "original title"
FROM "views"
WHERE "artist" = 'Hokusai'
ORDER BY "entropy" DESC LIMIT 1;
