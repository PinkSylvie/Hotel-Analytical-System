delete from chain where chid is NULL or '';

delete from hotel where hid is NULL or '';

delete  from client where clid is null or '';

-- room_unavailable

delete from room_unavailable where ruid is null;

delete from room_unavailable where rid is null;

delete from room_unavailable where start_date is null or start_date='';

delete from room_unavailable where end_date is null or end_date='';
