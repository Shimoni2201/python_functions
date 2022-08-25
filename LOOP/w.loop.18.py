n=int(input("enter limit :"))
total=0
for i in range (1,n+1):
    total= total+((-1/i)**i)
print("sum=",abs(total))