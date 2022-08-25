a=int(input("enter a num "))
b=a
c=0
while b>0:
    d=b%10
    c=d+c*10
    b=int(b/10)
if a==c:
    print(a,"is palindrome")
else:
    print(a, "is not palindrome")