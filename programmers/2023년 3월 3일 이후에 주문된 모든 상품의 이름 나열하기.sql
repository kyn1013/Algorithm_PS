select p.name
from orders o
inner join products p
on o.product_id = p.id
where o.order_date > '2023-03-03'