create database MVW
use [MVW]

create table [dbo].[Type]
(
	[ID] [int] primary key,
	[Type] [nvarchar](10) not null,
) on [primary]

create table [dbo].[User]
(
	[ID] [int] Identity(1,1) primary key,
	[UserTypeID] [int],
	[Username] [nvarchar](20) Not null,
	[Password] [nvarchar](30) not null,
	[Status] [bit] not null default 1
) on [primary]

create table [dbo].[manga]
(
	[ID] [int] Identity(1,1) primary key,
	[Name] [nvarchar](10) not null,
	[Genre] [nvarchar](10) not null,
	[Author] [nvarchar](20) not null,
	[Summary] [text],
	[Thumbnail] [varbinary] (max)
) on [primary]

create table [dbo].[chapter]
(
	[ID] [int] Identity(1,1) primary key,
	[Chapter_num] [int],
	[MangaID] [int],
	[Page_num] [int],
	[Page_picture] [varbinary](max)
) on [primary]

create table [dbo].[favorite]
(
	[ID] [int] Identity(1,1) primary key,
	[UserID] [int],
	[MangaID] [int]
) on [primary]