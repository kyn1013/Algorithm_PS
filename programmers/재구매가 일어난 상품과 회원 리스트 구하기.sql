select USER_ID, PRODUCT_ID
from 
(SELECT user_id, product_id, count(*) c
from ONLINE_SALE
group by 1, 2) a
where a.c > 1
order by USER_ID asc, PRODUCT_ID desc
