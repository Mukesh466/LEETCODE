# Write your MySQL query statement below
select e.name as Employee
from Employee e
join Employee i
on e.managerId = i.id
where e.salary > i.salary;