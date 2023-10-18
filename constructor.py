#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100 #class variables
    #default constructor
    def __init__(self, a, b):
        self.firstNumber = a #instance variables
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())


# ---------------------------------------------------------------------------------------

'''# print("parameterized constructor--> constructor with parameter")
# class Student:
#     def __init__(self, name, roll):
#         print("Name:", name)
#         print("Rollno:", roll)

# s1=Student("madhu", 439)

print("--------------------------------------------")

print("non-parameterized constructor--> constructor with no parameter")
class Student:
    def __init__(self):
        print("Hi")
    def Info(self):
        print("Name: madhu")
        print("Rollno: 439")

s1=Student()
s1.Info()'''