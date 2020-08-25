#Parent Super Base
#Child  Sub   Derived

class Parent:
    def phone(self):
        print("Have Samsung galaxy A6")
class Child(Parent):
    pass
class SubChild:
    def M3(self):
        print("Inside subchild")
c=Child()
c.phone()