#7.2.Dictionary.py

dic={}
print(dict())
print(dic)
d={'name':'mani', 'age':20, 'course':'DA', 'batchno':14}
print("Dictionary{} : ", d)
print("Accessing : ", d['age'])
print("Accessing : ", d.get('name'))
#print("Accessing : ", d['exams'])
#print("Accessing : ", d.get('exams'))
print("Accessing : ", d.get('exams', 3))
print("Dictionary{} : ", d)
d['name']='manikanta'
print("update : ", d)
d['city']='Draksharamam'
print("Adding : ", d)
print("Dictionary{} : ", d)

d.popitem()
print("Remove : ", d)
d.pop("age")
print("Remove : ", d)
d['city']='Draksharamam'
print("Adding : ", d)
print("Dictionary{} : ", d)

del d['batchno']
print("Dictionary{del} : ", d)

#d.clear()
#print("Dictionary{clear} : ", d)

#del d
#print("Dictionary{del} : ", d)


#Dictionary Built-in Methods 
print("Dictionary{} : ", d)
print("default : ", d.get('age', 'attach'))
print("Dictionary{} : ", d)
print("Keys() : ", d.keys())
print("Values() : ", d.values())
print("Items() : ", d.items())

print("len() : ", len(d))
print("sort() : ", sorted(d))
print("max() : ", max(d))
print("min() : ", min(d))

#Nested Dictionary
mem={
    1:10, 2:30, 'name':'aditya', 'age':22,
    1:90, 3:69, 'name':'aid', 'city':'kakinada'
}
print("NestedDictionary : ", mem)
print(len(mem))