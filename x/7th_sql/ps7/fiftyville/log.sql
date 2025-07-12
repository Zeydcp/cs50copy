-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check all tables in database
.tables

-- Looking for a crime scene report that matches the date and the location of the crime
.schema crime_scene_reports

SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- Crime happened at 10:15 am, 3 witnesses

-- Check interviews of 3 witnesses
.schema interviews

SELECT transcript
  FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28;
-- Look for cars that left the bakery within ten minutes of crime
-- Thief withdrew money from ATM on Leggett Street earlier that morning
-- Thief asked friend to purchase earliest flight ticket out of Fiftyville on 29th, duration of call less than a minute

-- Check bakery footage
.schema bakery_security_logs

SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021 AND month = 7
AND day = 28 AND hour = 10
AND minute > 15 AND minute < 25
AND activity = 'exit';
-- Thief drove a car with one of these 8 plates.

-- Check ATM transactions
.schema atm_transactions

SELECT id, account_number, amount
FROM atm_transactions
WHERE year = 2021 AND month = 7
AND day = 28 AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';
-- 8 different account number possibilites

-- Check phone_calls
.schema phone_calls

SELECT caller, receiver
FROM phone_calls
WHERE year = 2021 AND month = 7
AND day = 28 AND duration < 60;
-- 9 possibilites of having the right phone call

-- Check flights
.schema flights

SELECT id, destination_airport_id
FROM flights
WHERE year = 2021 AND month = 7
AND day = 29 ORDER BY hour, minute LIMIT 1;
-- id 36 and destination id is 4

-- Check airports
.schema airports

SELECT city
FROM airports
WHERE id = 4;
-- Destination is New York City

-- Check passengers
.schema passengers

SELECT passport_number
FROM passengers
WHERE flight_id = 36;
-- 2 out of 8 possibilities are who we are looking for


-- Check for name by merging all information gathered
.schema people


SELECT name AS Thief, phone_number
FROM people
WHERE phone_number = (
    SELECT phone_number
    FROM people
    WHERE passport_number IN (
        SELECT passport_number
        FROM passengers
        WHERE flight_id = 36)
    AND license_plate IN (
        SELECT license_plate
        FROM bakery_security_logs
        WHERE year = 2021 AND month = 7
        AND day = 28 AND hour = 10
        AND minute > 15 AND minute < 25
        AND activity = 'exit')
    AND (phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE year = 2021 AND month = 7
        AND day = 28 AND duration < 60)
        OR phone_number IN (
        SELECT receiver
        FROM phone_calls
        WHERE year = 2021 AND month = 7
        AND day = 28 AND duration < 60))
    AND id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
            SELECT account_number
            FROM atm_transactions
            WHERE year = 2021 AND month = 7
            AND day = 28 AND atm_location = 'Leggett Street'
            AND transaction_type = 'withdraw')));
-- This gives us the name Bruce, who is the thief. To get Bruce's friend, we can link them with their phone call.
-- We know Bruce's phone number so the other number in the call must be Bruce's accomplice

-- Check their call
SELECT caller, receiver
FROM phone_calls
WHERE (
    caller = '(367) 555-5533'
    OR receiver = '(367) 555-5533')
AND year = 2021 AND month = 7
AND day = 28 AND duration < 60;
-- This tells us that Bruce was the caller so the receiver's number must be the accomplice

-- Now to link a phone number to a name
SELECT name
FROM people
WHERE phone_number = '(375) 555-8161';
-- This gives us the name Robin