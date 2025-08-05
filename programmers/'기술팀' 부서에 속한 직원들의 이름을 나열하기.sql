select e.name

from employees e

left join departments d

on e.department_id = d.id

where d.name = '기술팀'
