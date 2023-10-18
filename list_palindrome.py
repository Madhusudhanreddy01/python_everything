def str_(strings_):
    list_=[]
    for i in strings_:
        if i == i[::-1]:
            list_.append(i)
    print(list_)

strings_= ['racecar', 'level', 'madam', 'madhu']
str_(strings_)