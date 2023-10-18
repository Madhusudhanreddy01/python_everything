l1 = ["siya", "priya", "jiya"]
l2 = [170, 120, 130]

for i in range(len(l1)):
    for j in range(i+1, len(l2)):
        if str(l1[i]) > str(l2[j]):
            l2[i], l2[j] = l2[j], l2[i]
            l1[i], l1[j] = l1[j], l1[i]

print(l1)

# l1=["siya","priya","jiya"]
# l2=[170,120,130]
# di={}
# final = []
# for i in range(len(l1)):
#     di[l2[i]]=l1[i]
# # print(di)
# l2.sort(reverse=True)
# # print(l2)
# for j in l2:
#     # print(di[j])
#     final.append(di[j])
# print(final)