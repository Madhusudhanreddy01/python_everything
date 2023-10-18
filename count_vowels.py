# get the count, how many vowels in string

def string(word):
    vowels_= "AEIOUaeiou"
    count=0
    for i in word:
        if i in vowels_:
            count += 1

    return count


word = input("Enter the string: ")
print(string(word))
