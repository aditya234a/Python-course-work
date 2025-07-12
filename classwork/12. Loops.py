'''
#    For loops:
#  how to print a table

num = int(input("enter the number:"))

for i in range(1,31):
    print(f'{num} * {i} = {num*i}')
    

s = 'praveen harhith varun sheshu krishna'.lower()
n= len(s)
ch = input("enter the char:").lower()

for i in range (n):
    if s[i]==ch:
        print(ch,i)

products = ['cycle','watch','laptop','mobile','mouse']
items = input("enter the items:").split()

for i in items:
    if i in products:
        print(products.index(i),i)
    else:
        print(f"{i} is not availble")

'''

#     While loops:

email,pwd = 'xyz@gmail.com','xyz@123'
max_attempts = 5

while max_attempts>0:
    usermail = input("enter the email:")
    password = input("enter the password:")

    if usermail==email and pwd==password:
        print("login successful")
        break
    else:
        print("invaild login")
    max_attempts-=1
else:
    print("try after some time.")