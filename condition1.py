#................................condition statement.......................
age=21
if(age>=22):
    print("can vate & apply for license")
    
    
age=24
if(age>=22):
    print("can vote")# SPACE INDENTATION
    print("can drive")
    
    
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
print("end of code")


age=14
if(age>=18):
    print("can vote")
else:
    print("cannot vote")
#................................ IF condition statement.......................
num=5
if(num>2):
    print("greater than 2")
if(num>3):
    print("greater than 3")
#................................ELIF condition statement.......................   
    num=5
if(num>2):
    print("greater than 2")# false
elif(num>3):
    print("greater than 3")# chack
#................................ELSE condition statement.......................  
light="pink"
if(light=="red"):#false
    print("stop")
elif(light=="green"):#false
    print("go")
elif(light=="yellow"):#false
    print("look")
else:
    print("light is broken")#print
print("end of code")
