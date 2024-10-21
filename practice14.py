#q1. create Account class with 2 attributes- balance & account no.
#q2. create methods for debit , credit & printing the balance.
class Account:
    def __init__(self,bal,Acc):
        self.balance=bal
        self.Account_no=Acc
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance =",self.get_balance())
        
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance =",self.get_balance())
        
    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
        

