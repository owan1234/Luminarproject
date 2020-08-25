import datetime
class Person:
    def Setvalue(self, pname,age):
        self.age=age
        self.pname=pname
    def printvalue(self):
        print(self.pname)
        print(self.age)
class Bank(Person):
    Bname="SBI"
    def __init__(self,accno):
        self.accno=accno
        self.balance=3000
    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print("Your", self.accno, "has been Debited with", amount, "on", datetime.date.today())
    def printacc(self):
        print("Name",self.pname)
        print("Age",self.age)
        print("Bank Name",Bname)
        self.balance()
    def deposit(self,amount):
        self.balance+=amount
        print("Your",self.accno, "has been Criedited with",amount,"on",datetime.date.today())
    def balance(self):
        print("Your available balance is",int(self.balance))
obj=Bank(1001)
obj.Setvalue("Ajay",25)
obj.deposit(5000)
obj.withdraw(1000)
obj.printacc()
obj.balance()