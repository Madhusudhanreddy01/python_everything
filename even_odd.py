even_odd = [2,3,4,5,6,7,8,9,10]

even_=[]
odd_=[]

for i in even_odd:
    if i % 2 == 0:
        even_.append(i)
    else:
        odd_.append(i)

dict_= {"even":even_, "odd":odd_}
print(dict_)
