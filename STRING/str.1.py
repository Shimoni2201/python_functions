msg=input("enter string:")
msg=list(msg)
msg.sort()
print(msg)
print(msg[::2])
msg_vo=[c for c in msg if c=='a' or c=='i' or c=='o' or c=='u' or c=='e']
print(msg_vo)
vo="aeiou"  # vo=['a','e','u']
for character in vo:
    print(character ," :",msg.count(character))