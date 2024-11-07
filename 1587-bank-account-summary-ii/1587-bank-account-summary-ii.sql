# Write your MySQL query statement below
select u.name as NAME, sum(t.amount) as BALANCE
from users u
natural join Transactions t
group by t.account
having BALANCE>10000