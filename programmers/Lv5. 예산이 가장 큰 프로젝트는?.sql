select Name, Department, Salary
from 
(
SELECT Department,
	Name,
	Salary, 
	rank() over(partition by Department order by Salary desc) rn
from Employees e
) a
where rn = 1
