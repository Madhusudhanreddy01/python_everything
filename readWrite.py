file = open("test.txt")

#Read all the contents of file
#Read n number of characters by passing parameter
# print(file.read(5))

#Read one single at a time readLine()
# print(file.readline())
# print(file.readline())



#Print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()


#values = [abc, madhu, xyz]
for line in file.readlines():
    print(line)

file.close()







