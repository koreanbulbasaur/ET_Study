use mywork;

alter table highschool_students
drop primary key;

alter table highschool_students
add primary key (student_no);

alter table highschool_students
drop column class;

alter table highschool_students
add class varchar(50) null;