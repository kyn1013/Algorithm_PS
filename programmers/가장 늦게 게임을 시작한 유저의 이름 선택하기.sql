SELECT name

FROM lol_users

where join_date =

(select max(join_date)

from lol_users

)
