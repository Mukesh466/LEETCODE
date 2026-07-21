# Write your MySQL query statement below
select p.product_name,sum(o.unit) as unit
from products p 
join orders o 
on o.product_id=p.product_id
where o.order_date like "2020-02-%"
group by o.product_id
having unit >=100
;