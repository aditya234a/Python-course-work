
#  1. if - condition statement

print("Traffic Signals".center(50,"*"))

s = input("enter the status(R O G):")

if s=='R':
    print("STOP")
if s=='O':
    print("READY")
if s=='G':
    print("GO")



 # 2. else - condition statement

print("Welcome To Amazon Store".center(50,"*"))

items = ['shoes','smartwatch','bags','phone','airpods','toycar']


searchinput = input("enter the items:").lower()

if searchinput in items:
    print(f"{searchinput} found. buy now !!!")
else:
    print(f'{searchinput} is out of stock now. we will notify you.')



# weekend budget plan 

print("Bubget Plan".center(50,"*"))

amount = int(input("enter the amountyou can spend for weekend:"))

if amount>200000:
    print("trip to goa")
elif amount>15000:
    print("go for shopping")
elif amount>10000:
    print("clubingg")
elif amount>5000:
    print("dinner")
elif amount>1000:
    print("go for movie")
elif amount>500:
    print("go for street food")
else:
    print("save the money and sleep")



#  Grading System

print("Student Grade".center(100,"*"))

data = {
    1:{'name':'praveen','attempt_status':False,'python':0,'sql':0,'powerbi':0},
    2:{'name':'mani','attempt_status':True,'python':100,'sql':90,'powerbi':80},
    3:{'name':'sheshu','attempt_status':True,'python':90,'sql':70,'powerbi':60},
    4:{'name':'eswar','attempt_status':True,'python':100,'sql':60,'powerbi':70},
    5:{'name':'vikas','attempt_status':True,'python':60,'sql':40,'powerbi':90},

}
stuid = int(input("enter the student id :"))

if data[stuid]['attempt_status'] :
    total=(data[stuid]['python']+data[stuid]['sql']+data[stuid]['powerbi'])/3
    if total>90:
        print(f'Congrats!!!\n{data[stuid]["name"]} got "A" grade')
    elif total>75:
        print(f'good!!!\n{data[stuid]["name"]} got "B" grade')
    elif total>60:
        print(f'improve!!!\n{data[stuid]["name"]} got "C" grade')
    elif total>35:
        print(f'just passed!!!\n{data[stuid]["name"]} got "D" grade')
    else:
        print(f'Better luck next time!!!\n{data[stuid]["name"]} failed')

else:
    print(f'{data[stuid]["name"]} is not attempted the exam.')
              



