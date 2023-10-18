# class items:
#     def __init__(self, cart):
#         self.cart= list(cart)
        
#     #special function
#     def __len__(self):
#         print("The total items are:")
#         return len(self.cart)#built-in function
# purchase = items(['apple', 'banana', 'mango','grapes'])
# print(len(purchase))#prints the body of the special function


class areaClass:
    def area(self,a,b=None,c=None,d=None):
        
        #when a and c are passed as arguments
        if a!=None and b!=None and a!=b and a!=c:
            print("Area of the triangle",(0.5*a*b))
            
         #when a,b,c and d are passed as arguments   
        elif(b!=None and c!=None and d!=None and a==b and a==c):
             print("Area of the square",(a*c))
                
        elif(b==None and c==None and d==None):
            print("Enter more numbers")
        else: 
            if(a==c):
                print("Area of the rectangle",(a*b))
            else:
                print("Area of the rectangle",(a*c))
        
obj=areaClass()
obj.area(33)
obj.area(19,8,77)#Area of the triangle 76.0
obj.area(18,18,18,18)#Area of the square 324
obj.area(72,38,72,38)#Area of the rectangle 2736


print("-------------------------or-------------------------------")

#method overloading

class add_method:
   def add(self,x,y):
       return x+y
   def add(self,x,y,z):
       return x+y+z

a = add_method()
print(a.add(2,3,4))
