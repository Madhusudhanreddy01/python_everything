# class Parrot:

#     # class attribute
#     name = ""
#     age = 0

# # create parrot1 object
# parrot1 = Parrot()
# parrot1.name = "Blu"
# parrot1.age = 10

# # create another object parrot2
# parrot2 = Parrot()
# parrot2.name = "Woo"
# parrot2.age = 15

# # access attributes
# print(f"{parrot1.name} is {parrot1.age} years old")
# print(f"{parrot2.name} is {parrot2.age} years old")


# print("-------------------or---------------------")

# class Student():
#     name = "madhu"
#     roll = 439

# s1=Student()

# print("Name:", s1.name)
# print("Roll-no:", s1.roll)

print("-------------------or---------------------")
print("class with variable and function:")
class Student():
    name = "madhu"
    roll = 439
    marks = 60.76

    def showInfo(self):
        print("Name:", s1.name)
        print("Roll-no:", s1.roll)
        print("marks:", s1.marks)



s1=Student()
s1.showInfo()

print("----->To access a class varaibles inside the function self keyword is used because self refers to the current class object")

# -----------------------------------------------------------------------------------

'''**Classes and Objects**

A class is a blueprint for creating objects. It defines the attributes and methods that 
objects of that class will have. An object is an instance of a class. 
It has its own unique set of attribute values and can call the methods defined in the class.

Here is an example of a class and object in Python:

python'''

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} the {self.breed} says woof!")

# Create a new Dog object
fido = Dog("Fido", "Golden Retriever", 3)

# Call the bark() method on the fido object
fido.bark()


'''Output:

```
Fido the Golden Retriever says woof!
```'''



