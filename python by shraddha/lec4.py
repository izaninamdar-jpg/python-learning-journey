#dictionaries
"""info = {
    'key' : 'value',
    'name' :  'apnacollege',
    'learning' : 'python',
    15 : 343.545
}
print(info[15])
info['key'] = 'keeyee'
info['name']= 'izan'
info['learning'] = 434
print(info)
info["surname"]= 'inamdar'
print(info)
empty = {}
print(empty)
empty["name"]= 'apnacollege'
print(empty)"""
#nested dictionaries 
student = {
    'name' : 'izan ',
    'subjects': {
         'phy' : 43,
         'chem' : 88,
          'math' : 89 },
    'phone no' : 909904565,
    +91 : 'india'
}
"""#print(student)
#print(student["subjects"])
#print(student ["subjects"] ['chem'])
print(student.keys())
print(list(student.keys())) #typecasting eg float(9)
ab = (list(student.keys())) 
print(len(list(student.keys())))
print(len(ab))
print(student.values()
print(list(student.values()))
print(student.items())
print(list(student.items()))
pairs = list(student.items()) 
print(pairs[0])
print(pairs[1])

student.update({'delhi':'city'})
#another method
new_dict ={ 'city':'delhi'}
student.update(new_dict)
print(student)

#sets in python 
collection = {1,2,3,5,'hello','hello','hello',4}
print(collection)
print(type(collection))
print(len(collection))
collection1 = set () # for empty set creation
print(type(collection1))
collection = set()
collection.add(1)
collection.add(2)
collection.add(8)
collection.add(5)
collection.remove(2) #if values doesnt exist in set ERROR 
collection.pop()
print(collection)
collection.pop()
print(collection)
collection.clear()
print(len(collection))
"""
collection = set()
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

print(set1.union(set2))
print(set1.intersection(set2))

