# 1.Arithmetic Operators
a = 20
b = 10

print("Adiition(+):",a+b)                    #Addition(+): 30

print("Subtraction(-):",a-b)                 #Subtraction(-): 10

print("Multiplication(*):",a*b)              #Multiplication(*): 200

print("Division(/):",a/b)                    #Division(/): 2.0

print("Floor Division(//):",a//b)            #Floor Division(//): 2

print("Modulus(%):",a%b)                     #Modulus(%): 0

print("Exponentiation(**):",a**b)            #Exponentiation(**): 10240000000000
 
# 2.Comparison Operators
print("Equal to(==):",a==b)                        #Equal to(==): False
print("Equal to(==):",a==a)                        #Equal to(==): True

print("Not Equal to(!=):",a!=b)                    #Not Equal to(!=): True
print("Not Equal to(!=):",a!=a)                    #Not Equal to(!=): False

print("Greater than(>):",a>b)                      #Greater than(>): True
print("Greater than(>):",b>a)                      #Greater than(>): Flase

print("Less than(-):",a<b)                         #Less than(-): False
print("Less than(-):",b<a)                         #Less than(-): True

print("Greater than or Equal to(>=):",a>=b)        #Greater than or Equal to(>=): True
print("Greater than or Equal to(>=):",b>=a)        #Greater than or Equal to(>=): Flase

print("Less than or Equal to (<=):",a<=b)          #Less than or Equal to (<=): False
print("Less than or Equal to (<=):",b<=a)          #Less than or Equal to (<=): True

# 3.Assignment Operators
c = 5
print("Assign(=):",c)                                 #Assign(=): 5

c+=3
print("Add & Assign(+=):",c)                          #Add & Assign(+=): 8

c-=2
print("Subtract & Assign(-=):",c)                     #Subtract & Assign(-=): 6

c*=4
print("Multiple & Assign(=):",c)                      #Multiple & Assign(=): 24

c/=2
print("Divide & Assign(/=):",c)                       #Divide & Assign(/=): 12.0

c//=3
print("Floor Divide & Assign(//=):",c)                #Floor Divide & Assign(//=): 4.0

c%=2
print("Modulus & Assign(%=):",c)                      #Modulus & Assign(%=): 0.0

c**=3
print(" Exponentiate & Assign(=):",c)                 #Exponentiate & Assign(=): 0.0

# 4.Logical Operators
 
print(a > 10 and b < 20)

print(a > 10 or b<20)

print(not(a>10))

# 5.Membership Operators

d = {
    'name':'tarak',
    'age':40,

    'name':'arjun',
    'age':41

}
print(type(d))                                                       #<class 'dict'>
print('tarak' not in d)                                              #True
print('name' in d)                                                   #True

fav_movies = ["Darling","Temper","Businessman","Badri"]
print('Darling' not in fav_movies)                                   #False
print('Badri' in fav_movies)                                         #True
print(type(fav_movies))                                              #<class 'list'>

# 6.Identity Operators

k=[1,2,5,4]
l=[1,2,5,4]
print("IS:", k is l)            #False
print("IS NOT:", k is not l)    #True

# 7.Bitwise Operators

x=4                                 #Binary= 0 1 0 0
y=6                                 #Binary= 0 1 1 0
                                             
print("AND(&):", x&y)               # 0 1 0 0 = 4
print("OR(|):", x|y)                # 0 1 1 0 = 6
print("XOR(^):", x^y)               # 0 0 1 0 = 2       Opposite reactions can be True
print("NOT(~):", ~x)                #  [~n = -(n + 1)]
print("NOT(~):", ~y)                #  [~n = -(n + 1)]


