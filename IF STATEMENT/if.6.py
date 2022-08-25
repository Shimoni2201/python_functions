a=int(input("enter marks of math = "))
b=int(input("enter marks of sci = "))
c=int(input("enter marks of eng = "))

print("total = ",a+b+c)
avg=(a+b+c)/3
print("avg = ",avg)
if avg>=90:
    print("grade A")
elif avg>=80:
    print("grade B")
elif avg>=70:
     print("grade C")
elif avg>=60:
     print("grade D")
else :
     print("grade F")
