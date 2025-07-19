select u.user_id,
		u.email,
		coalesce(p.point, 0) point
from users u
left join point_users p on u.user_id = p.user_id
order by point desc

select u.user_id,
		u.email,
		if(p.point is null, 0, p.point) point
from users u
left join point_users p on u.user_id = p.user_id
order by point desc