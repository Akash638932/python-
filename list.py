#.................................................LIST..............................................
marks=[94.0,87.5,95.0,66.0,45.1]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])

student=["karan",95.9,17,"Delhi"]
print(student[0])
student[0]="akash"
print(student)

#.................................................LIST SLICING..............................................
marks=[89,95,567,78,99,98,89]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])
print(marks)
#.................................................LIST METHODS..............................................
list=[2,1,3]
list.append(4)
print(list)


list=[2,1,3]
list.sort()
print(list)

list=[2,1,3]
list.sort(reverse=True)
print(list)

list=[2,1,3]
list.reverse()
print(list)

list=[2,1,3]
list.insert(2,45)#2 index ,45 value
print(list)

list=[2,1,3]
list.remove(3)
print(list)

list=[2,1,3]
list.pop(1)#remove index
print(list)
#list.