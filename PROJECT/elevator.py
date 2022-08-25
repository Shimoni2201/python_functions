def is_nagetive(no,yes):
    if no <= 0:
        return True
    else :
        return False
class customer:
    user=int(input("enter num of customers?"))
    floor=int(input("enter num of floors?"))
    while is_nagetive(user,floor):
        user = int(input("enter num of customers?"))
        floor = int(input("enter num of floors?"))
    print(user,floor)
#class building:
#class elevator:
