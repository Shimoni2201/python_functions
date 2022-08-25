end=int(input("enter the limit"))
d=0
c=0
count=0
while end>0:
    a=int(input("enter a num"))
    if a>0:
        count=count+1
    elif a==0:
        c=c+1
    else :
        d=d+1
    end=end-1
print(count,c,d)