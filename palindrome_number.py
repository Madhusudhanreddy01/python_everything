def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
# x=int(input("Enter: "))
# print(isPalindrome(x))