l=[]
m=[]
n=[]
for i in range (int(input("size of list:"))):
    l.append(int(input("enter num in list1:")))
    m.append(int(input("enter num in list2:")))
    n.append(l[i]+m[i])
print(n)