# duplicates in string

def string(word):
    res = []
    for i in word:
        k = word.count(i)
        if k>1 and i not in res:
            res.append(i)
    return res
           
'''word = input("enter the string = ")
k = string(word)
print(k)'''
