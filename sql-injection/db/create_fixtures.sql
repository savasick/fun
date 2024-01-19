CREATE TABLE IF NOT EXISTS numbers (
    number BIGINT,
    timestamp BIGINT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username varchar(30),
    admin boolean
);

INSERT INTO users
    (username, admin)
VALUES
    ('savasick', true),
    ('broller', false),
    ('parrot', false),
    ('kali', false),
    ('haki', false);