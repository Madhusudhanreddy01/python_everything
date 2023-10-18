# Given number check prime number or not a prime number

# number = int(input("Enter a number = "))
# count = 0

def check(number):
    count = 0
    if number <2:
        return False
        
    else:
        for i in range(2,number+1):
            if number % i == 0:
                count += 1
        if count == 1:
            return True
        else:
            return False
