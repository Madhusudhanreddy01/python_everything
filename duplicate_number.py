# program to find the duplicate numbers in the list
def duplicate(n):
    a=[]
    b=[]
    for i in n:
        if i not in a:
            a+=[i]
        else:
            b+=[i]
    return b
List = [17,19,18,18,21]
print("duplicate ->",duplicate(List))
List = [2,3,4,5,6,4,7]
print("duplicate ->",duplicate(List))