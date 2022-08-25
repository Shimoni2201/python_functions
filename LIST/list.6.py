list1=[]
n=int(input("enter end "))
for i in range (n):
    import random
    list1.append((random.randint(0,50)))
print(list1)
for value in list1:
    value=value**2
    print(value)
list2=[]
str1='abcdefghijklmnopqrstuvwxyz'
for a in range(1,len(str1)):
    c=(str1[a])*(a)
    list2.append(c)
print(list2)