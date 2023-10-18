# program to find the missing numbers in the list
def findMissing(n):
    numbers = set(n)
    output = []
    for i in range( n[0],n[-1]):
        if i not in numbers:
            output.append(i)
    return output
List = [17,19,18,18,21,23]
print("missing ->",findMissing(List))
List = [2,3,5,6,8]
print("missing ->",findMissing(List))