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

def dumb_decorator(callback):
    @functools.wraps(callback)
    def do_nothing():
        pass
    return do_nothing

@dumb_decorator
def my_function():
    print ("Main func")


my_function()