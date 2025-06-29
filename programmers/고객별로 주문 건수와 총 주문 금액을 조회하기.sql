select c.CustomerName CustomerName,
		count(o.OrderID) OrderCount,
		coalesce (sum(o.TotalAmount), 0) TotalSpent
from Customers c
left join Orders o
	on c.CustomerID = o.CustomerID
group by 1
