
-- 1. ALL student where mark is 
--  less than 40. Sort this by fee ascending

-- SELECT *
-- FROM student
-- WHERE mark < 40
-- ORDER BY fee ASC;

-- 2. ALL students where 
-- fee is less than 200k,
--  sort by grade ascending

-- SELECT * FROM student
-- WHERE
-- fee<200000
-- ORDER BY mark ASC;

-- 3. where bio is null and mark is less than 40 order by name

-- SELECT *
-- FROM student
-- WHERE (bio IS NULL AND mark < 40)
-- ORDER BY name ASC;

-- 4. where gender is distinct order by email

SELECT DISTINCT mark
FROM student



-- SELECT s.*
-- FROM student AS s
-- INNER JOIN(
--     SELECT DISTINCT mark
--     FROM student
-- ) AS m
-- ON s.mark=m.mark
-- ORDER BY s.mark ASC

-- 5. name contains letter a// text search

-- SELECT * FROM student
-- WHERE
-- name LIKE '%an%';

-- 6. where is_married is true and mark is greater than 40 ORDER by fee

-- SELECT *
-- FROM student
-- WHERE is_married = true AND mark > 40
-- ORDER BY fee;

-- 7. Range where mark ranges from 80 to 90 ORDER by gender
-- SELECT *
-- FROM student
-- WHERE mark BETWEEN 80 AND 90
-- ORDER BY gender;