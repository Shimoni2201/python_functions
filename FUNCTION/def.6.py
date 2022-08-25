def cube(num):
    a=num**3
    print("cube:",a)
def by_three(num):
    if num%3==0:
        cube(num)
    else:
        print("invalid")
by_three(num=int(input("enter num:")))