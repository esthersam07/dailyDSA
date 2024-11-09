# Write your MySQL query statement below
select d.name as Department,e.name as Employee, Salary
from Employee e
join Department d
on e.departmentId = d.id
where (e.departmentId,Salary) in (select departmentId, max(salary)
from Employee
group by departmentId)