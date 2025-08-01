'''
def reverse(s,ind):
    if ind==len(s):
        return
    reverse(s,ind+1)
    print(s[ind],end = ' ')
    
s = input("enter the string:")
reverse(s,0)
'''

def sumofdigits(n):
    if n == 0:
        return 0
    return n % 10 + sumofdigits(n//10)

n = int(input("enter the number:"))
print("sum of digits is:", sumofdigits(n))