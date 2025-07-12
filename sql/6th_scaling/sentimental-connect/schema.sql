CREATE TABLE `users` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `first_name` VARCHAR(32) NOT NULL,
    `last_name` VARCHAR(32) NOT NULL,
    `username` VARCHAR(16) NOT NULL UNIQUE,
    `password` VARCHAR(16) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `schools` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `type` ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL,
    `location` VARCHAR(32) NOT NULL,
    `founded` SMALLINT NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `companies` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `industry` ENUM('Technology', 'Education', 'Business') NOT NULL,
    `location` VARCHAR(32) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `user_connections` (
    `user1_id` INT UNSIGNED,
    `user2_id` INT UNSIGNED,
    CHECK (`user1_id` < `user2_id`),
    PRIMARY KEY(`user1_id`, `user2_id`),
    FOREIGN KEY(`user1_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`user2_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `school_connections` (
    `user_id` INT UNSIGNED,
    `school_id` INT UNSIGNED,
    `start` DATE NOT NULL DEFAULT (CURRENT_DATE),
    `end`  DATE NOT NULL DEFAULT (CURRENT_DATE),
    `type` VARCHAR(4) NOT NULL,
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `schools`(`id`),
    CHECK (`start` < `end`)
);

CREATE TABLE `company_connections` (
    `user_id` INT UNSIGNED,
    `company_id` INT UNSIGNED,
    `start` DATE NOT NULL DEFAULT (CURRENT_DATE),
    `end`  DATE NOT NULL DEFAULT (CURRENT_DATE),
    `title` VARCHAR(32) NOT NULL,
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`company_id`) REFERENCES `companies`(`id`),
    CHECK (`start` < `end`)
);
