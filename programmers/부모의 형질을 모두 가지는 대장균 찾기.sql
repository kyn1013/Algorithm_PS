select c.ID, c.GENOTYPE, p.GENOTYPE PARENT_GENOTYPE
from ECOLI_DATA c #자식
    left join ECOLI_DATA p on c.PARENT_ID = p.ID
where p.GENOTYPE = (c.GENOTYPE & p.GENOTYPE) 
order by 1
