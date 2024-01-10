


-- ALTER TABLE students ADD COLUMN 
-- parent_name VARCHAR(60);

-- CREATE TABLE temp_students AS SELECT email,'name',gender,parent_name
-- FROM students;

-- DROP TABLE students;

-- ALTER TABLE temp_students RENAME to students


-- 10 students. 
-- CREATE TABLE students(
--     id INTEGER PRIMARY KEY,
--     name VARCHAR(50) NOT NULL CHECK(LENGTH(name)>4),
--     email VARCHAR(250) NOT NULL UNIQUE CHECK(LENGTH(email)>4),
--     phone INTEGER NOT NULL UNIQUE,
--     gender TEXT CHECK(gender IN ('MALE','FEMALE','OTHER'))
-- )

-- Add column. Twigger account ->  ADD COLUMN NULL
-- ALTER UNIQUE