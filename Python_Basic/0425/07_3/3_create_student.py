class Student:
    def __init__(self, name, korean, math, english, science) -> None:
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science


Students = [
    Student("바다거", 98, 78, 87, 67),
    Student("현용범", 82, 23, 65, 79),
    Student("미누", 90, 87, 98, 67),
    Student("이현", 89, 78, 87, 67)
]

print(Students[0].name)
print(Students[0].korean)
print(Students[0].math)
print(Students[0].english)
print(Students[0].science)
