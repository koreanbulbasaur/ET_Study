class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("-"*6, '학생 목록', '-' * 6)
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-"*24)

    def __init__(self, name, korean, math, english, science) -> None:
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self) -> str:
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())


students = [
    Student("바다거", 98, 78, 87, 67),
    Student("현용범", 82, 23, 65, 79),
    Student("미누", 90, 87, 98, 67),
    Student("이현", 89, 78, 87, 67)
]

Student.print()
