class Employee:
    # class attribute
    company = "Msys"
    # constructor
    def __init__(self, name, age, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary

# creating objects
emp1 = Employee("John", 34, 50000)
emp2 = Employee("Harry", 30, 60000)

# accessing class attributes using __class__ method
# syntax is-- instance.__class__.attribute
print(f"{emp1.name} and {emp2.name} work for {emp1.__class__.company}")

# accessing instance attributes
# syntax is-- instance.instance_attribute
print(f"{emp1.name}'s age is {emp1.age} and salary is {emp1.salary}")
print(f"{emp2.name}'s age is {emp2.age} and salary is {emp2.salary}")
