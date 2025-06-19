SELECT p.PRODUCT_ID,
        p.PRODUCT_NAME,
        sum(p.PRICE * o.AMOUNT) TOTAL_SALES
from FOOD_PRODUCT p 
    inner join FOOD_ORDER o on p.PRODUCT_ID = o.PRODUCT_ID
where o.PRODUCE_DATE >= '2022-05-01' and o.PRODUCE_DATE < '2022-06-01'
group by 1, 2
order by 3 desc, 1
