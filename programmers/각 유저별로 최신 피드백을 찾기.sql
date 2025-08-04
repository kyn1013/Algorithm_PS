select user_name, max(feedback_date)
from lol_feedbacks
group by user_name