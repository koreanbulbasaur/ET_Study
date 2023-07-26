use mywork;

create table student_delete as
select *
	from highschool_students;
    
alter table student_delete
	add constraint primary key (student_no);
    
describe student_delete;
    
create table student_delete2 as
select *
	from highschool_students;
    
alter table student_delete2
	add constraint primary key (student_no);
    
describe student_delete2;

delete from student_delete
	where age is null;

delete from student_delete;

insert into student_delete
select *
	from highschool_students;
    
select *
	from student_delete
	where student_name like '%Matthews';
    
delete from student_delete
	where student_name like '%Matthews'
    order by student_no desc
    limit 1;
    
commit;