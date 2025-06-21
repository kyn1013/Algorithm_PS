select Category, ProductName Top_Product, TotalSold 
from 
(
select p.Category,
	p.ProductName,
	sum(o.Quantity) TotalSold,
	rank() over(partition by p.Category order by sum(o.Quantity) desc) rn
from Orders o
left join Products p on o.ProductID = p.ProductID
group by 1, 2
) a
where a.rn = 1