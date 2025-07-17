
# 1.
date,month,year = input().split('-')
print(f'{year}/{month}/{date}')

# 2.
n= int(input())
if n%2==0:
    print("even number")
else:
    print("odd number")

# 3.
s = input().lower()
s = s.translate(str.maketrans("aeiou","*****"))
print(s)

# 4.
l = list(map(float,input().split()))
print(sum(l))
print(max(l))

# 5.
credentials = ("admin","python123")
username = input()
password = input()
if credentials[0] == username and credentials:
    print("login succesfull")
else:
    print("access denied")

# 6.
names = set(input().split(','))
print(sorted(names))

# 7.
n=int(input())
data={}
max_val=0
res_name=''
for _ in range(n):
    name,marks=input().split()
    marks=int(marks)
    if marks>max_val:
        max_val=marks
        res_name=name
        
    data[name]=marks

# 8. 
sen = input().split()
for i in sen:
    print(i[::-1],end=' ')

# 9.
l = list(map(int,input().split()))
while (0 in l):
    l.remove(0)
print(l) 


l = list(map(int,input().split()))
res = []
for i in l:
    if i!= 0:
        res.append(i)
        print(res) 
        
# 10.
line = input()
data = {}
for i in line:
    if i not in data and i!=0:
        data[i]=line.count(i)
print(data)

