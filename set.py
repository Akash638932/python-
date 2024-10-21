'''
#.............................SET.........................
collection={1,2,3,2,2,2,"hello","world","world"}# dovalicate value ignore
print(collection)
print(len(collection))# total number of items

collection=set()# empty set: syntax
print(type(collection))
'''

#.............................SET METHODS.........................
collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("Akash")
collection.add((1,2,3,4))
print(collection)


collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(2)
collection.remove(3)
print(collection)


collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("Akash")
collection.add((1,2,3,4))
collection.clear()
print(len(collection))
print(collection)


collection={"hello","Akashgupta","world","coding","python"}
print(collection.pop())
print(collection.pop())


set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1)
print(set2)



set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))
