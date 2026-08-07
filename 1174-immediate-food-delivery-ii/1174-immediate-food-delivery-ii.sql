with ref as (select delivery_id,customer_id,
order_date=customer_pref_delivery_date as immediate
from Delivery 
where (customer_id,order_date) in (
    select customer_id,min(order_date)
    from Delivery
    group by customer_id
)
)
select round(avg(immediate *100),2) as immediate_percentage
from ref;