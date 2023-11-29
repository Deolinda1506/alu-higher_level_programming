-- listing all the recrdsin the table leaving out those without names
SELECT score,name
FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC

