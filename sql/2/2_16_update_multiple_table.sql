use mywork;

update student_update2 a, student_update1 b
	set a.age = b.age + 1000
    where a.student_no = b.student_no;
    
update student_update2 a, student_update1 b
	set b.age = ifnull(b.age, 0),
		a.age = b.age + 2000
	where a.student_no = b.student_no;
    
commit;

insert into student_update2
select *
	from student_update1 a
    where student_no between 20230003 and 2023005
    on duplicate key update student_name = a.student_name, age = a.age;
    
commit;