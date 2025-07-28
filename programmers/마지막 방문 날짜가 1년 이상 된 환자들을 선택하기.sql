select *
from patients
where last_visit_date <= date_sub(curdate(), interval 1 year)