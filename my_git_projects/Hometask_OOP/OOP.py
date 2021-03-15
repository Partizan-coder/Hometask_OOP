class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        return

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
        return

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(self, Student) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        average = 0
        count = 0
        for value in self.grades.values():
            average += int(sum(value))
            count += 1
        if count > 0:
            average = round(average / count, 1)
        else:
            average = 'оценок за домашние задания еще нет'
        return average

    def __str__(self):
        average = self.average_grade()

        courses_progress = ''
        for num in range(len(self.courses_in_progress)):
            courses_progress += self.courses_in_progress[num]
            courses_progress += ', '
        courses_progress = courses_progress[0:len(courses_progress) - 2:1]

        courses_finished = ''
        for num in range(len(self.finished_courses)):
            courses_finished += self.finished_courses[num]
            courses_finished += ', '
        courses_finished = courses_finished[0:len(courses_finished) - 2:1]
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {average}\n" \
               f"Курсы в процессе изучения: {courses_progress}\n" \
               f"Завершенные курсы: {courses_finished}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        average_s = self.average_grade()
        average_o = other.average_grade()
        return average_s < average_o

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
        average_s = self.average_grade()
        average_o = other.average_grade()
        return average_s > average_o

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
        average_s = self.average_grade()
        average_o = other.average_grade()
        return average_s == average_o


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        return


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lecturer_grades = {}
        return

    def average_lecturer_grade_course(self, course):
        average = round(sum(self.lecturer_grades[course]) / len(self.lecturer_grades[course]), 1)
        return average

    def average_lecturer_grade(self):
        average = 0
        count = 0
        for value in self.lecturer_grades.values():
            average += int(sum(value))
            count += len(value)
        average = round(average / count, 1)
        return average

    def __str__(self):
        average = self.average_lecturer_grade()
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекцию: {average}"

    def __lt__(self, other, course):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        average_s = self.average_lecturer_grade_course(course)
        average_o = other.average_lecturer_grade_course(course)
        return average_s < average_o

    def __gt__(self, other, course):
        if not isinstance(other, Lecturer):
            print('Ошибка')
        average_s = self.average_lecturer_grade_course(course)
        average_o = other.average_lecturer_grade_course(course)
        return average_s > average_o

    def __eq__(self, other, course):
        if not isinstance(other, Lecturer):
            print('Ошибка')
        average_s = self.average_lecturer_grade_course(course)
        average_o = other.average_lecturer_grade_course(course)
        return average_s == average_o


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


def average_students_grade(students_list, course):
    average = 0
    for student in students_list:
        value = student.grades.get(course)
        average += int(sum(value))
    average = round(average / len(students_list), 1)
    return print(f'Средняя оценки за домашние задания по всем студентам в рамках курса "{course}": {average}')


def average_lecturer_grade_course(lecturer_list, course):
    average = 0
    count = 0
    for lecturer in lecturer_list:
        grades = lecturer.lecturer_grades.get(course)
        count += len(grades)
        average += int(sum(grades))
    average = round(average / count, 1)
    return print(f'Средняя оценки за лекции по всем лекторам в рамках курса "{course}": {average}')


student_1 = Student('Ruoy', 'Eman', 'Male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ["C++"]

student_2 = Student('Jane', 'Fox', 'Female')
student_2.courses_in_progress += ['Java']
student_2.courses_in_progress += ['Python']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('John', 'Smith')
reviewer_2.courses_attached += ['Java']
reviewer_2.courses_attached += ['Python']

lecturer_1 = Lecturer('Cool', 'Lecturer')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Best', 'Buddy')
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Java', 8)

reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Java', 5)

student_1.rate_lecturer(lecturer_1, 'Java', 7)
student_1.rate_lecturer(lecturer_2, 'Python', 9)

student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 10)

students_list_maker = []
students_list_maker += student_1, student_2
lecturer_list_maker = []
lecturer_list_maker += lecturer_1, lecturer_2

print('Переопредленный метод __str__: для класса "Student":')
print(student_1)
print()
print('Сравнение оценок за лекции лектора 1 и лектора 2 по курсу "Java" (л1 = л2):')
print(lecturer_1.__gt__(lecturer_2, 'Java'))
print()
average_lecturer_grade_course(lecturer_list_maker, "Java")
print()
average_students_grade(students_list_maker, "Python")
