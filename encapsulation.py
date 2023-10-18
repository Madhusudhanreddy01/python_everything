# Python Encapsulation:
# Encapsulation is one of the key features of object-oriented programming. 
# Encapsulation refers to the bundling of attributes and methods inside a single class.

# It prevents outer classes from accessing and changing attributes and methods of a class. 
# This also helps to achieve data hiding.

# In Python, we denote private attributes using underscore as the prefix 
# i.e single _ or double __. For example,

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


print("---------------------------or---------------------------------")

#encapsulation

class hdfc_bank:
   def __init__(self,account_number,customer_name,balance = 0):
       self.account_number = account_number
       self.customer_name = customer_name
       self.balance = balance

   def deposit(self,amount):
       if amount > 0:
           self.balance += amount
       else:
           print("invalid deposit number")

   def withdraw(self,amount):
       if amount <= self.balance:
           self.balance -= amount
       else:
           print("insufficient balance")

   def get_balance(self):
       return self.balance

   def get_accountnumber(self):
       return self.account_number

   def get_customer_name(self):
       return self.customer_name

   def __str__(self):
       return f"Account Number: {self.__accountNumber}\nCustomer Name: {self.__customerName}\nBalance: {self.__balance}"


a = hdfc_bank("50100366141772","madhusudhan",1000)
print(a.balance)
print(a.customer_name)
a.deposit(1000)
print(a.balance)
a.withdraw(1997)
print(a.balance)