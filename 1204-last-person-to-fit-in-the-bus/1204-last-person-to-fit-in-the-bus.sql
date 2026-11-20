/* Write your T-SQL query statement below */
SELECT TOP 1
    t.person_name
FROM (
    SELECT 
        person_name,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS totalWeight
    FROM Queue
) t
WHERE t.totalWeight <= 1000
ORDER BY t.turn DESC;
