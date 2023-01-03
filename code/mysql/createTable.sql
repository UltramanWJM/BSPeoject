use bs;

create table `Users` (
`id` int auto_increment primary key,
`phone` varchar(30) default ''not null unique,
`username` varchar(30) default '' not null,
`password` varchar(30) default ''not null
);

create table `Scenes` (
`sceneId` int auto_increment primary key,
`sceneName` varchar(30) default '' not null,
`userId` int not null,
`imgPath` varchar(128) default '' not null,
`deviceNumber` int default 0 not null
);

create table `Devices` (
`deviceId` int auto_increment primary key,
`deviceName` varchar(30) default '' not null,
`sceneId` int not null,
`userId` int not null,
`deviceType` int not null,
`positionX` float default 0,
`positionY` float default 0
);

create table `Lights` (
`deviceId` int auto_increment primary key,
`status` int default 0 not null,
`luminance` int default 0 not null
);

create table `Switches` (
`deviceId` int auto_increment primary key,
`status` int default 0 not null
);

create table `Sensors` (
`deviceId` int auto_increment primary key,
`temperature` float default 0,
`humidity` float default 0
);

create table `Lockes` (
`deviceId` int auto_increment primary key,
`status` int default 0 not null
);

create table `DeviceMes`
(
    `deviceId` int unsigned auto_increment	primary key,
--     `alert` int default 0 not null,
--     `deviceId` int default 0 not null,
    `info` varchar(128) default '' not null,
    `timestamp` datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    `valid` int default 0 not null
) charset = utf8;

select * from Users;
select * from Scenes;
select * from Devices;
select * from Lights;
select * from Switches;
select * from Sensors;
select * from DeviceMes;

drop table Users;
drop table Scenes;
drop table Devices;
drop table Sensors;
drop table DeviceMes;

delete from Scenes;
delete from Devices;

insert into users values (111, '120', '王屌丝', '123');

update DeviceMes set info='3', valid=1 where deviceId=1;