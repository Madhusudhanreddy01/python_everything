# 1) Need to print prime numbers till 100
#   ex: 2,3,5,7,11,13.....97
#oneway__________________________________________________________
n=int(input())
for i in range(2, n+1):
    factors = 0
    for j in range(2, i-1):
        if (i%j)==0:
            factors = factors + 1

    if factors==0:
        print(i)

#Twoway________________________________________________________
import math
num = int(input())
for j in range(2, num+1):
    flag = False
    for i in range(2,math.floor(math.sqrt(j)+1)):
        if j % i == 0:
            flag = True
    
    if flag == False:
        print(j)
# _____________________________________________________________________________________________
# 2) Given list, need to find the duplicate number and missing number
#    input: [17,19,18,18,21] output: 18,20(duplicate,missing)
#    input: [28,31,31,29,30] output: 31,32(duplicate,missing)

a=input()
b=list(map(int,a[1:len(a)-1].split(",")))
duplicate=[]
missing=[]
first_no=b[0]-1
for i in b:
    count=b.count(i)
    if(count>1):
        duplicate.append(i)
    first_no+=1 
    if(first_no not in b):
        missing.append(first_no)
set_=list(set(duplicate))+missing
print(*set_)
