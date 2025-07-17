
'''
n=input("Enter your DOB : ")
n=n[6:]+n[2:6]+n[:2]
n=n.replace("-","/")
print(n)



a = float(input("enter the numbers:"))
b = float(input("enter the numbers:"))
d = (a+b)
print(d)
if a>b and b>a:
    print (a)
else: 
    print(b)

    
    

a = list(map(float,input("enter the values:").split()))

total_price = sum(a)
max_prices = max(a)

print(total_price)
print(max_prices)



credentials = ("admin","python123")
username,password=credentials

user=input("Enter : ")
pasw=input("Enter password : ")

if user==username and pasw==password:
    print("Login sucessful")
else:
    print("Access Deined")


s=input("Enter names : ").split(",")
s=set(s)
m=list(s)
m.sort()
print(m)


d=eval(input())

m=max(d,key=d.get)
print(m)


s=input("Enter : ").split()
n=0
for i in s:
    print(s[n][::-1],end=" ")
    n+=1


s=input("Enter values : ").split()
s.remove('0')
print(s)

l = ["phones",'watch','facewash','bike','car']
for i in l:
    if i=='bike':
        continue
    print(i)
else:
    print("end of the store")

    
for row in range (6):
    for col in range (3):
        print('*',end=" ")
    print()


for row in range(10,0,-1):
    for col in range(row):
        print('*',end='  ')
    print()
    


for row in range(8):
    for col in range(row +1):
        print(row,end = " ")
    print()


for row in range(8):
    for col in range (8 - row):
        print(row,end = " ")
    print()

    

n = int(input("enter the number:"))

for row in range(n):
    for spa in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()
    '''
for row in range(8):
    for col in range(row +1):
        print('*',end = " ")
    print()
for row in range(9):
    for col in range (9 - row):
        print('*',end = " ")
    print()


