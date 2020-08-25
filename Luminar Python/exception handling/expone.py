num1=int(input("enter value For Num1"))
num2=int(input("Enter Value for Num2 "))
try:
    res=num1/num2
    print("Result",res)
except Exception as e:
    print(e.args)