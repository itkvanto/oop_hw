class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sr_grade=0

    def rate_lecture(self,lecturer,course,grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course not in lecturer.courses_grades:
                lecturer.courses_grades[course]=[grade]
            else:
                lecturer.courses_grades[course].append(grade)

    def __str__(self):
        summma=0
        kol=0
        for el in self.grades:
            summma+=sum(self.grades[el])
            kol+=len(self.grades[el])
        self.sr_grade=summma/kol
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.sr_grade,1)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self,other):
        if not isinstance(other, Student):
            print('Нет такого студента!')
            return
        return self.sr_grade < other.sr_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_grades = {}
        self.sr_grade = 0

    def __str__(self):
        summma=0
        kol=0
        for el in self.courses_grades:
            summma+=sum(self.courses_grades[el])
            kol+=len(self.courses_grades[el])
        self.sr_grade=summma/kol
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.sr_grade,1)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора!')
            return
        return self.sr_grade < other.sr_grade

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def sr_grade_students(students,course):
    summa=0
    kol=0
    for el in students:
        if course in el.courses_in_progress:
            summa+=sum(el.grades[course])
            kol+=len(el.grades[course])
    return round(summa/kol,1)

def sr_grade_lecturers(lecturers,course):
    summa=0
    kol=0
    for el in lecturers:
        if course in el.courses_attached:
            summa+=sum(el.courses_grades[course])
            kol+=len(el.courses_grades[course])
    return round(summa/kol,1)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student1 = Student('Ivan', 'Ivanov', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']
best_student1.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Some', 'Lecturer')
cool_lecturer.courses_attached += ['Python']

cool_lecturer1 = Lecturer('Other', 'Lecturer')
cool_lecturer1.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Reviewer')
cool_reviewer.courses_attached += ['Python']

cool_reviewer1 = Reviewer('Other', 'Reviewer')
cool_reviewer1.courses_attached += ['Python']

print(cool_reviewer)
print(cool_reviewer1)

cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)

cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student1, 'Python', 8)
cool_reviewer1.rate_hw(best_student1, 'Python', 9)

print(best_student)
print(best_student1)
print(best_student < best_student1)

best_student.rate_lecture(cool_lecturer,'Python',10)
best_student.rate_lecture(cool_lecturer,'Python',5)
best_student.rate_lecture(cool_lecturer,'Python',10)

best_student1.rate_lecture(cool_lecturer1,'Python',3)
best_student1.rate_lecture(cool_lecturer1,'Python',5)
best_student1.rate_lecture(cool_lecturer1,'Python',4)

print(cool_lecturer)
print(cool_lecturer1)
print(cool_lecturer < cool_lecturer1)

print(sr_grade_students([best_student,best_student1],'Python'))
print(sr_grade_lecturers([cool_lecturer,cool_lecturer1],'Python'))