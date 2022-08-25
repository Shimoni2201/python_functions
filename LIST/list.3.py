list1=[8,9,10]
print(list1)
list1[1]=17
list1.append(4)
list1.append(5)
list1.append(6)
print(list1)
list1.remove(list1[0])
print(list1)
list1.sort()
print(list1)
list2=list1*2
print("double list:",list2)
list2.insert(3,25)
print(list2)