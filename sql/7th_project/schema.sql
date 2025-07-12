-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

-- User info
CREATE TABLE "users" (
    "id" INTEGER,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "birth_date" NUMERIC,
    "address" TEXT,
    "country" TEXT,
    PRIMARY KEY("id")
);

-- User connections to other users
CREATE TABLE "friends" (
    "user1_id" INTEGER CHECK ("user1_id" < "user2_id"),
    "user2_id" INTEGER CHECK ("user1_id" < "user2_id"),
    PRIMARY KEY("user1_id", "user2_id"),
    FOREIGN KEY("user1_id") REFERENCES "users"("id"),
    FOREIGN KEY("user2_id") REFERENCES "users"("id")
);

-- Playlist info
CREATE TABLE "playlists" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "creation_date" NUMERIC,
    "original_owner_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("original_owner_id") REFERENCES "users"("id")
);

-- Associating playlists with people who own them
CREATE TABLE "playlist_owners" (
    "playlist_id" INTEGER,
    "user_id" INTEGER NOT NULL,
    FOREIGN KEY("playlist_id") REFERENCES "playlists"("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id")
);

-- Artist info
CREATE TABLE "artists" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "about" TEXT,
    PRIMARY KEY("id")
);

-- Album info
CREATE TABLE "albums" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "release_date" NUMERIC,
    "artist_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("artist_id") REFERENCES "artists"("id")
);

-- Song info
CREATE TABLE "songs" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "genre" TEXT,
    "description" TEXT,
    "length" NUMERIC,
    "streams" INTEGER,
    "release_date" NUMERIC,
    "artist_id" INTEGER,
    "album_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("artist_id") REFERENCES "artists"("id"),
    FOREIGN KEY("album_id") REFERENCES "albums"("id")
);

-- Songs contained in each playlist
CREATE TABLE "playlist_content" (
    "playlist_id" INTEGER,
    "song_id" INTEGER,
    FOREIGN KEY("playlist_id") REFERENCES "playlists"("id"),
    FOREIGN KEY("song_id") REFERENCES "songs"("id")
);

-- Podcast info
CREATE TABLE "podcasts" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "artist_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("artist_id") REFERENCES "artists"("id")
);

-- Podcast episodes info
CREATE TABLE "podcast_episodes" (
    "name" TEXT NOT NULL,
    "podcast_id" INTEGER NOT NULL,
    "length" NUMERIC,
    "genre" TEXT,
    "streams" INTEGER,
    FOREIGN KEY("podcast_id") REFERENCES "podcasts"("id")
);

-- Associates playlist with original owner each time a playlist is added
CREATE TRIGGER "log_original_owner"
AFTER INSERT ON "playlists"
FOR EACH ROW
BEGIN
    INSERT INTO "playlist_owners"
    VALUES (NEW."id", NEW."original_owner_id");
END;

-- Speeds up finding user info
CREATE INDEX "user_index" ON "users" ("username");

-- Speeds up adding and unadding friends
CREATE INDEX "friends_index" ON "friends" ("user1_id", "user2_id");

-- Speeds up view to find Trending new songs
CREATE INDEX "song_dates_index" ON "songs" ("release_date");

-- Finds 50 most streamed songs that came out in the last month
CREATE VIEW "trending_new_songs" AS
SELECT "name", "streams"
FROM "songs"
WHERE julianday(CURRENT_DATE) - julianday("release_date") < 31
ORDER BY "streams" DESC
LIMIT 50;

-- Finds 50 most owned playlists
CREATE VIEW "most_popular_playlists" AS
SELECT "name", COUNT(*) AS "owners"
FROM "playlists" JOIN "playlist_owners"
ON "playlists"."id" = "playlist_owners"."playlist_id"
GROUP BY "playlists"."id"
ORDER BY "owners" DESC
LIMIT 50;

-- Finds 50 most streamed songs
CREATE VIEW "most_streamed_songs" AS
SELECT "name", "streams"
FROM "songs"
ORDER BY "streams" DESC
LIMIT 50;

-- Finds 50 most streamed albums
CREATE VIEW "most_streamed_albums" AS
SELECT "name", SUM("streams") AS "streams"
FROM "albums" JOIN "songs"
ON "albums"."id" = "songs"."album_id"
GROUP BY "albums"."id"
ORDER BY "streams" DESC
LIMIT 50;

-- Finds 50 most streamed podcasts
CREATE VIEW "most_streamed_podcasts" AS
SELECT "name", SUM("streams") AS "streams"
FROM "podcasts" JOIN "podcast_episodes"
ON "podcasts"."id" = "podcast_episodes"."podcast_id"
GROUP BY "podcasts"."id"
ORDER BY "streams" DESC
LIMIT 50;
