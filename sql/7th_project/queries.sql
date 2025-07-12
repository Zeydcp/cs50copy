-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

-- Find trending new songs
SELECT *
FROM "trending_new_songs";

-- Find most popular playlists
SELECT *
FROM "most_popular_playlists";

-- Find most streamed songs
SELECT *
FROM "most_streamed_songs";

-- Find most streamed albums
SELECT *
FROM "most_streamed_albums";

-- Find most streamed podcasts
SELECT *
FROM "most_streamed_podcasts";

-- New user is created
INSERT INTO "users" ("username", "password", "email", "birth_date", "address", "country")
VALUES ('newuser', 'boo!', 'newuser@email.com', '2002-05-03', '123 Happy Street', 'United States'),
('seconduser', 'password', 'seconduser@email.com', '2002-05-15', '59 Spotify Street', 'India');

-- Both users add each other
INSERT INTO "friends"
SELECT
    (SELECT "id" FROM "users" WHERE "username" = 'newuser'),
    (SELECT "id" FROM "users" WHERE "username" = 'seconduser');

-- New song is added
INSERT INTO "songs" ("name", "genre", "description", "length", "release_date")
VALUES (
    'Power',
    'Rap',
    'In the song, Kanye pokes fun at his haters, criticizes the United States',
    '00-04-52',
    '2010-05-28'
);

-- Update password for a user
UPDATE "users"
SET "password" = 'changed!'
WHERE "username" = 'newuser';

-- Delete friendship between two people
DELETE FROM "friends"
WHERE "user1_id" = (
    SELECT "id"
    FROM "users"
    WHERE "username" = 'newuser'
) AND "user2_id" = (
    SELECT "id"
    FROM "users"
    WHERE "username" = 'seconduser'
);
