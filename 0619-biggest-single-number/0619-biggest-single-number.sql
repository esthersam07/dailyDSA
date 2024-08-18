# Write your MySQL query statement below
with temp as(
select num, count(num) as freq
from MyNumbers
group by num
)
select max(num) as num
from temp
where freq=1