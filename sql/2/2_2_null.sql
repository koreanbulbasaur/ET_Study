USE mywork;
CREATE TABLE test_highschool_students
(
 student_no VARCHAR(20) NOT NULL,
 student_name VARCHAR(100) NOT NULL,
 grade TINYINT NULL,
 class VARCHAR(50) NULL,
 gender VARCHAR(20) NULL,
 age SMALLINT NULL,
 enter_date DATE
);

describe test_highschool_students;

drop table test_highschool_students;