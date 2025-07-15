select p.id, sum(p.price * o.quantity) total_sales
from orders o
left join products p
on o.product_id = p.id
group by p.id
order by 2 DESC limit 1