class Numbers:
    def add_digits(self, num):
        while num >=10:
            sum_digit = 0
            while num > 0:
                sum_digit += num % 10
                num //= 10
            num = sum_digit
        return "The single digit of the given number {} is = {}".format(value,num)

        
obj=Numbers()
value=int(input("Enter the value:"))
print(obj.add_digits(value))