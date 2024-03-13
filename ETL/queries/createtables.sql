CREATE TABLE IF NOT EXISTS chain(
    chid serial primary key,
    cname varchar,
    springmkup float,
    summermkup float,
    fallmkup float,
    wintermkup float);

create table if not exists client(
    clid serial primary key,
    fname varchar,
    lname varchar,
    age integer,
    memberyear integer);

--room decription

create table if not exists hotel(
    hid serial primary key,
    chid integer references chain(chid),
    hname varchar,
    hcity varchar);

--employee

--login

--room

--room unavailable

--reserve