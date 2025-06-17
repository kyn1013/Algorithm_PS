SELECT distinct r.CAR_ID
from CAR_RENTAL_COMPANY_CAR r
inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    on r.CAR_ID = h.CAR_ID
where r.CAR_TYPE = '세단'
        and month(h.START_DATE) = 10
order by 1 desc
