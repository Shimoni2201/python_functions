op=1
customer= []
title=["id","name","book","date1","date2","price"]
while op!=6:
    print("\tLIB SYSTEM")
    print("\t1.Entry")
    print("\t2.View")
    print("\t3.Search by id")
    print("\t4.Search by book name")
    print("\t5.exit")
    op=int(input("enter your option:"))
    if op==1:
        op1='y'
        while op1=='y':
            student = []
            student.append(int(input("Enter No:")))
            student.append(input("Enter Name:"))
            student.append(input("Book issued:"))
            student.append(input("Date of issued:"))
            student.append(int(input("How many days you want:")))
            price=50*student[4]
            student.append(price)
            op1 = (input("do you want to continue(y/n)?:"))
            customer.append(student)

    elif op==2:
        for student in customer:
            for t,value in zip(title[0:],student[0:]):
                print(t,value)
    elif op==3:
        s_id=int(input("enter id :"))
        for student in customer:
            if s_id==student[0]:
                for t,value in zip(title[0:],student[0:]):
                    print(t,value)
    elif op==4:
        b_name=input("enter book name:")
        for student in customer:
            if b_name==student[2]:
                for t,value in zip(title[0:],student[0:]):
                    print(t,value)
    elif op==5:
        print("you are exited")
    else:
        print("invalid")




