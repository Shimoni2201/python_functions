a=int(input("enter the num :"))
sum=0
b=a
while b>0:
    c=b%10
    sum= sum+(c**3)
    b//=10
if a==sum:
    print(a,"is an armstrong num")
else:
    print(a, "is not an armstrong num")
