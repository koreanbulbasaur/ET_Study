use mywork;

insert into highschool_students
(student_no, student_name, grade, class, gender, age, enter_date) VALUES
(20230001, 'Celine Larsen', 75, 'English', 'female', NULL, '2023-02-03');

INSERT INTO highschool_students
(student_no, student_name, grade, class, gender, age, enter_date) VALUES
(20230002, 'Max Matthews', 85, 'Mathematics', 'male', NULL, '2023-02-03'),
(20230003, 'Phil Lawrence', 55, 'Mathematics', 'male', 23, '2023-02-03'),
(20230004, 'Madison Hopkins', 60, 'English', 'female', 21, '2023-02-03'),
(20230005, 'Bailey Glisson', 60, 'English', 'female', 24, '2023-02-03'),
(20230006, 'Alex John', 55, 'English', 'male', 25, '2023-02-03');

INSERT INTO highschool_students values
(20230007, 'Ernest Woolery', 78, 'Physics', 'male', 22, '2023-02-03');

INSERT INTO highschool_students (student_no, student_name, grade, class, gender, age, enter_date) VALUES
(20230008, 'Rolf Meyer', 85, 'Physics', 'male', 24, '2023-02-03'),
(20230009, 'Owen Turner', 78, 'Arts', 'male', 21, '2023-02-03'),
(20230010, 'Maya Lawrence', 55, 'English', 'female', 25, '2023-02-03'),
(20230011, 'Elissa Stark', 89, 'Arts', 'female', NULL, '2023-02-03'),
(20230012, 'Roselyn Mccarty', 94, 'Arts', 'female', 21, '2023-02-03');

INSERT INTO highschool_students (student_no, student_name) VALUES
(20230013, 'Evelyn Parker');

INSERT INTO highschool_students
(student_no, student_name, gender, age) VALUES
(20230014, 'Rosie Matthews', 'female', 24);

commit;