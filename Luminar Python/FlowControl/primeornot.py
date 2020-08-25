num=int(input("Enter number"))
for i in range(2,num//2):
    if num%i==0:
        print("Not prime")
        exit()
print("Prime")
#10 50 10 to 50