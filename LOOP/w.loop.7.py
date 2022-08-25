a=int(input("enter a num :"))
sum=0
while a>0:
    c=a%10
    sum=sum+c
    a=int(a/10)
print(sum)
