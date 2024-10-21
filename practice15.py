#q1 Define a Circle class to create a circle with radius  using the constructor.
#Define an Area() method of the class which calculates the area of the circle.
#Define a perimeter()method of the class which allows you to calculate the perimeter of the circle.
class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return (22/7) * self .radius ** 2
    
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
        
        
cl1=Circle(21)
print(cl1.area())
print(cl1.perimeter())




#q2. Define a Eployee class with attributes role, department & salary.this class showDetails()methods.
#Create an Engineer class tha inherits properties from Employee &        attributes: name & age.
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")        
        
engg1=Engineer("Elon musk",48)
engg1.showDetails()

#Q3  create a class called Order which stores item & its price
# Use Dunder function __gt__() to convey that:
# order1> order2 if price of order1 of order2
print("..................................................................")
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1=Order("chips",20)
odr2=Order("tea",15)
print(odr1 > odr2)
    