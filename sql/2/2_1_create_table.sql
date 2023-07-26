create database mywork;

create database if not exists mywork;

create database rubbish;

drop database rubbish;

use mywork;
create table test_highschool_students(
	student_no		varchar(20),
    student_name 	varchar(100),
    grade			tinyint,
    class			varchar(50),
    gender 			varchar(20),
    age				smallint,
    enter_date		date
);

describe test_highschool_students;

drop table test_highschool_students;