# Importing OS module
import os
# geting the current directory
cwd = os.getcwd()
# joining the current directory
path = os.path.join(cwd)
# creating list of path
files = os.listdir(path)
# using for loop
for file in files:
    # printing the file name
	print(os.path.join(path, file))