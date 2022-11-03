use bs

create table `Users` (
`id` int auto_increment primary key,
`phone` varchar(30) default ''not null unique,
`username` varchar(30) default '' not null,
`password` varchar(30) default ''not null
)

create table `Scenes` (
`sceneId` int auto_increment primary key,
`sceneName` varchar(30) default '' not null,
`userId` int not null,
`imgPath` varchar(128) default '' not null,
`deviceNumber` int default 0 not null
)

create table `Devices` (
`deviceId` int auto_increment primary key,
`deviceName` varchar(30) default '' not null,
`sceneId` int not null,
`userId` int not null,
`deviceType` int not null,
`positionX` float default 0,
`positionY` float default 0
)

select * from Users
insert into users values (111, '120', '王屌丝', '123')
drop table Users
drop table Scenes
drop table Devices
