select count(*) FISH_COUNT
from 
(select f.FISH_TYPE, n.FISH_NAME
from FISH_INFO f
left join FISH_NAME_INFO n on n.FISH_TYPE = f.FISH_TYPE) a
where FISH_NAME = 'BASS' or FISH_NAME = 'SNAPPER'' by