select d.name
from departments d
left join employees e
on d.id = e.department_id
where e.id is null