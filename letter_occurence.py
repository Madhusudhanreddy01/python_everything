def letter_(a, b):
    count=0
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            count += 1

    return  ("The number of occurrences of", b, "in", a, "is", count)

# a=input()
# b=input()
# print(letter_(a,b))
