import self as self


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if grade <= 10:
                if course in lecturer.grades_from_student:
                    lecturer.grades_from_student[course] += [grade]
                else:
                    lecturer.grades_from_student[course] = [grade]
            else:
                return 'Error'

    def average_grade(self):
        average_grade = []
        for values in self.grades.values():
            i = 0
            while i < len(values):
                average_grade.append(values[i])
                i += 1
        aver_grade = round((sum(average_grade) / len(average_grade)), 1)
        return aver_grade

    def __str__(self):
        res = f'Студент \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравнивать можно только студентов :(")
            return
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print("Сравнивать можно только студентов :(")
            return
        return self.average_grade() <= other.average_grade()

def student_average_grade_course(students, course):
    summ = []
    for student in students:
        for courses, grade in student.grades.items():
            if courses == course:
                i = 0
                while i < len(grade):
                    summ.append(grade[i])
                    i += 1
    av_grade_course = sum(summ) / len(summ)
    return av_grade_course

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_student = {}

    def average_rating(self):
        average_rate = []
        for values in self.grades_from_student.values():
            i = 0
            while i < len(values):
                average_rate.append(values[i])
                i += 1
        aver_rate = round((sum(average_rate) / len(average_rate)), 1)
        return aver_rate

    def __str__(self):
        res = f'Преподаватель \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнивать можно только лекторов :(")
            return
        return self.average_rating() < other.average_rating()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнивать можно только лекторов :(")
            return
        return self.average_rating() <= other.average_rating()

def lecturer_average_grade(lecturers):
    summ = []
    for lecture in lecturers:
        for grade in lecture.grades_from_student.values():
            i = 0
            while i < len(grade):
                summ.append(grade[i])
                i += 1
    av_grade = sum(summ) / len(summ)
    return av_grade

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades and grade <= 10:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        res = f'Проверяющий \nИмя: {self.name} \nФамилия: {self.surname}\n'
        return res



# Создаем студентов
# Студент 1
best_student = Student('Bosha', 'Garinov', 'male')
best_student.courses_in_progress += ['Python', 'JS', 'HTML']
best_student.finished_courses += ['Введение в программирование', 'Введение в Git']
# Студент 2
iot_student = Student('Alisa', 'Yandexova', 'female')
iot_student.courses_in_progress += ['Python', 'JS', 'IoT']
iot_student.finished_courses += ['Введение в программирование', 'Введение в Git', 'Введение в искусственый интелект', 'Машинное обучение']


# Создаем проверяющих
# Проверяющий 1
cool_reviewer = Reviewer('Donald', 'Drump')
cool_reviewer.courses_attached += ['Python', 'HTML', 'JS']
# Проверяющий 2
nice_reviewer = Reviewer('Jurui', 'Konstantinovich')
nice_reviewer.courses_attached += ['Python', 'HTML', 'JS']

# Cоздаем лекторов
# Лектор 1
nice_lecturer = Lecturer('Stephen', 'Nowaking')
nice_lecturer.courses_attached += ['Python', 'HTML', 'JS']
# Лектор 2
best_lecturer = Lecturer('Ole', 'G')
best_lecturer.courses_attached += ['Python', 'HTML', 'JS']

# Ставим оценки студентам
cool_reviewer.rate_hw(best_student, 'Python', 7)
nice_reviewer.rate_hw(best_student, 'HTML', 7)
cool_reviewer.rate_hw(iot_student, 'Python', 10)
nice_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(iot_student, 'JS', 10)
nice_reviewer.rate_hw(best_student, 'HTML', 10)

# Cтавим оценки лекторам
best_student.lecturer_grade(nice_lecturer, 'Python', 10)
iot_student.lecturer_grade(best_lecturer, 'JS', 10)
best_student.lecturer_grade(nice_lecturer, 'HTML', 10)
best_student.lecturer_grade(nice_lecturer, 'Python', 8)
iot_student.lecturer_grade(best_lecturer, 'Python', 10)

students_list = [best_student, iot_student]
lectors_list = [nice_lecturer, best_lecturer]
# print(student_average_grade_course(students_list, 'Python'))
print(lecturer_average_grade(lectors_list))

# # Сравним кого-нибудь
# print(nice_lecturer < best_lecturer)
# print(iot_student >= best_student)

# # Вывод(общий)
# print(cool_reviewer)
# print(nice_reviewer)
# print(nice_lecturer)
# print(best_lecturer)
# print(best_student)
# print(iot_student)