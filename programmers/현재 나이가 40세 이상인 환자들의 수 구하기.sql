select count(*)
from patients
where 40 <= timestampdiff(year, birth_date, curdate())
SELECT COUNT(*) FROM patients
WHERE birth_date <= DATE_SUB(CURDATE(), INTERVAL 40 YEAR);