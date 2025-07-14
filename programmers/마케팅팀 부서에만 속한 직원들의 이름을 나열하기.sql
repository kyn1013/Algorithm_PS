select e.name
from departments d
inner join employees e
on d.id = e.department_id
where d.name = '마케팅팀'