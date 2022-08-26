import random

b= random.randint(0,10)
user="yes"
# print(b)
while user=="yes" or user=="YES":
    a = int(input("enter a number:"))
    if 0<=a and a<=10:
        if a==b:
            print("both numbers are equal, no1 =",a,"no2 = ",b)

        elif a<b:
            print("the random number is higher, no1 =",a,"no2 = ",b)

        else:
            print("the input number is higher,  no1 =",a,"no2 = ",b)
        user = input("do you want to continue?")
    else:
        print("invalid input")
        user="yes"

