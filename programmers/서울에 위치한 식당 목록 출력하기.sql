select r.REST_ID, r.REST_NAME, r.FOOD_TYPE, r.FAVORITES, r.ADDRESS, a.food_avg as SCORE
from REST_INFO r
inner join 
(
select i.REST_ID, round(avg(r.REVIEW_SCORE), 2) food_avg
from REST_INFO i
left join REST_REVIEW r on i.REST_ID = r.REST_ID
group by i.REST_ID
) a on r.REST_ID = a.REST_ID
where substring(r.ADDRESS, 1, 2) = '서울' 
        and a.food_avg is not null
order by SCORE desc, r.FAVORITES desc
