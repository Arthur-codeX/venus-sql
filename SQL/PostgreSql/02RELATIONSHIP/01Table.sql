

-- Student, subjects <JOIN TABLE:student_subject> ---> MANY MANY
-- Student Parent  MANY ONE
-- STUDENT ADDERESS ONE TO ONE 

-- student

-- DROP TABLE IF EXISTS 
-- address,
-- subject,
-- parent,
-- student,
-- subject_student
-- ;

CREATE TABLE IF NOT EXISTS address(
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    pobox VARCHAR (255) NOT NULL
);

-- CREATE TABLE IF NOT EXISTS subject(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     code VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS parent(
--      id SERIAL PRIMARY KEY,
--      name VARCHAR(255) NOT NULL
-- );

--
-- 

CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent_id INTEGER REFERENCES parent(id),
    address_id INTEGER NOT NULL UNIQUE REFERENCES address(id)
    
 );

 CREATE  TABLE IF NOT EXISTS student_subject(
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES student(id),
    subject_id INTEGER NOT NULL REFERENCES subject(id),
    UNIQUE(student_id,subject_id)
 )
