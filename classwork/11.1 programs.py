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