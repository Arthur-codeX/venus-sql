-- SELECT * FROM student;
--
-- 
-- SELECT * from parent
-- WHERE
-- (id=5)
-- OR 
-- (id=2)
-- OR 
-- (id=1);

-- SYNTAX
-- select <* OR table1.<column>> table_name
-- INNER JOIN <table_name> ON table1.<column>=table2.columnt
--
-- 

-- SELECT * FROM student

-- SELECT *
-- FROM student
-- INNER JOIN parent
-- ON student.parent_id=parent.id

-- SELECT s.id,
-- s.name,
-- p.name AS parent_name,
-- p.id AS parent_id
-- FROM student AS s
-- INNER JOIN
-- parent AS p
-- ON s.parent_id=p.id