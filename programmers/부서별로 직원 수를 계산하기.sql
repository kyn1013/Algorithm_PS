select d.name, count(*)

from employees e

left join departments d

on e.department_id = d.id

group by d.name
