month_fee=2000
def package_1():
    global yearly_fee
    yearly_fee=12*month_fee
    a=50/100*yearly_fee
    return a
def package_2():
    eghtm_fee=8*month_fee
    b=30/100*eghtm_fee
    return b
def package_3():
    fourm_fee=4*month_fee
    c=10/100*eghtm_fee
    return c
def package_4():
    twom_fee=2*month_fee
    c="no discount"
    return c
user=input("what package do you want? type '1' for package 1 type '2' for package 2 type '3' for package 3 type '4' for package 4: ")
if user=='1':
 print("amount after discount for package 1 is ",yearly_fee,package_1())   
elif user=='2':
    print("amount after discount for package 2 is ",package_2())
elif user=='3':
    print("amount after discount for package 3 is ",package_3()) 
elif user=='4':
    print("amount after discount for package 4 is ",package_4())  
else:
    print("there is no such type of package")