USE mywork;

-- 기본 키(Primary Key)
CREATE TABLE test_highschool_students
(
 student_no VARCHAR(20) NOT NULL PRIMARY KEY,
 student_name VARCHAR(100) NOT NULL,
 grade TINYINT NULL,
 class VARCHAR(50) NULL,
 gender VARCHAR(20) NULL,
 age SMALLINT NULL,
 enter_date DATE
);

describe test_highschool_students;

drop table test_highschool_students;

-- student_no : NULL or NOT NULL ?
CREATE TABLE test_highschool_students
(
 student_no VARCHAR(20) PRIMARY KEY,
 student_name VARCHAR(100) NOT NULL,
 grade TINYINT NULL,
 class VARCHAR(50) NULL,
 gender VARCHAR(20) NULL,
 age SMALLINT NULL,
 enter_date DATE
);

describe test_highschool_students;

drop table test_highschool_students;

-- another make primary key
CREATE TABLE test_highschool_students
(
 student_no VARCHAR(20) NOT NULL,
 student_name VARCHAR(100) NOT NULL,
 grade TINYINT NULL,
 class VARCHAR(50) NULL,
 gender VARCHAR(20) NULL,
 age SMALLINT NULL,
 enter_date DATE,
 PRIMARY KEY (student_no)
);

describe test_highschool_students;

drop table test_highschool_students;