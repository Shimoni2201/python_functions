msg=input("enter string:")
#print(msg[::2])
# for char in msg.upper():
#     print(char,":",msg.count(char))
# for char in msg.lower():
#     print(char,":",msg.count(char))
upper=0
lower=0
digit=0
space=0
for c in msg:
    if c.isupper():
        upper+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1
    elif c.islower():
        lower+=1
    else :
        print("invalid")
print("the num of uppercase:",upper)
print("the num of space:",space)
print("the num of digit:",digit)
print("the num of lowercase:",lower)