#.............................DICTIONARY.........................
dic={
    "name": "akash",
    "age": 20,
    "marks": [89,98,99],
    
    
}
null_dic={}
null_dic["name"]="thakur"
print(null_dic)
dic["name"]="kavay"# overflow
dic["name"]=23
dic["surname"]="akashgupta"
print(dic["name"])
print(dic)

#.............................NESTED DICTIONARY.........................
student={
    "name":"akash",
    "score":{
        "chem":98,
        "phy":97,
        "math":95
    }
}
print(student["score"]["math"])
print(student)


#.............................DICTIONARY METHODS.........................
student={
    "name":"akash",
    "score":{
        "chem":98,
        "phy":97,
        "math":95
    }
}
print(len(student))
print(len(list(student.keys())))
print(student.keys())
print(list(student.keys()))



student={
    "name":"akash",
    "score":{
        "chem":98,
        "phy":97,
        "math":95
    }
}
print(student.values())
print(list(student.values()))


student={
    "name":"akash",
    "score":{
        "chem":98,
        "phy":97,
        "math":95
    }
}
pairs=list(student.items())
print(pairs[0])
print(student.items())
print(list(student.items()))

student={
    "name":"akash",
    "score":{
        "chem":98,
        "phy":97,
        "math":95
    }
}
#print(student["name"])
print(student.get("name"))


student={
    "name":"akash",
    "score":{
        "chem":98,
        "phy":97,
        "math":95
    }
}
#new_dict={"city":"delhi","age":16}
#student.update(new_dict)
#print(student)

student.update({"city": "delhi"})
print(student)