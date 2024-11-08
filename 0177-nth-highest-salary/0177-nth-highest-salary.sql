CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET n = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct(salary)
      from Employee
      order by salary DESC
      limit 1 offset n

  );
END