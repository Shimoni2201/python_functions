comp=['r','p','s']
import random
n=comp[random.randint(0,2)]
op="yes"
while op=="yes":
    user = input("enter your weapon(r/p/s):")
    print("user action:",user)
    print("comp action",n)
    if user==n:
        print("draw")
    elif user=="r":
        if n=="s":
            print("user wins")
        else:
            print("user loose")
    elif user=="s":
        if n=="r":
            print("user loose")
        else:
            print("user wins")
    elif user=="p":
        if n=="r":
            print("user wins")
        else:
            print("user loose")
    op=input("do you want to play again (yes/no)???")