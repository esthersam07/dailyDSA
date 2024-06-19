# Write your MySQL query statement below
# concept understanding link - https://www.youtube.com/watch?v=j7z9FIYfn9s
SELECT s.user_id, CASE WHEN c.time_stamp IS NULL
THEN 0.00
ELSE ROUND(SUM(c.action='confirmed')/COUNT(*),2)
END AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id