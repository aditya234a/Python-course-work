'''
def reverse(s,ind):
    if ind==len(s):
        return
    reverse(s,ind+1)
    print(s[ind],end = ' ')
    
s = input("enter the string:")
reverse(s,0)


def sumofdigits(n):
    if n == 0:
        return n
    return n % 10 + sumofdigits(n//10)

n = int(input("enter the number:"))
print("sum of digits is:", sumofdigits(n))


def productofdigits(n):
    if n ==0:
        return 2
    return n%10 * productofdigits(n//10)

n =int(input("enter the number:"))
print("product of digits is:",productofdigits(n))


def addnumbers(n):
    if n ==0:
        return 0
    return n%10 + addnumbers(n//10)
n = int(input("enter the numbers:"))
print("add the two numbers:",addnumbers(n))


def countnumbers(n):
    if n<10:
        return 1
    return 1 + countnumbers(n//10)
n = int(input("enter the numbers:"))
print("count the numbers:",countnumbers(n))



import operator as opr

a = int(input("enter the a:"))
b = int(input("enter the b:"))

option = input("enter the option(+-*/%**):")

if option=='+':
    opr.add(a,b)
elif option=='-':
    opr.sub(a,b)
    



import platform

print(platform.system())
print(platform.release())
print(platform.processor())


import sys

#print(sys.argv)
#print(sys.path)
print(sys.version)



class instagram:
    def __init__(self,username,password):
        print("welcome to the instagram")
        self.bio=''
        self.post=[]
        self.followers={}
        self.following={}
        self.username=username
        self.password=password
        print(f"Hello {self.username} login successfull")

manikanta= instagram("manikanta","mani@123!")



class instagram:
    def __init__(self,username,password):
        print("welcome to the instagram")
        self._bio=''
        self.post=[]
        self.followers=[]
        self.following=[]
        self.username=username
        self.__password=password
        print(f"Hello {self.username} login successfull")


    @property
    def externalbio(self):
        return self._bio

    @externalbio.setter
    def externalbio(self,upd_bio):
        self._bio=upd_bio

    def showPassword(self):
        return self.__password
    def updatePassword(self,new_pwd):
        self.__password=new_pwd
manikanta=instagram("manikanta","mani@1234!")

#public var-accessing
print("Bio:",manikanta._bio)
print("Post:",manikanta.post)
print("Followers:",manikanta.followers)
print("Following:",manikanta.following)
print("Username:",manikanta.username)

#modifying - public var
manikanta._bio="Peace"
manikanta.post.append("Python-course.png")
manikanta.followers.extend(["Peace","kiran"])
manikanta.following.extend(["ntr","virat"])
manikanta.username='manikanta_.'

print("\nAfter updating: ")
print("Bio:",manikanta._bio)
print("Post:",manikanta.post)
print("Followers:",manikanta.followers)
print("Following:",manikanta.following)
print("Username:",manikanta.username)

#private var-accessing
print("\nPassword :",manikanta.showPassword())
print("updated password:",manikanta.updatePassword("mani@12"))
'''

class Login:
    def __init__(self,username,paasword):
        self.username=username
        self.__password=password


  

