use bs

create table `Users` (
`id` int auto_increment primary key,
`phone` varchar(30) default ''not null unique,
`username` varchar(30) default '' not null,
`password` varchar(30) default ''not null
)

select * from Users
insert into users values (001, '110', 'sb', '110')
drop table Users

create table user_info
(
    id       int unsigned auto_increment	primary key,
    name     varchar(128) default '' not null,
    password varchar(128) default '' not null,
    email    varchar(128) default '' not null
);