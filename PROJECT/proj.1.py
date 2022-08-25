user="yes"
while user=="yes":
    a = int(input("enter a num :"))
    b = int(input("enter a num :"))
    sum=0
    while b>0:
        print("A=",a,"B=",b)
        if b%2!=0:
            print( "B is odd, we add A to product:",a)
            sum=sum+a
            b=int(b/2)
            a=a*2
        else:
            b=int(b/2)
            a=a*2
    print("multiplication =",sum)
    user=input("do you want to continue(yes/no)?")
