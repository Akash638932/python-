#........................................STRINGS...................................
str1='this is a strings'
str2="this is a string"
str3="""this is a string"""
print(str1)
print(str2)
print(str3)

str1="this is a strings .\n we are creating it in python."
str2="this is a strings .\t we are creating it in python."
print(str1)
print(str2)

#........................................CONCATENATION...................................
str1="akash"
str2="gupta"
final_str=str1+str2
print(final_str)

#........................................LENGTH OF STR...................................
str1="akash"
len1=len(str1)
print(len1)

str2="gupta"
len2=len(str2)
print(len2)

final_str=str1+"  "+str2
print(final_str)
print(len(final_str))

num1="akashguptakamalapuri"
print(num1)
print(len(num1))

#........................................INDEXING...................................

str="Akash_gupta"
#chr=str
print(str[3])
#print(chr[2])
print(str[-3])

#........................................SLICING...................................
str="akash gupta"
print(str[1:4])
print(str[0:4])
print(str[6:12])
print(str[5:len(str)])#last index
print(str[5:])#last index
print(str[:4])# first
print(str[5:])#last

#........................................SLICING NEGATIVE INDEX............................
str="apple"
print(str[-3:-1])
print(str[-5:-2])

#........................................SLICING  FUNCTIONS............................
str="I am studying python from appaCollege"
print(str.endswith("ege"))#substr returns true

str="i am studying python from appaCollege"
print(str.capitalize()) #first time 

str="i am studying python from appaCollege"
str=str.capitalize()
print(str)# original string modifice 

str="i am studying python from appaCollege"
print(str.replace("o","a"))
print(str.replace("python","javascrip"))

str="i am  from studying python from appaCollege"
print(str.find("o"))
print(str.find("from"))

str="i am  from studying python from appaCollege"
print(str.count("from"))
#str.


