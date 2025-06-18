select a.CATEGORY,
        a.PRICE MAX_PRICE,
        a.PRODUCT_NAME
from
(
SELECT CATEGORY,
        PRODUCT_NAME,
        rank() over(partition by CATEGORY order by PRICE desc) as ranking,
        PRICE
from FOOD_PRODUCT
) a
where a.ranking = 1
    and a.CATEGORY in ('과자', '국', '김치', '식용유')
order by 2 desc
