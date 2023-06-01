class Student:
    count = 0

    def __init__(self, name, korean, math, english, science) -> None:
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성됨".format(Student.count))


students = [
    Student("바다거", 90, 1, 1, 33),
    Student("현용범", 90, 2, 29, 33),
    Student("미누", 90, 1, 1, 33),
    Student("이현", 60, 7, 8, 63)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))
