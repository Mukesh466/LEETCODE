# Write your MySQL query statement below
select em.unique_id,e.name
from Employees e
left join EmployeeUNI em
on em.id=e.id