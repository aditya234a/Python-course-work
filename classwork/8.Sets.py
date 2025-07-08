a=set ()
print(a)

#  3. Operations on Sets

#  a. Membership Testing

sets = {1,23,4,5,60,76,89}
set1 = {2,3,4,54,6,78,8}
print(4 in sets)
print(3 in sets )
print(4 not in set1)
print(54 in set1)

#  b. Union (| or union() method)

setas = {2,3,76,8,4,5,89,78}
set1 = {3,4,67,80,76,36,76}
print(setas | set1)

#  c. Intersection (& or intersection() method)

seta = {45,67,8,9,32,34,54}
set1 = {67,8,9,67,33,43}                  # it can print with common elements
print(seta & set1)

#  d. Difference (- or difference() method)

sete = {1,2,3,4,5,7}
set1 = {2,3,1,4,6}
print(sete - set1)

#  e. Symmetric Difference (^ or symmetric_difference() method)

sety = {1,2,3,4,5,6,7}
set1 = {8,7,6,5,4,3,2}                    # is that remove common elements and we print remaining elements
print(sety ^ set1)

#  f. Subset (<= or issubset() method)

setu = {1,2}
set1  = {1,2,3}
set2 = {2,3,1}
set3 = {3,1,2}
print(setu<=set1)
print(setu>=set2)
print(setu<=set3)

#  g. Superset (>= or issuperset() method)

setl = {1,2,3}
set1 = {1,2}
set2 = {2,3}
set3 = {3,2}
print(setl>=set1)
print(setl<=set2)
print(setl>=set3)

#  h. Disjoint Sets (isdisjoint() method)

set1 = {676,87,98}
set2 = {68,90,54}

set3 = {78,23,43}
set4 = {75,23,98}

print(set1.isdisjoint(set2))

print(set3.isdisjoint(set4))

#  4. Built-in Methods for Sets

s = {1,2,3,4,5,6,7,8,9}
s1 = {3,4,5,6,7,8,9}
s2 = {4,5,4,6,7,8,9}

s.add(12)
print(s)

s.remove(5)
print(s)

s.discard(9)
print(s)

s.pop()
print(s)

s.clear()
print(s)

s1.union(s2)
print(s1)

#  5. Built-in Functions for Sets

x = {1,2,3,4,5,6,7}

print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x))

a = [1,2,3,6,7]
print(set(a))

#  6. Immutability and Frozensets

f = frozenset((4,5,6,7,8,9))
print(f)

