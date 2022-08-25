a=int(input("enter a num :"))
b=0
i=2
while(i<a//2):
    if(a%i==0):
        b=b+1
    i=i+1
if(b==0 and a!=1):
    print(a,"is prime number")
else:
    print(a,"not a prime")