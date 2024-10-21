#............................dunder function..............
print("...................................__add__.....................")
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,num2):
        newReal=self.real+ num2.real
        newImg=self.img+ num2.img
        return complex(newReal,newImg)
        
num1=complex (1,3)
num1.showNumber()

        
num2=complex (4,6)
num2.showNumber()

#num1=num1.add(num2)
num3=num1+num2
num3.showNumber()

print("....................................__sub__.......................")
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return complex(newReal,newImg)
        
num1=complex (1,3)
num1.showNumber()

        
num2=complex (4,6)
num2.showNumber()

num3=num1-num2
num3.showNumber()
print("....................................multi..................................")
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __mul__(self,num2):
        newReal=self.real*num2.real
        newImg=self.img*num2.img
        return complex(newReal,newImg)
        
num1=complex (1,3)
num1.showNumber()

        
num2=complex (4,6)
num2.showNumber()

num3=num1*num2
num3.showNumber()
print("......................................divi.......................")
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __truediv__(self,num2):
        newReal=self.real/num2.real
        newImg=self.img/num2.img
        return complex(newReal,newImg)
        
num1=complex (1,3)
num1.showNumber()

        
num2=complex (4,6)
num2.showNumber()

num3=num1/num2
num3.showNumber()
print(".....................................percentege(moddulo).......................")
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __mod__(self,num2):
        newReal=self.real%num2.real
        newImg=self.img%num2.img
        return complex(newReal,newImg)
        
num1=complex (1,3)
num1.showNumber()

        
num2=complex (4,6)
num2.showNumber()

num3=num1%num2
num3.showNumber()