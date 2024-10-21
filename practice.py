#................................CONDITION SATEMENT.......................#
#................................a=5 & g=5.......................#
#................................a=2 & g=f.......................#
A=int(input("A:"))
G=input("M/F:")
if((A==1 or A==2)and G== "m"):
    print("fee is 100")
elif(A==3 or A == 4 or G =="F"):
    print("fee is 200")
elif(A==5 and G =="M"):
    print("fee is 300")
else:
    print("no fees")
    
#............................. SINGLE LINE IF /TERNARY OPERATER..........................#
food= input("food:")
eat="yes"if food =="cake" else "no"
print("eat")

#............................. SINGLE LINE IF /TERNARY OPERATER..........................#
food= input("food:")
print=("sweet")if food =="cake"or food =="jalebi"else print("not sweet")


#............................. CLEVER IF /TERNARY OPERATER..........................#
age=int(input("age:"))
vate=("yes","no") [age>=18]

#............................. CLEVER IF /TERNARY OPERATER..........................#
sal=float(input("salary:"))
tax=sal*(0.1,0.2)[sal<=5000000]
print(tax)

#............................. CALCULATE SIMPLE INTEREST..........................#
num1=float(input("a:"))
num2=float(input("b:"))
num3=float(input("c:"))
print(num1*num2*num3/100)


#.............................improved..........................#
p=float(input("p:"))
r=float(input("r:"))
t=float(input("t:"))
si=(p*r*t/100)
print(si)

