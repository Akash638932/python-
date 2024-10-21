print(".................................class & object.................")
'''
class Student:
    name="Akash gupta"
    
s1=Student()
print(s1.name)

s2=Student()

print(s2.name)

class Car:
    colur="blue"
    brand="mercedes"
    
car1=Car()
print(Car.colur)
car1=Car()
print(Car.brand)

print("...........................__init__function.......................")
class Student:
    #name="Akash gupta"
    #default constructors
   # def __init__(self):
     #   pass
    # parameterized constructors
    def __init__(self,name,marks):#new object,self
        self.name=name
        self.marks=marks
        print(("adding new student in database.........."))
        
s1=Student("karan",99)
print(s1.name,s1.marks)
    
s2=Student("Akash",100)
print(s2.name,s2.marks)


print(".................................class $ instance Attributes.........................")
class Student:
    college_name="abc college"
    # parameterized constructors
    def __init__(self,name,marks):#new object,self
        self.name=name
        self.marks=marks
        print(("adding new student in database.........."))
        
s1=Student("karan",99)
print(s1.name,s1.marks)
    
s2=Student("Akash",100)
print(s2.name,s2.marks)
print(s2.college_name)


#print("..........................................")
class Student:
    college_name="Abc college"
    name="anonymous"#class attr
    
    def __init__(self,name,marks):
        self.name=name#obj attr> class attr
        self.marks=marks
        print("adding new student in database..........")
        
s1=Student("Akash",99)
print(s1.name)
'''
print(".........................................methods..........................")
class Student:
    college_name="abc college"
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks
        
s1=Student("Akash",99)
s1.welcome()
print(s1.get_marks())