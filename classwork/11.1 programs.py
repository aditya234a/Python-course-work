'''
seats ={
    'L1':True,
    'L2':True,
    'U1':True,
    'U2':False,
}

print("Bus seats:",seats.keys())

seatid = input("enter the seat number to book:").upper()

if seatid in seats:
    if seats[seatid]:
        print("Seat is avaliable. You can book")
    else:
        print("Seat is not avaliable. Pick other one")
else:
    print("Chooce the seat number properly")
          


print("Check number positive or negitive".center (50,"*"))

num = int(input("enter the number:"))

if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero")


print("check the year leap or not".center(50,"*"))

year = int(input("enter the year:"))

if year % 400 or year % 4==0 and year % 100!=0:

    print(f'{year} is leaf year')

else:

    print(f'{year} is not a leaf year')


a = int(input("enter the number:"))

if a%2==0:
    print("even")
else:
    print("odd")




a = int(input("enter the number:"))
if a%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")    

a = int(input("enter the number:"))
if a%3==0 and a%7==0:
    print("both are divisible by 3 and 7")
elif a%7==0:
    print("divisible by 7")
elif a%3==0:
    print("divisible by 3")
else:
    print("both are not divisible 3 and 7")
    
a = int(input("enter the marks:"))
if a>=35:
    print("pass")
else:
    print("fail")
    

a = int(input("enter the number:"))
if a>=100 and a<=999:
    print("it is a three digit number")
else:
    print("it is a not three digit number")
    
    
a = int(input("enter the num1:"))
b = int(input("enter the num2:"))
if a>b:
    print(a,"is a greater than",b)
elif b>a:
    print(b,"is a greater than",a)
else:
    print(a,"is equal numbers",b)
    

a = int(input("enter the num1:"))
b = int(input("enter the num2:"))
if a<b:
    print(a,"less than",b)
elif b<a:
    print(b,"less than",a)
else:
    print(a,"is equal numbers",b)
    

a = int(input("enter the number:"))
if a==0:
    print("number is zero")
else:
    (print("nunber is not zero"))

    
a = int(input("enter the number:"))
if a%10==0:
    print("multiple by 10")
else:
    print("not multiple by 10")
    

a = int(input("enter the age:"))
if a>=18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

    
a = int(input("enter the number:"))
if a>=1 and a<=100:
    print("its a range")
else:
    print("its a not range")
    

a = int(input("enter the num1:"))
b = int(input("enter the num2:"))

if b**2==a:
    print(a,"square of",b)
else:
    print(a,"not square of",b)
    
a = input("enter the name1:").lower()
b = input("enter the name2:").lower()
if a==b:
    print("strings are equal")
else:
    print("strings are not equal")
'''
a = int(input("enter the number:"))
if a*1==0 :
    print("its a prime number")
else:
    print("its not a prime number")