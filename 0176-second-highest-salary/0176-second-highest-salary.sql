# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from (
    select salary,dense_rank() over (order by salary desc) as SecondHighestSalary
    from Employee
)s
where SecondHighestsalary=2;