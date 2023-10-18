list_=[1,2,2,3,4,5,6]
em_=[]

for i in list_:
    if i not in em_:
        em_.append(i)
print(em_)
