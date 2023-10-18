def word_(a):
    words=a.split()
    dict_={}
    for i in words:
        dict_[i]=len(i)
    return dict_

words="I am Madhusudhan"
print(word_(words))