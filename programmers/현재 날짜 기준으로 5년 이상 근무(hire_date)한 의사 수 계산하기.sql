select count(*)
from doctors
where hire_date <= date_sub(curdate(), interval 5 year)