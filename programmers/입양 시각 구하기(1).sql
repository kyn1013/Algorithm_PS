SELECT hour(DATETIME) as HOUR, count(*) COUNT
from ANIMAL_OUTS
where  9 <= hour(DATETIME) and hour(DATETIME) < 20
group by 1
order by HOUR
