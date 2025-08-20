select user_name,
count(satisfaction_score)
from lol_feedbacks
group by user_name
order by 2 desc limit 3