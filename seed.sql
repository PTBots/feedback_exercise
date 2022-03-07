DROP DATABASE IF EXISTS feedback_exercise;

CREATE DATABASE feedback_exercise;

\c feedback_exercise;

CREATE TABLE users 
(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);