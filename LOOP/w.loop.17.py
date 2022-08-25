sum=0
for i in range(1,8,1):
    fact=1
    for j in range(1,i+1,1):
        fact=fact*j
    div=i/fact
    sum=sum+div
print("sum=",sum)