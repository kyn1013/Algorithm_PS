SELECT c.CustomerName,
	sum(total) TotalAmount,
	count(OrderId) OrderCount
from Customers c
left join 
(
select o.OrderId, o.CustomerID ,p.ProductName, o.Quantity * p.Price total
from Orders o
left join Products p on o.ProductID = p.ProductID
) a
on c.CustomerID = a.CustomerID
group by 1
