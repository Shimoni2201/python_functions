def shut_down(s):
    if s=='yes':
        print("shutting down ")
    elif s=='no':
        print("shut down abort")
    else:
        print("sorry")
shut_down(s=input("do you want to shut down?"))