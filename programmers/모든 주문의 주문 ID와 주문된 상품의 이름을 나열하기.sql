select o.id, p.name

from orders o

left join products p

on o.product_id = p.id
