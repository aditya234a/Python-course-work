a=set ()
print(a)

#  3. Operations on Sets

#  a. Membership Testing

set = {1,23,4,5,60,76,89}
set1 = {2,3,4,54,6,78,8}
print(4 in set)
print(3 in set )
print(4 not in set1)
print(54 in set1)

#  b. Union (| or union() method)

set = {2,3,76,8,4,5,89,78}
set1 = {3,4,67,80,76,36,76}
print(set | set1)

#  c. Intersection (& or intersection() method)

set = {45,67,8,9,32,34,54}
set1 = {67,8,9,67,33,43}                  # it can print with common elements
print(set & set1)

#  d. Difference (- or difference() method)

set = {1,2,3,4,5,7}
set1 = {2,3,1,4,6}
print(set - set1)

#  e. Symmetric Difference (^ or symmetric_difference() method)

set = {1,2,3,4,5,6,7}
set1 = {8,7,6,5,4,3,2}                    # is that remove common elements and we print remaining elements
print(set ^ set1)

#  f. Subset (<= or issubset() method)

set = {1,2}
set1  = {1,2,3}
set2 = {2,3,1}
set3 = {3,1,2}
print(set<=set1)
print(set<=set2)
print(set<=set3)