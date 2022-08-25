pword=input("enter password")
length=lower=upper=digit= False
if len(pword)>=8:
    length=True
    for i in pword:
        if i.isupper():
            upper= True
        elif i.islower():
            lower= True
        elif i.isdigit():
            digit=True
if length and lower and upper and digit:
    print("password is valid")
else:
    print("password is invalid")