'''

 level -0
   submenu
   search by billno
   search by product name :

'''



from Vendor import Vendor
from Customer import Customer

billbook={"Vendor":[],"Customer":[]}
def menu(title):
    for i,t in zip(range(len(title)),title):
        print("press ",i ,"for ",t)

    op=int(input("Enter your option :"))
    return op

def format(title):
    print("\t\t",title)
    print("\t\t",end="")
    for i in range(len(title)):
        print("-",end="")
    print("\n")

menu_list=["Purchase","Sales","Exit"]
sub_menu_list=["Entry","View","Search by bill no.","Search by product name","Main Menu"]
op1=0
while op1 != menu_list.index("Exit"):
    format("SunShine Pvt Ltd ")
    op1=menu(menu_list)

    if op1 == menu_list.index("Purchase"):
        format("Purchase")
        op2=0
        while op2 != sub_menu_list.index("Main Menu"):
            op2=menu(sub_menu_list)

            if op2 == sub_menu_list.index("Entry"):
                format("Entry")
                op3="yes"
                while op3.lower()=="yes":
                    vendor=Vendor()
                    vendor.setVendor()
                    billbook["Vendor"].append(vendor)
                    op3=input("do you want to add another bill(yes/no)?:")
            elif op2== sub_menu_list.index("View"):
                format("View")
                for vendor in billbook["Vendor"]:
                    vendor.getVendor()
                    format("====================")
            elif op2== sub_menu_list.index("Search by bill no."):
                format("Search by bill no.")
                bill = (input("Enter the bill no."))
                for billno in billbook["Vendor"]:
                    if bill == billno:
                        vendor.getVendor()
                format("====================")
            # elif op2 == sub_menu_list.index("Search by product name"):
            #     format("Search by product name")
            #     product=input("Enter product name ")
            #     if product not in billbook.values():
            #         vendor.getVendor()
            #     format("====================")
            elif op2 == sub_menu_list.index("Main Menu"):
                print("Back to main menu ")
            else :
                print("Wrong option is selected try again !!")

    elif op1== menu_list.index("Sales"):
        format("Sales")
        op2=0
        while op2 != sub_menu_list.index("Main Menu"):
            op2 = menu(sub_menu_list)

            if op2 == sub_menu_list.index("Entry"):
                format("Entry")
                op3 = "yes"
                while op3.lower() == "yes":
                    customer = Customer()
                    customer.setCustomer()
                    billbook["Customer"].append(customer)
                    op3 = input("do you want to add another bill(yes/no)?:")
            elif op2 == sub_menu_list.index("View"):
                format("View")
                for customer in billbook["Customer"]:
                    customer.getCustomer()
                    format("====================")
            elif op2== sub_menu_list.index("Search by bill no."):
                format("Search by billno.")
            elif op2==sub_menu_list.index("Search by product name"):
                format("Search by product name")
            elif op2 == sub_menu_list.index("Main Menu"):
                print("Back to main menu ")
            else:
                print("Wrong option is selected try again !!")

    elif op1 == menu_list.index("Exit"):
        print("you are exited ")
    else :
        print(" wrong option selected try again !!")
