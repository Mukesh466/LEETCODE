# Write your MySQL query statement below
delete e
from Person e
join Person i
on e.email = i.email and e.id > i.id