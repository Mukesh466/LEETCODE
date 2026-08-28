# Write your MySQL query statement below
select s.machine_id,round(avg(t.timestamp-s.timestamp),3) as processing_time
from Activity s
join Activity t
on s.machine_id=t.machine_id and 
s.process_id=t.process_id and 
s.activity_type="start" and 
t.activity_type="end"
group by s.machine_id;