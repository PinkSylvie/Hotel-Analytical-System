CREATE TABLE IF NOT EXISTS chain(
    chid serial primary key,
    cname varchar,
    springmkup float,
    summermkup float,
    fallmkup float,
    wintermkup float);
