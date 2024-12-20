select c.aId as ID
from 
(select a.ID aId,
        a.PARENT_ID aPid,
        b.ID bId,
        b.PARENT_ID bPid
from ECOLI_DATA a
inner join ECOLI_DATA b on a.PARENT_ID = b.ID
)
c inner join ECOLI_DATA d on c.bPid = d.ID
where d.PARENT_ID is null
order by ID asc 
