a="Nittin and his mom went to a park last friday His Mom observed that the weather was too cool If we reverse the number 1331 then we also get 1331" 
b=a.split(" ")
# print(len(b))
list_=[]
for i in range(len(b)):
    c=b[i]
    # print(c)
    c=(b[i][::-1]).upper()
    # print(c)
    d=b[i].upper()
    # print(d)
    if (c==d):
        if(len(d)!=1):
            list_.append(d)
set_=sorted(list(set(list_)))
# print(set_)
# dict_={}
# for i in set_:
#     dict_[i]=list_.count(i)
# print(dict_)


c = 0
for i in set_:
    c += list_.count(i)
print(c)



print("-------------------------or--------------------")

input_="Nittin and hi mom went to park last Friday Nittin's Mom observed that the weather was tool cool if reverse the number 1331 then we also get 1331".split(" ")
store=[]
for i in input_:
    x=i.lower()
    if(x==x[::-1]):
       store.append(x)
result={}
for i in set(store):
    result[i]=store.count(i) 
print("count :"+str(sum(result.values())))