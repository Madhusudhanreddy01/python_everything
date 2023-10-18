'''Given list, need to find the duplicate number and missing number
   input: [17,19,18,18,21] output: 18,20(duplicate,missing)
   input: [28,31,31,29,30] output: 31,32(duplicate,missing)'''
#oneway
# a=input()
# b=list(map(int,a[1:len(a)-1].split(",")))
# duplicate=[]
# missing=[]
# first_no=b[0]-1
# for i in b:
#     count=b.count(i)
#     if(count>1):
#         duplicate.append(i)
#     first_no+=1 
#     if(first_no not in b):
#         missing.append(first_no)
# set_=list(set(duplicate))+missing
# print(*set_)


#Another way
# def answer(x):
#     j = m = min(x)
#     repeated = missing = -1

#     while j < m + len(x):
#         i = j - m

#         if x[i] != j :
#             correct = x[i] - m

#             if x[i] != x[correct]:
#                 swap(x, i, correct)
#             else:
#                 repeated = x[i]
#                 j += 1
#         else:
#             j += 1

#     for i, v in enumerate(x):
#         if v -i != m:
#             missing = i + m

#     return (repeated, missing)


# def swap(x, i, correct):
#      x[i], x[correct] = x[correct], x[i]
     
# x = [28, 31, 31, 29, 30]
# repeated, missing = answer(x)
# print(repeated, missing)

#thirdway
# def result(x):
#     unique_sum = sum(set(x))
#     start = min(x)
#     end = start + len(x)

#     repeated = sum(x) - unique_sum
#     missing = sum(range(start, end)) - unique_sum

#     return (repeated, missing)

# x = [28, 31, 31, 29, 30]
# repeated, missing = result(x)
# print(repeated, missing)

#anotherway
# program to find the missing and duplicate numbers in the list
def findMissing(n):
    numbers = set(n)
    output = []
    for i in range(n[0],n[-1]):
        if i not in numbers:
            output.append(i)
    return output
def dupicate(n):
    a=[]
    b=[]
    for i in n:
        if i not in a:
            a+=[i]
        else:
            b+=[i]
    return b
List = [17,19,18,18,21]
print("duplicate ->",dupicate(List),"missing ->",findMissing(List))