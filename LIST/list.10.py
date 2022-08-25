'''
list1=[1,2,3,4,5]
print(list1)
list2=list1[0]
list1[0]=list1[1]
list1[1]=list1[2]
list1[2]=list1[3]
list1[3]=list1[4]
list1[4]=list2
print(list1)
'''
list1=[]
user='y'
while user=='y':
    list1.append(int(input("enter num:")))
    user=input("do you want to continue(y/n)?")
print(list1)
for i in range (len(list1)):
    temp=list1[0]
    list1[0]=list1[i]
    list1[i]=temp
print(list1)
