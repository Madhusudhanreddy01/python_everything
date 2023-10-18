# # importing os module
# import os   
# # os.mkdir method
# os.mkdir("D:\Python\os_path\old") 

# -----------------------------------------------

# # importing os module
# import os   
# # os.getcwd method
# print(os.getcwd())  

# ---------------------------------------------

# # Importing os module
# import os
# # python os path join method
# combined_path = os.path.join("D:\Python\os_path", "os.py")
# # printing the combined path
# print(combined_path)

#---------------------------------------------

# # Importing os module
# import os
# # absolute path
# path = "/Home"
# # python os path join method
# combined_path = os.path.join(path, "tutorials", "main_file.py")
# # printing the combined path
# print(combined_path)

# -------------------------------------------------

# # Importing os module
# import os
# # absolute path
# path = "/Home"
# # python os path join method
# combined_path = os.path.join("tutorials", path, "main_file.py")
# # printing the combined path
# print(combined_path)

# ----------------------------------------------
# # Importing os module
# import os
# # absolute path
# path = "/Home"
# # python os path join method
# combined_path = os.path.join("tutorials", "main_file.py", path)
# # printing the combined path
# print(combined_path)

# ----------------------------------------------------
# # Importing os module
# import os
# # absolute path
# path = "/Home"
# # python os path join method
# combined_path = os.path.join(path, "tutorials", "main_file.py", "")
# # printing the combined path
# print(combined_path)
# --------------------------------------
# # Importing os module
# import os
# # python os path join method
# combined_path = os.path.join( "", "", "")
# # printing the combined path
# print(combined_path)

# ---------------------------------------------------

# # Importing os module
# import os
# # list
# path = ["home", "tutorial", "main.py"]
# # python os path join method
# combined_path = os.path.join(*path)
# # printing the combined path
# print(combined_path)

# --------------------------------------------

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





