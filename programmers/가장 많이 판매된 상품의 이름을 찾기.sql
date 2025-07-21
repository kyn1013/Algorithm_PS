select p.name, sum(o.quantity)
from orders o
inner join products p
on o.product_id = p.id
group by p.name
order by 2 desc limit 1