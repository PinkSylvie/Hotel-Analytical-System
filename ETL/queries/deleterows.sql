delete from chains where chid is NULL or '';

delete from hotel where hid is NULL or '';

delete  from client where clid is null or '';

delete from roomunavailable where ruid is null;

delete from roomunavailable where rid is null;

delete from roomunavailable where startdate is null or startdate='';

delete from roomunavailable where enddate is null or enddate='';
