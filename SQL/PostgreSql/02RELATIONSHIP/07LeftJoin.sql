

SELECT * 
FROM student  as s
LEFT JOIN parent as p
ON s.parent_id=p.id
INNER JOIN address as a
ON s.address_id=a.id
ORDER BY
s.name ASC