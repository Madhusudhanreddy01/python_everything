#1
list_=[(5,6),{"a", "b"}, [5,1]]
print(dict(list_))
print("------------------------")
#2
print(dict(a=1, b=(1,2), c=[1,2,3], d={1,2,3}))
print("------------------------")
#3
keys=["a","b","c"]
values=[1,2,3,4]
print(dict(zip(keys, values)))
print("------------------------")
#4
madhu={1:2,"want":["I", "will", "come"],"yes":{4,5,6}}
print(madhu["want"])
print(madhu.get("yes"))
print("------------------------")
#5
madhu={1:2,"want":["I", "will", "come"],"yes":{4,5,6}}
print(madhu.pop("want"))
print(madhu)
print("------------------------")
#6
madhu={1:2,"want":["I", "will", "come"],"yes":{4,5,6}}
del madhu["yes"]
print(madhu)
print("------------------------")
#7
madhu={1:2,"want":["I", "will", "come"],"yes":{4,5,6}}
x=madhu.popitem()
print(x)
print(madhu)
print("------------------------")
#8
madhu={1:2,"want":["I", "will", "come"],"yes":{4,5,6}}
x=madhu.clear()
print(x)
print(madhu)
print("------------------------")
#9
madhu={1:2,"want":["I", "will", "come"],"yes":{4,5,6}}
x=madhu.copy()


