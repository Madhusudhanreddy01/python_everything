n=int(input("enter:"))
a=0
b=1
for i in range(n):
    # print(a,end=' ')
    temp=a
    c=a+b
    a=b
    b=c
print(temp)