# This file is the program

import class_definition

emp = class_definition.Employee("Marcia", "VP of Sales")
emp.display()


class_definition.greeting()

from class_definition import Employee, greeting

emp = Employee("Marcia", "VP of Sales")
emp.display()

greeting()