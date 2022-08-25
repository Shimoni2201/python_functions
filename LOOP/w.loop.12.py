a=int(input("enter a num "))
b=int(input("enter a num "))
i=1
while b!=0:
    temp=b
    b=a%b
    a=temp
gcd=a
print(gcd)
