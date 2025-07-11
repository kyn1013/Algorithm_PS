select Country,
	CustomerName Top_Customer,
	total_amount Top_Spent
from 
(
select c.Country 
	, c.CustomerName
	, sum(o.TotalAmount) total_amount
	, rank() over (partition by c.Country order by sum(o.TotalAmount) desc) ranking
from Customers_n c
left join Orders_n o
	on c.CustomerID = o.CustomerID
group by 1, 2
) a
where ranking = 1