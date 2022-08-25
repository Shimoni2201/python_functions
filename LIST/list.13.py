list1=[]
a=[]
for i in range (int(input("enter end num:"))):
    list1.append(int(input("enter num:")))
print(list1)
for i in list1:
    if i not in a:
        a.append(i)
print(a)