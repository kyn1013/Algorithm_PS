select a.ID, 
        case WHEN a.percent <= 0.25 THEN 'CRITICAL'
        WHEN a.percent <= 0.5 THEN 'HIGH'
        WHEN a.percent <= 0.75 THEN 'MEDIUM'
        else 'LOW' end COLONY_NAME
from 
(select ID,
        percent_rank() over(order by SIZE_OF_COLONY desc) percent
from ECOLI_DATA)
a
order by 1
