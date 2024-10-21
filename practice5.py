'''
#q1 store following word meanings in a python dictionary:
#Table: "a piece of furniture","list of facts & figures"
#Cat:" a small animal"
dictionary={
    "cat": "a small animal",
    "table": {"a piece of furniture","list of facts & figures"}
    
    
}
print(dictionary)


#q2 You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all Students.
    #"python","java","c++","python","javascript","java","python","java","c++","c".
subject={
    "python","java","c++","python","javascript",
    "java","python","java","c++","c"
    }
print(len(subject))

#q3 wap to enter marks of 3 subjects from the user and store them in a dictionary start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={ }
x=int(input("enter phy:"))
marks.update({"phy":x})

x=int(input("enter chem:"))
marks.update({"chem":x})

x=int(input("enter mathe:"))
marks.update({"mathe":x})

print(marks)

'''
#q4 Figure out a way to store 9 & 9.0 as separate values in the set (You can take help of built-in data types).
#value={9,"9.0"}
#print(value)
value={
    ("float",9.0),
    ("int",9)
}
print(value)