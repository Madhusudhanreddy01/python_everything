def arbr_(*args):
    results = 0
    for i in args:
        results += i
    return results

print(arbr_(1,2,3,4))

def key(**kwargs):
    results = 0
    for i in kwargs.values():
        results += i
    return results

print(key(a=1,b=2,c=3,d=4,e=5))