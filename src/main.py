class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def class_method(cls):
        print ("This is a class method")

        print ("I'm a {}".format(cls))

    @staticmethod
    def static_method():
        print ("This is a static method")


anna = Student('Anna', 'MIT')
ozrlz = Student('ozrlz', 'UDG')

ozrlz.class_method()
Student.static_method()