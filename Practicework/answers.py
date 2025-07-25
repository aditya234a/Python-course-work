
# example-1
n = float(input("enter the salary:"))
if n<=250000:
    print("no tax")
elif n<=500000:
    print((n-250000)*0.05)
elif n<=1000000:
    print((n-500000)*0.20)
else:
    print((n-1000000)*0.30)

# example-2
n = int(input("enter th members:"))
total = 0
for i in range(n):
    if i<=5:
        print("ticket free")
    elif i<=18:
        print(total+=100)
    elif i<=60:
     print(total+=150)
    else:
        print(total+=120)
print(total)

# example-6
n = int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

# example-7
n = {
    1:{'month':'one month','fee':500},
    2:{'quaterly':'six months','fee':1300},
    3:{'yearly':'twelve months','fee':5000}       
}
choice=int(input("enter one choice in gym:"))
a = int(input("enter no.of people:"))
if choice in n:
    print(n[choice]['fee'] *a)
    
# example-8
t =int(input("enter the total bill:"))
if t>=0 and t<=999:
    print(f'Total bill:{t}')
elif t>=1000 and t<=4999:
    print(f'Total bill:{t-((t/100)*5)}')
elif t>=5000 and t<=9999:
    print(f'Total bill:{t-((t/100)*10)}')
else:
    print(f'Total bill:{t-((t/100)*15)}')

# example-9
pin = '1234'
attempt = 0
max_attempts = 3
while attempt< max_attempts:
    pin1=input("enter your pin:").strip()
    if pin==pin1 and len(pin1)==4:
        print("access")
        break
    else:
        print("pin incorrect")
        attempt+=1
else:
    print("atm blocked.try again later.")

