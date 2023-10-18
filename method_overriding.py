class Animal:

    # attributes and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        # super().eat()
        print("I like to eat bones")

# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()


# In the above example, the eat() method of the Dog subclass overrides the same method of the Animal superclass.

# Inside the Dog class, we have used

# # call method of superclass
# super().eat()
# to call the eat() method of the Animal superclass from the Dog subclass.

print("--------------------------------------or-------------------------------------------")

#method overriding

class animal:
   def make_sound(self):
       print("generic animal sound")
class cat(animal):
   def make_sound(self):
    #    super().make_sound()
       print("meow")

a = cat()
a.make_sound()