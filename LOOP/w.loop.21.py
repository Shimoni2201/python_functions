num1=int(input("enter a num :"))
num2=int(input("enter a num :"))
tol=0
sign=-1
for i in range (0,num1):
    p=1
    fact=1
        for j in range (1,i+1):
            p=p*num1
            fact=fact*j
     sign= -1*sign
     tol=tol+sign*p/fact
    i=i+2
print("sin(",x,") =",tol)

