#Parent Super Base
#Child  Sub   Derived

class Parent:
    def m1(self):
        print("Inside Parent")
class Child(Parent):
    def m2(self):
        print("Inside Child")
class SubChild(Child):
    def m3(self):
        print("Inside subchild")
#subchild
SC=SubChild()
SC.m1()
SC.m2()
SC.m3()
#child
C=Child()
C.m1()
C.m2()
#C.m3()#error

#parent
p=Parent()
#p.m2()#error
p.m1()
#p.m3()#error