
-- student
-- name,email,phone,

-- parent-> name,email,phone

-- DROP TABLE student;

-- DB Relation(manages,exists,delete it accendentaly) 
-- And non Relational ITS DIFICULT TO MANAGE RELATIONSHIPS.

-- DONT DO THIS.

-- CREATE TABLE parent(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL UNIQUE ,
--     phone VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE student(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL UNIQUE ,
--     phone BIGINT NOT NULL UNIQUE,
--     parent_id INTEGER NOT NULL
-- )

-- INSERT INTO parent(name,email,phone)
-- VALUES('Josephine','jose@gmail.com',32423323)


-- INSERT INTO student(name,email,phone,parent_id)
-- VALUES('Sam ','sam@sam.com',32423323,1)

-- SELECT * FROM student
-- WHERE email='sam@sam.com'

-- SELECT * FROM parent
-- WHERE id =1

-- INSERT INTO student(name,email,phone,parent_id)
-- VALUES('Bongai ','b@gmail.com',564645,2)


--- > DO THIS BUT NOT THE BEST

-- DROP TABLE parent,student;

-- CREATE TABLE parent(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL UNIQUE ,
--     phone VARCHAR(255) NOT NULL UNIQUE
-- );

-- CREATE TABLE student(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL UNIQUE ,
--     phone BIGINT NOT NULL UNIQUE,
--     parent_email VARCHAR(255) REFERENCES parent(email)
-- )

-- INSERT INTO parent(name,email,phone)
-- VALUES('Josephine','jose@gmail.com',432423423)

-- SELECT * FROM parent

-- INSERT INTO student(name,email,phone,parent_email)
-- VALUES('Sam','sam@sam.com',423423,'jose@gmail.com')


-- UPDATE parent SET email='jose2@gmail.com'
-- WHERE id=1