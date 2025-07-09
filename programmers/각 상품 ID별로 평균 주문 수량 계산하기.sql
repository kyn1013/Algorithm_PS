select p.id, avg(o.quantity)
from orders o
inner join products p
on o.product_id = p.id
group by p.id