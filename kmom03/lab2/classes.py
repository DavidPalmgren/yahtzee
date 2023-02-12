"""
Classes module
"""
class Person():
    """Person the class"""

    def __init__(self, name, ssn, address = ""):
        self.name = name
        self._ssn = ssn
        self.address = address

    def get_ssn(self):
        """returns private instance attribute ssn"""
        return self._ssn

    def set_address(self, address):
        """
        sets address
        """
        self.address = address

    def __str__(self):
        if self.address:
            return f"Name: {self.name} SSN: {self.get_ssn()} {str(self.address)}"
        return f"Name: {self.name} SSN: {self.get_ssn()}"

class Address():
    """Address class"""
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return f"Address: {self.city} {self.state} {self.country}"

class Teacher(Person):
    """
    Teacher class
    """
    def __init__(self, name, ssn, address=""):
        super().__init__(name, ssn, address)
        self.courses = []

    def add_course(self, course):
        """
        appends course to courses
        """
        self.courses.append(course)

    def __str__(self):
        courses = ", ".join(self.courses)
        return f"{super().__str__()} Courses: {courses}"

class Student(Person):
    """
    Student class inherit from Person
    """
    def __init__(self, name, ssn, address=""):
        super().__init__(name, ssn, address)
        self.courses_grades = []

    def add_course_grade(self, course, grade):
        """appendar tuple till courses_grades"""
        self.courses_grades.append((course, grade))

    def average_grade(self):
        """
        tar ut värdet grade från tuple hoppar över - returnerar totalet / på antal kurser utan -
        """
        grade_total = 0
        counter = 0
        for i in self.courses_grades:
            _ ,grade = i
            counter += 1
            if grade != "-":
                grade_total += grade
            else:
                counter -= 1
        return grade_total/counter
