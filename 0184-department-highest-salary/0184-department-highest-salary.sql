# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary
from Employee e
join Department d
on e.departmentID=d.id
where e.salary = (
    select max(salary)
    from Employee e
    where e.departmentID=d.id
);