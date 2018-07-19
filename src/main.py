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


import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_fun():
        print ("In the decorator!")
        func()
        print("After the decorator")
    return function_that_runs_fun

def decorator_with_arguments(number):
    def inner_decorator(func):
        @functools.wraps(func)
        def func_returning_func():
            print("In the decorator")
            func()
            print("After the decorator")
        return func_returning_func
    return inner_decorator
@decorator_with_arguments(56)
def my_function():
    print ("Main func")


my_function()