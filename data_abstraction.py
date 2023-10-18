# # Data Abstraction: Abstraction means Data hiding, 

# # essential data is shown to the user or outside class and unessential data is hidden.

# # In python if we want to perform data hiding then it can be done by using double underscore(__) 

# # prefix with variables or functions then they can not be accessed outside that function.

# class Test1:
#     x = 10
#     y = 20

#     def myFun1(self):
#         print("This is function1")

# class Test2(Test1):
#     def myFun2(self):
#         print("This is function2")
#         print(self.x)
#         self.myFun1()

# obj=Test2()
# obj.myFun2()

# print("-------------------------------------------------------")

# # Example with data hiding:
# class Test1:
#     __x = 10
#     y = 20

#     def myFun1(self):
#         print("This is function1")

# class Test2(Test1):
#     def myFun2(self):
#         print("This is function2")
#         print(self.x)
#         self.myFun1()

# obj=Test2()
# obj.myFun2()


print("-------------------or--------------------")

#abstraction

from abc import ABC,abstractmethod

class shape(ABC):
   def area(self):
       pass

class square(shape):
   def __init__(self,side):
       self.side = side

   def area(self):
       return self.side * self.side

a = square(5)
print(a.area())
