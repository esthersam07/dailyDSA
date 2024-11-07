# Write your MySQL query statement below
select u.name as NAME, sum(amount) as BALANCE
from users u
right join Transactions t
on u.account=t.account
group by t.account
having BALANCE>10000