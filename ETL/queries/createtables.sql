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

create table if not exists roomdescription(
    rdid serial primary key,
    rname varchar,
    rtype varchar,
    capacity integer,
    ishandicap boolean);

create table if not exists hotel(
    hid serial primary key,
    chid integer references chain(chid),
    hname varchar,
    hcity varchar);

create table if not exists employee(
    eid serial primary key,
    hid integer references hotel(hid),
    fname varchar,
    lname varchar,
    age integer,
    position varchar,
    salary float);

create table if not exists login(
    lid serial primary key,
    eid integer references employee(eid),
    username varchar,
    password varchar);

create table if not exists room(
        rid serial primary key,
        hid integer references hotel(hid),
        rdid integer references roomdescription(rdid),
        rprice float);

    
create table if not exists roomunavailable(
    ruid serial primary key,
    rid integer references room(rid),
    startdate date,
    enddate date);

--reserve
