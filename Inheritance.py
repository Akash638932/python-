print("....................................inheritance.............................")
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started...........")
        
    @staticmethod
    def stop():
        print("car stopped")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        
        
car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")

#print(car1.name)
print(car1.start())


print("..........................................single inheritan...................")
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started...........")
        
    @staticmethod
    def stop():
        print("car stopped")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        
        
car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")

#print(car1.name)
print(car1.start())

print(".....................................multi-level Inheritance...........................")
class Car:
    @staticmethod
    def start():
        print("car started...........")
        
    @staticmethod
    def stop():
        print("car stopped")
        
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
        
        
class Fortuner(ToyotaCar):
    def __iniit__(self,type):
        self.type=type
        
car1=Fortuner("diesel")
car1.start()
print("...........................................multiple Inheritance......................")
class A:
    vara="welcome to class A"
    
class B:
    varb="welcome to class B"

class c(A,B):
    varc="welcome to class C"
    
    
c1=c( )

print(c1.varc)
print(c1.varb)
print(c1.vara)
    

    

