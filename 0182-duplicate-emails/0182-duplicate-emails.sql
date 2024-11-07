# Write your MySQL query statement below
select email
from (
    select email, count(email) as ecount
    from Person
    group by email) as temp
where ecount>1