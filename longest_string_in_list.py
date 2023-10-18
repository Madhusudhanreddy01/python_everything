def string(my_list):
    longest_string = ""
    for i in my_list:
        if len(i) > len(longest_string):
            longest_string = i
    return longest_string



my_list =  ["M", "Pannala", "PMSR", "MSR"]
print(string(my_list))
