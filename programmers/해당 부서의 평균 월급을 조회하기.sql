select Department,
	avg(Salary) Avg_Salary
from employees e
group by Department
order by Avg_Salary desc limit 1