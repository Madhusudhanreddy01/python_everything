def perfect(a):
    sum_=0
    for i in range(1,a):
        if (a%i==0):
            sum_=sum_+(i)
    if(sum_==a):
        return "Perfect Number"
    else:
        return "Not a Perfect Number"

# a=int(input())
# print(perfect(a))
