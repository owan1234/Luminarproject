def fact(num):
    if num==0:
        return 1
    else:
        fact=1
        for i in range(1,(num+1)):
            fact*=i
    return fact

num=int(input("enter number"))
print(fact(num))