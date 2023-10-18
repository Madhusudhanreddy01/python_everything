def pal(a):
    a=a.lower()
    reverse_a=""
    for char in a:
        reverse_a=char + reverse_a
    if a==reverse_a:
        return "Palindrome"
    else:
        return "Not a Palindrome"

# a=input("Enter: ")
# print(pal(a))