num1=int(input("enter value 1"))
num2=int(input("enter value 2"))
num3=int(input("enter value 3"))
if (num1>num2)&(num1>num3):
    print("Max:",num1)
elif (num2>num1)&(num2>num3):
    print("Max:",num2)
elif num1==num2==num3:
    print("All are equal")
else:
    print("Max:",num3)