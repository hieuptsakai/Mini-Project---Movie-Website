CREATE DATABASE MovieWeb
USE [MovieWeb]

CREATE TABLE M_Type
(
	ID INT identity(1,1) primary key,
	UserTypeID INt,
	M_Type NVARCHAR(10) NOT NULL
)

CREATE TABLE M_User
(
	ID INT identity(1,1) primary key,
	UserTypeID NVARCHAR(10) NOT NULL,
	Username Nvarchar(10) not null,
	U_Password Nvarchar(10) not null,
	U_StatusID Nvarchar(10) not null
)

CREATE TABLE Manga
(
	ID INT identity(1,1) primary key,
	M_Name Nvarchar(30) not null,
	genre nvarchar(10) not null,
	author nvarchar(10) not null,
	summary text,
	thumbnail varbinary (max)
)

create table chapter
(
	ID int identity(1,1) primary key,
	Chapter_num int,
	MangaID INT,
	Page_num int,
	Page_picture varbinary(max)
)

create table favorite
(
	ID int identity(1,1) primary key,
	UserID int,
	MangaID int
)

