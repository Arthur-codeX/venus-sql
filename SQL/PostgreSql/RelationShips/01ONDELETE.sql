--- CORRECT WAY


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
--     parent_id INTEGER NOT NULL REFERENCES parent(id) 
--      ON DELETE CASCADE 
-- )

-- ON DELETE CASCADE --> when you delete a parent the student will be deleted
-- ON DELETE RESTRICT --> you cant delete a parent.
-- ON DELETE SET TO <NULL> 


-- INSERT INTO parent(name,email,phone)
-- VALUES
-- ('Josephine','jose@gmail.com',432423423),
-- ('John','john@gmail.com',342532353)


-- INSERT INTO student(name,email,phone,parent_id)
-- VALUES 
-- ('Mery','mercy@gmail.com',3445434,1),
-- ('Nzinza','nzinza@gmail.com',3566545,1),
-- ('Diana','daiana@gmail.com',32232434,2)