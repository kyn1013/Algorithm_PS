select e.name name, d.name departments_name
from employees e
left join departments d
on e.department_id = d.id