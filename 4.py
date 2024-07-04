class Department:
    def __init__(self, name, institute):
        global department_id_counter
        self.id = department_id_counter
        department_id_counter += 1
        self.name = name
        self.institute = institute
        self.teachers = []

    def __str__(self):
        return f"Department(ID: {self.id}, Name: {self.name}, Institute: {self.institute}, Teachers: {[teacher.name for teacher in self.teachers]})"


class Position:
    def __init__(self, name):
        global position_id_counter
        self.id = position_id_counter
        position_id_counter += 1
        self.name = name

    def __str__(self):
        return f"Position(ID: {self.id}, Name: {self.name})"


class Teacher:
    def __init__(self, name, age, department_id, position_id):
        global teacher_id_counter
        self.id = teacher_id_counter
        teacher_id_counter += 1
        self.name = name
        self.age = age
        self.department_id = department_id
        self.position_id = position_id

    def __str__(self):
        return f"Teacher(ID: {self.id}, Name: {self.name}, Age: {self.age}, Department ID: {self.department_id}, Position ID: {self.position_id})"


# Глобальные счетчики ID
department_id_counter = 1
position_id_counter = 1
teacher_id_counter = 1

# Пример данных
departments = [
    Department("Computer Science", "Engineering"),
    Department("Mathematics", "Science"),
    Department("Physics", "Science")
]

positions = [
    Position("Professor"),
    Position("Assistant Professor"),
    Position("Lecturer")
]

teachers = [
    Teacher("Alice Smith", 40, 1, 1),
    Teacher("Bob Johnson", 35, 1, 2),
    Teacher("Charlie Rose", 30, 2, 3),
    Teacher("David Brown", 50, 2, 1),
    Teacher("Eva Green", 45, 3, 2)
]

# Заполнение кафедр преподавателями
for teacher in teachers:
    for department in departments:
        if department.id == teacher.department_id:
            department.teachers.append(teacher)


def department_with_most_teachers(departments):
    max_teachers = 0
    max_department = None
    for department in departments:
        if len(department.teachers) > max_teachers:
            max_teachers = len(department.teachers)
            max_department = department
    return max_department


max_department = department_with_most_teachers(departments)
print(f"Department with most teachers: {max_department.name}")


def departments_by_teacher_count(departments):
    return sorted(departments, key=lambda d: len(d.teachers), reverse=True)


sorted_departments = departments_by_teacher_count(departments)
print("Departments sorted by number of teachers:")
for department in sorted_departments:
    print(f"{department.name}: {len(department.teachers)} teachers")


def youngest_department(departments):
    min_avg_age = float('inf')
    youngest_department = None
    for department in departments:
        if department.teachers:
            avg_age = sum(teacher.age for teacher in department.teachers) / len(department.teachers)
            if avg_age < min_avg_age:
                min_avg_age = avg_age
                youngest_department = department
    return youngest_department


youngest_dept = youngest_department(departments)
print(
    f"The youngest department is {youngest_dept.name} "
    f"with an average age of {sum(teacher.age for teacher in youngest_dept.teachers) / len(youngest_dept.teachers):.2f} "
    f"years.")
