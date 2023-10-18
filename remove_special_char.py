l="my@office#is!in@jpnagar"

res=""

for i in l:
    if i in "!@#$%^&*":
        res += " "
    else:
        res += i

print(res)