'''
from functools import reduce

l = ['aditya','mani']
sum_all = reduce (lambda x,y:x+y,l)
print(sum_all)
'''
'''
 #1. Square of a number using lambda

n = int(input())
square = lambda n: n*n
print(square(n))

#2. Check if number is even using lambda

n = int(input())
is_even = lambda n: True if n%2==0 else False
print(is_even(n))

#3. Get maximum of two numbers using lambda
a = int(input())
b = int(input())
max = lambda a,b : a if a>b else b
print(max(a,b))

#4. Multiply two numbers using lambda

a = int(input())
b = int(input())
multiply = lambda a,b: a*b
print(multiply(a,b))


#5. Sort a list of tuples by second element using lambda

n = list(map(int,input().split()))
print(sorted(n, key = lambda i: i[1],reverse = True))

#6. Filter even numbers from a list using lambda and filter()

l = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda i: i%2==0,l)))

#7. Square each element in a list using lambda and map()

l = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda i: i*i,l)))

#8. Convert list of strings to uppercase using lambda

n = ['vikas','aditya','mani']
print(list(map(lambda i:i.upper(),n)))

#9. Sort list of dictionaries by key using lambda

n = [{ 'age': 30}, { 'age': 20}]
s= sorted(n,key = lambda i : i["age"]) 
print(s)

#10. Return length of a string using lambda

n = input()
length = lambda n: len(n)
print(length(n))

#11. Check if string starts with a vowel using lambda

n = input()
vowels = 'aeiouAEIOU'
v = lambda a:True if n[0] in vowels else False
print(v(n))

#12. Add 10 to each element using lambda and map()

n = list(map(int,input().split()))
v = list(map(lambda a: a+10,n))
print(v)
'''

