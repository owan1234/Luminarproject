num1=int(input("Enter value 1"))
num2=int(input("Enter value 2"))
num3=int(input("Enter value 3"))
if (num1>num2)&(num1>num3):
    if(num2>num3):
        print("Second largest:",num2)
    else:
        print("Second largest:", num3)
elif (num2>num1)&(num2>num3):
    if (num1 > num3):
        print("Second largest:", num1)
    else:
        print("Second largest:", num3)
elif num1==num2==num3:
    print("All are equal")
else:
    if (num2 > num1):
        print("Second largest:", num2)
    else:
        print("Second largest:", num1)