num1=int(input("Enter value 1"))
num2=int(input("Enter value 2"))
num3=int(input("Enter value 3"))
if (num1>=num2)&(num1>=num3):

    if(num2>num3):
        print("Sorted Order:",num1,num2,num3)
    else:
        print("Sorted Order:", num1, num3, num2)
elif (num2>=num1)&(num2>=num3):
    if (num1 > num3):
        print("Sorted Order:", num2, num1, num3)
    else:
        print("Sorted Order:", num2, num3, num1)
elif num1==num2==num3:
    print("All are equal")
else:
    if (num2 > num1):
        print("Sorted Order:", num3, num2, num1)
    else:
        print("Sorted Order:", num3, num1, num2)