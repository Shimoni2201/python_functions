a=input("enter a num : ")
print(a)
print(len(a))
b=""
i=len(a)
while i>0:
     b+=a[i-1]
     i=i-1
     print(b)
