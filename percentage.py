math=float(input("Enter math's number: "))
phy=float(input("Enter physic's number: "))
comp=float(input("Enter computer's number: "))
eng=float(input("Enter english's number: "))
urdu=float(input("Enter urdu's number: "))
obt_marks=math+phy+comp+eng+urdu
total_marks=500
perc=obt_marks/total_marks*100
print("Your percentage is ",perc,"%")
if perc>=80 and perc<100:
    print("Your grade is A1")
elif perc>=70 and perc<80:
    print("Your grade is A")
elif perc>=60 and perc<70:
    print("Your grade is B")
elif perc>=50 and perc<60:
    print("Your grade is C")
elif perc>=40 and perc<50:
    print("Your grade is D")
elif perc==0 and perc<40:
    print("Your grade is F")
else:
    print("You have entered wrong number because the percentage is either less than or equal 0 or greater than 100")








print("There are 4 types of packages in our school.\npackage 1:50% discount on full fee\nPackage 2:30% discount on eight months fee\nPackage 3:10% discount on four months fee\nPackage 4:no discount on 2 less than 2 months fee")
month_fee=2000
def package_1():
    global yearly_fee
    yearly_fee=12*month_fee
    a=50/100*yearly_fee
    return a
def package_2():
    global eghtm_fee
    eghtm_fee=8*month_fee
    b=30/100*eghtm_fee
    return b
def package_3():
    global fourm_fee
    fourm_fee=4*month_fee
    c=10/100*eghtm_fee
    return c
def package_4():
    global twom_fee
    twom_fee=2*month_fee
    c=twom_fee
    return c
user=input("\nwhat package do you want? type '1' for package 1 type '2' for package 2 type '3' for package 3 type '4' for package 4: ")
if user=='1':
    print("amount payable before dicount was: ",yearly_fee)
    print("amount payable after discount for package 1 is ",package_1())
elif user=='2':
    print("amount payable before discount was ",eghtm_fee)
    print("amount after discount for package 2 is ",package_2())

elif user=='3':
    print("amount payable before discount was ",fourm_fee)
    print("amount after discount for package 3 is ",package_3()) 
elif user=='4':
    print("There is no dicount on package 4 ")
    print(package_4())
else:
    print("there is no such type of package")