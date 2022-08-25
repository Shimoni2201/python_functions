list1=[]
count=0
res=0
for i in range (7):
    import random
    list1.append((random.randint(0,1)))
#print(list1)
    if list1[i]!=0:
        count=0
    else:
        count+=1
        res=count
print(list1)
print(res)