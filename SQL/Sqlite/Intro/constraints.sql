-- Common
---- NOT NULL -> 
---- UNIQUE  -> 
---- ENUMS

---POSTGRESQL
----- CHECK length>4 check length of a string
----- REGEX
----- min and maz

DROP TABLE STUDENTS;

-- --- ENUM TYPE
--CREATE TYPE gender AS ENUM ('MALE','FEMALE','OTHER');

-- -- CREATE STUDENTS TABLE

-- CREATE TABLE students(
--     id INTEGER PRIMARY KEY,
--     name VARCHAR(50) NOT NULL CHECK(LENGTH(name)>4),
--     email VARCHAR(250) NOT NULL UNIQUE CHECK(LENGTH(email)>4),
--     phone INTEGER NOT NULL UNIQUE,
--     gender TEXT CHECK(gender IN ('MALE','FEMALE','OTHER'))
-- )
