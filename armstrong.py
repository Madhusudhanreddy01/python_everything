def arm_(no):
    add=0
    length=len(no)
    for i in  no:
        store=int(i)**length
        add+=store
    if(str(add)==no):
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"

no=input("Enter:")
print(arm_(no))
