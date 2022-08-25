str=input("enter your string")
dic={}
for i in str:
    dic[i]=dic.get(i,0)+1
print(dic)
