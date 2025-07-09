select a.id, a.name
from
(
select p.id, p.name, sum(o.quantity) as sum_quantity
from products p
left join orders o
on o.product_id = p.id
group by 1, 2
) a
where 0 = a.sum_quantity