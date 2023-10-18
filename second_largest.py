def first_largest(val):
    largest_=val[0]
    for i in range(len(val)):
        if val[i] > largest_:
            largest_=val[i]
        

    second = val[0]
    for i in range(len(val)):
        if val[i] > second and val[i] != largest_:
            second = val[i]
    return second



values=[10,20,60,30,40,50]
print(first_largest(values))

print("-----------------------or---------------------")


def sec(s):
    first = s[0]
    second = s[0]

    for i in range(len(s)):
        if s[i] > first:
            second = first
            first = s[i]
        elif s[i] > second and s[i] < first:
            second = s[i]

    return second

s=[10,20,60,30,40,50]
print(sec(s))


print("-----------------------or---------------------")



def sec(s):
    first = 0
    second = 0

    for i in s:
        if i > first:
            second = first
            first = i
        elif i > second and i < first:
            second = i

    return second

s=[10,20,60,30,40,50]
print(sec(s))