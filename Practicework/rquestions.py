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
'''

def countnumbers(n):
    if n<10:
        return 1
    return 1 + countnumbers(n//10)
n = int(input("enter the numbers:"))
print("count the numbers:",countnumbers(n))