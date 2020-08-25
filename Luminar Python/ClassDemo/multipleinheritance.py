class Parent:
    def m1(self):
        print("Inside Parent")
class Child:
    def m2(self):
        print("Inside Child")
class SubChild(Child,Parent):
    def m3(self):
        print("Inside subchild")
print("SubChild")
SC=SubChild()
SC.m1()
SC.m2()
SC.m3()
print("Child")
C=Child()
#C.m1()#error
C.m2()
#C.m3()#error
print("Parent")
p=Parent()
#p.m2()#error
p.m1()
#p.m3()#error