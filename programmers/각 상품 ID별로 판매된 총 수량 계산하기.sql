select p.id, sum(o.quantity)
from orders o
left join products p
on o.product_id = p.id
group by p.id