use mywork;

select *
	from student_delete
    where student_name like '%Matthews';
    
delete from student_delete
	where student_name like '%Matthews'
    order by student_no desc
    limit 1;
    
delete a, b
	from student_delete a, student_delete2 b
    where a.student_no = b.student_no;
    
delete from student_delete
	where student_name like '%Matthews'
    order by student_no desc
    limit 1;
    
delete from student_delete2;

insert into student_delete
select *
	from highschool_students
    where student_no <> 20230018;
    
insert into student_delete2
select *
	from highschool_students;
    
delete from b
	using student_delete a, student_delete2 b
    where a.student_no = b.student_no;