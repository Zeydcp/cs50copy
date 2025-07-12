CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "founded" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "companies" (
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "user_connections" (
    "user1_id" INTEGER CHECK ("user1_id" < "user2_id"),
    "user2_id" INTEGER CHECK ("user1_id" < "user2_id"),
    PRIMARY KEY("user1_id", "user2_id"),
    FOREIGN KEY("user1_id") REFERENCES "users"("id"),
    FOREIGN KEY("user2_id") REFERENCES "users"("id")
);

CREATE TABLE "school_connections" (
    "user_id" INTEGER,
    "school_id" INTEGER,
    "start" NUMERIC NOT NULL DEFAULT CURRENT_DATE CHECK ("start" < "end"),
    "end"  NUMERIC NOT NULL DEFAULT CURRENT_DATE CHECK ("start" < "end"),
    "type" TEXT NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")
);

CREATE TABLE "company_connections" (
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start" NUMERIC NOT NULL DEFAULT CURRENT_DATE CHECK ("start" < "end"),
    "end"  NUMERIC NOT NULL DEFAULT CURRENT_DATE CHECK ("start" < "end"),
    "title" TEXT NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "companies"("id")
);

