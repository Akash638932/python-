#................................condition statement.......................#
#................................Traffic light code.......................#
light=input(" The traffic light :")
if(light=="red"):
    print("stop")
elif(light== "yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")
    
#...............................Grade of student........................#
marks=int(input("Enter of grade of student Marks:"))
if(marks >= 90):
  grade="A"
elif(marks >= 80 and marks <90):
  grade="b"
elif(marks>=70 and marks <80):
  grade="c"
else:
  grade="d"
print("grade of the student",grade)
    

#................................NESTING condition statement.......................  
age=34
if(age>=18):
    if(age>=80):
      print("cannot drive")
    else:
      print("can drive")
else:
  print("cannot drive")