select  e.Name, a.ProjectName, a.Budget
from Employees e
	left join
	(
	select ep.EmployeeID, p.ProjectName, p.Budget 
	from EmployeeProjects ep
	left join Projects p on ep.ProjectID = p.ProjectID
	) a on e.EmployeeID = a.EmployeeID
where a.Budget >= 10000
