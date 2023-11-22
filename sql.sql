create database hhrujobs

create table vacancies(
    id integer primary key,
    name varchar(50),
    requirements text,
    salary float,
    currency varchar(10),
    employer_id integer,
    employer_name varchar(50),
    link varchar(50)
);

create table employers(
    id integer primary key,
    name varchar(50),
    link varchar(50)
);