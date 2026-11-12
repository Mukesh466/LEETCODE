with temp as (
    select id,recordDate,temperature,lag(recordDate) over (order by recordDate) as prev_date,lag(temperature) over (order by recordDate) as prev_temp
    from Weather
) 
select id
from temp
where datediff(recordDate,prev_date)=1 and temperature > prev_temp;