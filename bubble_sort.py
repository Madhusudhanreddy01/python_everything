#It has only one rule --->compare and swap

# compares adjacent elements, and swaps them if they are out of order.

sort=[5, 3, 4, 1, 2]

len_=len(sort)-1
for i in range(len_,0,-1):
    for j in range(i):
        if sort[j] > sort[j+1]:
            sort[j], sort[j+1] = sort[j+1], sort[j]

print(sort)