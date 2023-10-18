#overridding

# class a:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        

#     def add(self):
#         c = self.a+self.b
#         print(c)

# class b(a):
#     # def __init__(self,a,b):
#     #     self.a = a
#     #     self.b = b
#     def add(self):
#         c = self.a * self.b
#         print(c)


# obj =a(3,5)
# obj.add()

# obj = b(3,5)
# obj.add()

#Encapsulation
class a:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        #protected variable
        self._d=a+b
        #private variable
        self.__e = 1+2
        

    def add(self):
        c = self.a+self.b
        print(c+self._d)
        print(c+self.__e)


class b(a):
    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b
    def add(self):
        c = self.a * self.b
        print(c)
        print(self._d)
        print(self.__e)


obj =a(3,5)
print(obj._d)
# print(obj.__e)
obj.add()

obj = b(3,5)
obj.add()