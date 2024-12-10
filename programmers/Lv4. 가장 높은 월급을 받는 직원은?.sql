select e.Name,
		e.Department,
		e.Salary,
		b.Top_Earner,
		b.Top_Salary
from employees e
	inner join 
	(
		select Department,
			Name Top_Earner,
			Salary Top_Salary
		from 
		(
		select Department,
			Name,
			Salary,
		rank() over(partition by Department order by Salary desc) rn
		from employees
		)a
		where rn = 1
	)b on e.Department = b.Department
