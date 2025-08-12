# #class = blueprint for creating objects
# class cat: 
#   # __init__ sets up the object's initial attributes
#   def __init__(self,name,color):
#     self.name = name #attribute = variable inside object
#     self.color = color #attribute = variable inside object
#   def meow(self): #method function inside object
#     print(f"{self.name} say meow!")

# # object = nstance created from a class
# my_cat = cat("subi","black")
# my_cat.meow() #access the method
# print(my_cat.name) #access the attribute

# class Car:
#   def __init__(self,color,mileage):
#     self.color = color
#     self.mileage = mileage

#   def drive(self,miles):
#     self.mileage = self.mileage + miles

# blue_car = Car("blue", 0)    
# blue_car.drive(200)
# print(blue_car.mileage)

# Encapsulation – Bundle data and functions together in a class.
# Abstraction – Hide unnecessary details from the user.
# Inheritance – A class can inherit attributes and methods from another.
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# class Square(Rectangle):
#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)


# square = Square(4)
# print(square.area())  # 16

# square.width = 5  # Modifies .width but not .length
# print(square.area())  # 20
# # Polymorphism – Different classes can have methods with the same name but different behaviors.



# # Exercise 1: Create a class Greeter with a method greet(name) that prints a greeting for the provided name.
# class Greeter:
#   def greet(self,name):
#     print(f"hello, {name}")

# user = Greeter()    
# user.greet("viola")

# # Exercise 2: Develop a class Calculator with methods to add and subtract two numbers.
# class calculator:
#   def add(self, num1, num2):
#     return(num1 + num2)
#   def subtract(self, num1, num2):
#     return(num1 - num2)
#   def multiply(self, num1, num2):
#     return(num1 * num2)
#   def divide(self, num1, num2):
#     if num2 != 0:
#       return(num1 / num2)
#     else:
#       print(f"Zero Division Error, num2 cannot be zero")
#   def modulus(self, num1, num2):
#     return(num1 % num2)
  
# result = calculator()  
# print(result.add(5,8))
# print(result.subtract(0,4))
# print(result.multiply(3,7))
# print(result.divide(7,6))
# print(result.modulus(9,9))

# Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.
# Python does not support multiple constructors directly.
# Instead, you use a single constructor with default arguments to achieve flexible object creatione.
# class Employee:
#     def __init__(self, name, id=None, department=None):
#         self.name = name
#         self.id = id
#         self.department = department

#     def display_details(self):
#         print(f"Name: {self.name}")
#         if self.id:
#             print(f"ID: {self.id}")
#         if self.department:
#             print(f"Department: {self.department}") 

# emp1 = Employee("John",25)
# emp1.display_details()

# emp2 = Employee("Doe", 101)
# emp2.display_details()

# emp3 = Employee("Jane", 102, "HR")
# emp3.display_details()             

# # Exercise 6: Design a Rectangle class with default attributes for length and width set to 1. 
# # Include methods to set these attributes and calculate the area.
# class Rectangle:
#   def __init__(self, length = 1, width = 1):
#     self.length = length
#     self.width = width

#   def set_dimensions(self, length, width):
#     self.length = length
#     self.width = width 

#   def Area(self):
#     return(self.length*self.width)
  
# my_rectangle = Rectangle()
# print(my_rectangle.Area()) 
# my_rectangle.set_dimensions(7,9)
# print(my_rectangle.Area())  

# # Exercise 7: Person Class with __str__ Method: Create a Person class with first and last name attributes 
# # and override the __str__ method to return the full name.
# class Person:
#   def __init__(self,fname, lname):
#     self.fname = fname
#     self.lname = lname

#   def __str__(self):
#     return f"{self.fname} {self.lname}"

# my_name = Person("John", "Doe")
# print(my_name) 

# Exercise 8: Student Grade Calculator: Implement a Student class with attributes for name and a list of marks. 
# Include a method to calculate the average and determine the grade.
class grade_calculator:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks

  def average(self):
    return (sum(self.marks) / len(self.marks))
  
  def grade(self):
    average = self.average()
    if average >= 90:
      return 'A'
    elif average >= 80:
      return 'B'
    elif average >= 70:
      return 'C'
    elif average >= 60:
      return 'D'
    elif average >= 50:
      return 'C'
    else:
      return 'F'

student = grade_calculator("mark", [70,67,83])
average_marks = student.average()
print(average_marks)
mean_grade = student.grade()
print(mean_grade)

    