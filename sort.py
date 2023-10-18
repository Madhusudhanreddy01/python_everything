l=[24, 46, 20, 33, 1, 5]
# l.sort()
# print(l)

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)