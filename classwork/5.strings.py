
# 1.OperationsOnStrings

s1='Aditya '
s2='Mandala'
print("Concatenation(+) : ", s1 + s2)             # Concatenation(+) : Aditya Mandala
print("Repetition() : ", s1*4)                    # Repetition() :    Aditya Aditya Aditya Aditya 
print("Repetition() : ", s2*4)                    # Repetition() :  MandalaMandalaMandalaMandala
print("Indexing : ", s1[0])                       # Indexing :  A
print("Indexing : ", s1[1])                       # Indexing :  d
print("Indexing : ", s1[2])                       # Indexing :  i
print("Indexing : ", s1[3])                       # Indexing :  t
print("Indexing : ", s1[4])                       # Indexing :  y
print("Indexing : ", s1[5])                       # Indexing :  a
print("Indexing : ", s1[6])                       # Indexing :  
                

s="Iam Aditya Icompleted BTech in 2025 at KIET"
print("Membership : ", "completed" in s)                 # Membership :  True
print("Membership : ", "2025" in s)                      # Membership :  True
print("Membership : ", "Aditya" not in s)                # Membership :  True
print("Membership : ", "mandala" in s)                   # Membership :  False


# 2.Built-in String Functions

#1. len() - Returns the length of the string.
#2. max() / min() - Returns the maximum or minimum character (based on ASCII values).
#3. sorted() - Returns a sorted list of characters.
#4. chr() / ord() - Converts between characters and their ASCII codes


m='Looking beautiful'
print("length : ",len(m))           #length :  17
print("max : ", max(m))             #max :  u
print("min : ", min(m))             #min :   
print("sorted : ", sorted(m))       #sorted :  [' ', 'L', 'a', 'b', 'e', 'f', 'g', 'i', 'i', 'k', 'l', 'n', 'o', 'o', 't', 'u', 'u']
print("character : ", chr(97))      #character :  a
print("Order : ", ord(' '))         #Order :  32

# String Methods

# 1.Case Conversion Methods

#1.upper()
#2.lower()
#3.capitalize()
#4.title()
#5.swapcase()
#6.casefold()

c='''i can improve mY SELF'''
print("upper('A') : ", c.upper())                  #upper() :  I CAN IMPROVE MY SELF
print("lower('a') : ", c.lower())                  #lower() :  i can improve my self
print("capitalize(Ab cd) : ", c.capitalize())      #capitalize() :  I can improve my self
print("title(Ab Cd) : ", c.title())                #title() :  I Can Improve My Self
print("swapcase(A-a, a-A) : ")                     #swapcase() :  I CAN IMPROVE My self

# 3.Search & Find Methods

f="adityaMandala"
print("find : ", f.find('a'))           #find :  0
print("rfind : ", f.rfind('a'))         #rfind :  12
print("find : ", f.find('x'))           #find :  -1

#print("index : ", f.index('x'))        #error

print("index : ", f.index('d'))         #index :  1
print("rindex : ", f.rindex('d'))       #rindex :  9
print("count : ", f.count('a'))         #count :  5

#4.String Tesing Mothods (Boolean Results )

g='Manikanta12324'
print("startswith(sub) : ", f.startswith('d'))          #startswith(sub) :  False
print("startswith(sub) : ", f.startswith('a'))          #startswith(sub) :  True
print("endswith(sub) : ", f.endswith('d'))              #endswith(sub) :  False
print("endswith(sub) : ", f.endswith('a'))              #endswith(sub) :  True
print("isspace : ", f.isspace())                        #isspace :  False
print("isalpha : ", f.isalpha())                        #isalpha :  True
print("isalpha : ", g.isalpha())                        #isalpha :  False
print("isalnum : ", g.isalnum())                        #isalnum :  True
print("isupper : ", f.isupper())                        #isupper :  False
print("islower : ", f.islower())                        #islower :  False
print("istitle : ", f.istitle())                        #istitle :  False
print("isidentifier : ", f.isidentifier())              #isidentifier :  True
print("istitle : ", g.istitle())                        #istitle :  True

print("         isdecimal()  ")
print("isdecimal() : ", '123'.isdecimal())            #isdecimal() :  True
print("isdecimal() : ", '123.67'.isdecimal())         #isdecimal() :  False
print("isdecimal() : ", '12abc3'.isdecimal())         #isdecimal() :  False
print("isdecimal() : ", 'Ⅷ'.isdecimal())            #isdecimal() :  False
print("isdecimal() : ", '٣'.isdecimal())              #isdecimal() :  True
print("isdecimal() : ", '²'.isdecimal())              #isdecimal() :  False
print("isdecimal() : ", '⅓'.isdecimal())              #isdecimal() :  False
print("isdecimal() : ", '五'.isdecimal())             #isdecimal() :  False

print("         isdigit()  ")
print("isdigit() : ", '123'.isdigit())              #isdigit() :  True
print("isdigit() : ", '123.67'.isdigit())           #isdigit() :  False
print("isdigit() : ", '12abc3'.isdigit())           #isdigit() :  False
print("isdigit() : ", 'Ⅷ'.isdigit())              #isdigit() :  False
print("isdigit() : ", '٣'.isdigit())                #isdigit() :  True
print("isdigit() : ", '²'.isdigit())                #isdigit() :  True
print("isdigit() : ", '⅓'.isdigit())                #isdigit() :  False
print("isdigit() : ", '五'.isdigit())               #isdigit() :  False

print("         isnumeric()  ")
print("isnumeric() : ", '123'.isnumeric())          #isnumeric() :  True
print("isnumeric() : ", '123.67'.isnumeric())       #isnumeric() :  False
print("isnumeric() : ", '12abc3'.isnumeric())       #isnumeric() :  False
print("isnumeric() : ", 'Ⅷ'.isnumeric())          #isnumeric() :  True
print("isnumeric() : ", '٣'.isnumeric())            #isnumeric() :  True
print("isnumeric() : ", '²'.isnumeric())            #isnumeric() :  True
print("isnumeric() : ", '⅓'.isnumeric())            #isnumeric() :  True
print("isnumeric() : ", '五'.isnumeric())           #isnumeric() :  True

#5.Replace & Modify Methods

print("replace(old,new) : ", f.replace('a', '@'))
print("replace(old,new) : ", f.replace('ad', '@%'))
print("maketrans() : ", f.maketrans('a', '@'))
print(ord('a'))
print(ord('@'))
print("translate(table) : ", f.translate('str'.maketrans('a', '@')))
print("translate(table) : ", f.translate('str'.maketrans('ad','@%')))