select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where (0 < SKILL_CODE & (select CODE from SKILLCODES where name = 'Python')) 
        or (0 < SKILL_CODE & (select CODE from SKILLCODES where name = 'C#'))
order by ID;
