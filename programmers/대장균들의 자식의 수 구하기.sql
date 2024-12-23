select e.ID, coalesce(count(d.ID), 0) CHILD_COUNT
from ECOLI_DATA e
left join ECOLI_DATA d on e.ID = d.PARENT_ID #부모컬럼에 자식의 정보를 붙여서 테이블 생성
group by e.ID
order by 1
