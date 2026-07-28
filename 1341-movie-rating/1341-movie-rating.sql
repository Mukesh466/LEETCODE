# Write your MySQL query statement below
select name as results from
(select user_id,name,count(*)
from users join MovieRating using(user_id)
group by user_id,name
order by count(*) desc ,name asc
limit 1) users

union all

select title as results from 
(select movie_id,title,avg(rating)
from Movies join MovieRating using(movie_id)
where created_at like "2020-02-%"
group by movie_id,title
order by avg(rating) desc,title asc
limit 1) Movies