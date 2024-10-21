#.........................integer.........................#
age=int(input("Enter the number of integer:"))
print(age)
print(type(age))

#.......................float.............................#
price=float(input("Enter the number of float:"))
print(price)
print(type(price))

#........................string..........................#
name=str(input("Enter the number of string:"))
print(name)
print(type(name))
#............................Dictionary..................#
dict={ 
        "name":"Akash",
        "cgpa":"7.5678",
        "marks":"234987",

}
print(dict['name'])
dict["name"],dict["cgpa"],dict["marks"]
#dict["key"]="value"

#..................................boolean....................#

num1=True
num2=False
print(num2)
print(type(num1))

#................................tuple.......................#
tup=(3,45,6678,89,23,45,67,89,0,9,34,23,56,34,56,67,89,8)
print(type(tup))

#................................set.......................#
set={12,4,45,56,78,90,78,778,45,67,68,56,67,667,67,89,}
print(type(set))

#................................list.......................#
list=[45,5,67,67,78,45,7,78,90,56,78,89,34,67,56,78,90]
print(type(list))
