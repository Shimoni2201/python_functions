msg=input("enter string:")
print(msg)
for i in range(len(msg)):
    x=msg[i:]+msg[:i]
    print("shift string:",x)