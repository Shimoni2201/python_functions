list1=[]
user=1
for i in range (20):
    import random
    list1.append((random.randint(0,100)))

print(list1)
print("avg:",sum(list1)/20)
print("max:",max(list1))
print("min:",min(list1))
list1.sort()
print("second largest:",list1[-2])
print("second smallest:",list1[1])
for value in (list1):
    if value % 2 == 0:
        print("even num:", value)
