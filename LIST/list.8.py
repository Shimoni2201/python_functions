a=int(input("enter a num:"))
list1=[]
for i in range(1,a+1):
    if a%i==0:
        list1.append(i)
print("factors:",list1)