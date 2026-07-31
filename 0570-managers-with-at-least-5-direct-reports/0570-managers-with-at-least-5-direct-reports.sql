select e1.name from Employee e1
join Employee e2 on e1.Id = e2.managerId
group by e2.managerId
having count(e2.id) >= 5;