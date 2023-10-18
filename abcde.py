str_="abcde"

res = ""
c=0
for i in range(len(str_)):
    res += str_[c]
    c+=1
    res += str(c)
print(res)
