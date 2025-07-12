
-- *** The Lost Letter ***
-- Find package id where the content congratulates
SELECT "id"
FROM "packages"
WHERE "contents" LIKE '%congratulatory%';
-- Produces package id 384

-- Find address id where package with that id was dropped
SELECT "address_id"
FROM "scans"
WHERE "package_id" = 384 AND "action" = 'Drop';
-- Produces address id 854

-- Find address type and name corresponding to that address id
SELECT "type", "address"
FROM "addresses"
WHERE "id" = 854;

-- *** The Devious Delivery ***
-- Find contents and package id that has no from address
SELECT "contents", "id"
FROM "packages"
WHERE "from_address_id" IS NULL;
-- Produces package id 5098

-- Find address id where package with that id was dropped
SELECT "address_id"
FROM "scans"
WHERE "package_id" = 5098 AND "action" = 'Drop';
-- Produces address id 348

-- Find address type corresponding to that address id
SELECT "type",
FROM "addresses"
WHERE "id" = 348;

-- *** The Forgotten Gift ***
-- Find address id that package was sent from
SELECT "id"
FROM "addresses"
WHERE "address" = '109 Tileston Street';
-- Produces address id 9873

-- Find contents and package id of the package using address id
SELECT "contents", "id"
FROM "packages"
WHERE "from_address_id" = 9873;
-- Produces package id 9523

-- Find last driver id corresponding to that package id
SELECT "driver_id"
FROM "scans"
WHERE "package_id" = 9523
ORDER BY "timestamp" DESC LIMIT 1;
-- Produces address id 17

-- Find name of driver with that id
SELECT "name"
FROM "drivers"
WHERE "id" = 17;
