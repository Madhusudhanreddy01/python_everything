# # define a superclass
# class super_class:
#     # attributes and method definition

# # inheritance
# class sub_class(super_class):
#     # attributes and method of super_class
#     # attributes and method of sub_class

# # -------------------------------------------------------

class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

# call subclass method 
labrador.display()


# print("------------------"or"-----------------------------")

#How to inherit one class into another:

# class Rectangle:
#     def rec_area(self, height, width):
#         area = height * width
#         print("Area of Rectangle:", area)

# class Square(Rectangle):
#     def squ_area(self, side):
#         area = side * side
#         print("Area of Square:", area)

# obj = Square()
# obj.rec_area(10,20)
# obj.squ_area(12)

# print("-----------------------------------------------")

# #single Inheritance: Only two classes are used in which one is inherited by another

# class Rectangle:
#     def rec_area(self, height, width):
#         area = height * width
#         print("Area of Rectangle:", area)

# class Square(Rectangle):
#     def squ_area(self, side):
#         area = side * side
#         print("Area of Square:", area)

# obj = Square()
# obj.rec_area(10,20)
# obj.squ_area(12)

# print("-----------------------------------------------")

# #Multiple Inheritance: more than two classes are inherited by a single class simultaneously called multiple inheritance.

# class Rectangle:
#     def rec_area(self, height, width):
#         area = height * width
#         print("Area of Rectangle:", area)

# class Square:
#     def squ_area(self, side):
#         area = side * side
#         print("Area of Square:", area)

# class Traingle(Rectangle, Square):
#     def tri_area(self, length, breadth):
#         area = 0.5 * length * breadth
#         print("Area of Triangle:", area)

# obj = Traingle()
# obj.rec_area(10,20)
# obj.squ_area(12)
# obj.tri_area(12, 25)

# print("-----------------------------------------------")

# # Multi-level Inheritance: First class is inherited by second class,
# # second class is inherited by third class and so.....on

# # each derived class is the base class for the next class.

# class Rectangle:
#     def rec_area(self, height, width):
#         area = height * width
#         print("Area of Rectangle:", area)

# class Square(Rectangle):
#     def squ_area(self, side):
#         area = side * side
#         print("Area of Square:", area)

# class Traingle(Square):
#     def tri_area(self, length, breadth):
#         area = 0.5 * length * breadth
#         print("Area of Triangle:", area)

# obj = Traingle()
# obj.rec_area(10,20)
# obj.squ_area(12)
# obj.tri_area(12, 25)

# print("-----------------------------------------------")

# # Hierarchical Inheritance: When a single class is inherited by two or more than two classes simultaneously.

# # derived class may be two or more than two but base class should be one.

# class Rectangle:
#     def rec_area(self, height, width):
#         area = height * width
#         print("Area of Rectangle:", area)

# class Square(Rectangle):
#     def squ_area(self, side):
#         area = side * side
#         print("Area of Square:", area)

# class Traingle(Rectangle):
#     def tri_area(self, length, breadth):
#         area = 0.5 * length * breadth
#         print("Area of Triangle:", area)

# obj = Traingle()
# obj.rec_area(10,20)
# # obj.squ_area(12)
# obj.tri_area(12, 25)

# print("-----------------------------------------------")

# # Hybrid  Inheritance: The combination of two or more than two inheritance

# # It can be combination of any two or more than two inheritance (single, multiple, multi-level, hierarchical).

# class Rectangle:
#     def rec_area(self, height, width):
#         area = height * width
#         print("Area of Rectangle:", area)

# class Square:
#     def squ_area(self, side):
#         area = side * side
#         print("Area of Square:", area)

# class Traingle(Rectangle, Square):
#     def tri_area(self, length, breadth):
#         area = 0.5 * length * breadth
#         print("Area of Triangle:", area)

# class Circle(Traingle):
#     def cir_area(self, radius):
#         area = 3.14 * radius * radius
#         print("Area of Circle:", area)

# obj = Circle()
# obj.rec_area(10,20)
# obj.squ_area(12)
# obj.tri_area(12, 25)
# obj.cir_area(2.3)

'''
#inheritance
class vehicle:
   def __init__(self,make,model,year):
       self.make = make
       self.model = model
       self.year = year

class car(vehicle):
   def __init__(self,make,model,year,car_wheels):
       super().__init__(make,model,year)
       self.car_wheels = car_wheels
   def started(self):
       print("car is ready to drive")

class bike(vehicle):
   def __init__(self,make,model,year,bike_wheels):
       super().__init__(make,model,year)
       self.bike_wheels = bike_wheels
   def started(self):
       print("bike is ready to drive")

a = car("skoda","rapid",2023,4)
b = bike("royal enfield","himalayan",2020,2)

print(a.make)
print(a.model)
print(b.model)

a.started()
b.started()'''