use mywork;
create table student_update1 as
select *
	from highschool_students;
    
alter table student_update1
	add constraint primary key (student_no);
    
create table student_update2 as
select *
	from highschool_students
    where student_no <= 20230004;
    
alter table student_update2
	add constraint primary key (student_no);
    
update student_update1
	set student_name = concat(student_name, '2'),
		age = age + 100;
        
update student_update1
	set student_no = student_no + 1
	where student_no >= 20230014;
    
update student_update1
	set student_no = student_no + 1
    where student_no >= 20230014
    order by student_no desc;