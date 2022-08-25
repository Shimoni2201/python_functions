no1 = int(input("enter a year :"))
if  no1%4==0 :
    if no1%100==0:
        if no1%400==0:
           print(no1,"is a leap year")
        else :
            print(no1,"is not a leap year")
    else:
        print(no1, "is a leap year")
else :
    print(no1, "is not a leap year")