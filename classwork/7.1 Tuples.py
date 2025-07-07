# 1. Accessing Tuple Elements 

#  a. Indexing

tuple = ("kiran","aditya","mani","eswar")
print(tuple[3])                                                 # Syntax: tuple[index]

#  b. Negative Indexing

tuple = (10,20,40,50,70)
print(tuple[-1])
print(tuple[-3])

#  c. Slicing

tuple = (10,20,40,60,79,56)
print(tuple[1:3])
print(tuple[-1:-3])
print(tuple[:-1])

# 2. Operations on Tuples

#  a. Concatenation

tuple1 = (90,78)
tuple2 = (57,37)
print(tuple1 + tuple2)                         #  Combine two or more tuples using the + operator

#  b. Repetition

tuple1 = (57, 78)
tuple2 = (9,5,7,8)
tuple3 = (7,4,3,9)
print(tuple1 * 3)                              #   Repeat the elements of a tuple using the * operator
print(tuple2 * 7)
print(tuple3 * 3)

#  c. Membership Testing

tuple = (2,5,7,89,67,98,65,45)
print(5 in tuple)
print( 89 in tuple)                            # Check if an element is present in the tuple using the in or not in keywords
print(78  in tuple)
print(97 not in tuple)

#  d. Tuple Unpacking

my_tuple = (1, "apple", 3.5)
a, b, c = my_tuple 

#  3.Tuple Methods

tuple = (2,4,56,4,4,4,8,9,6,7,6,5,3,2,3,2,4,5)
print(tuple.count(2))                              
print(tuple.count(4))                   #  Counts the number of occurrences of x in the tuple
print(tuple[5])                         #  Returns the first index of x in the tuple 
print(tuple.index(2))

#  4. Built-in Functions for Tuples

tuple1 = [2,3,4,5,6,7,8,9,7,6,5,4,3]

print(len(tuple))
print(max(tuple))
print(min(tuple))
print(sum(tuple))

#  5. Immutability and Tuple Behavior
nested_tuple1 = (1, [2,3])
nested_tuple2 = (1, [2,3])

nested_tuple1 [1][0] = 100
nested_tuple2[1].append(100)
print(nested_tuple1)
print(nested_tuple2)

