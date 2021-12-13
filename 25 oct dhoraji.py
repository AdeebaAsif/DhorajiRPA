database=[
{"user_id":1,"first name":"Adeeba","last name":"Bano","age":18},{"user_id":2,"first name":"Bushra","last name":"Khan","age":24},{"user_id":3,"first name":"Musfirah","last name":"Qureshi","age":13}
]
for i in database:
    if i["age"]>=18:
        print(i)




data=[]
dic={}
n=int(input("Enter no.of students who got admission: "))
for i in range(1,n+1):
    std_id=int(input("Enter ID: "))
    first_name=input("First Name: ")
    last_name=input("Last Name: ")
    dic["Student_id"]=std_id
    dic["First Name"]=first_name
    dic["Last Name"]=last_name
data.append(dic)
print(data)






data=[]
dic={}
n=int(input("How many stds got admission in your school"))
o=int(input("Enter no.of data you want from user"))
for i in range(1,n+1):
    for i in range(1,o+1):
        k=input("Enter what info you want from student : ")
        v=eval(input("Enter it's value : "))
        dic[k]=v
    data.append(dic)
print(data)