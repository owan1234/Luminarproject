class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def printvalue(self):
        print(self.id)
        print(self.name)
        print(self.sal)
    def __str__(self):
        return self.name
obj=Employee(1011,"Ajay",25000)
print(obj)