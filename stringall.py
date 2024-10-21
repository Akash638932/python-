#....................................BASIC OPERATIONS...............................
#.......................concatenation....................
num1="hello"+"world"
print(num1)
'''
lenghtnof str
len(str)
'''
#....................................indexing............................
num1="Akash----Gupta"
print(num1[6])
print(num1[1])
print(num1[5])
print(num1[7])


#....................................Slicing................................

str="Akash gupta"
print(str[1:4])
str[:4]#same as str[0:4]
str[1:]#same as str [1:len(str)]

#..............................slicing NEgative index........................
str="Akash"
print(str[-3:-1])

#...............................string function.............................
str="i am coder"
print(str.capitalize())
print(str.replace(2,4))
print(str.find(8))
print(str.count("am"))