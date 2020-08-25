num=int(input("Enter the number:"))
sum=0
temp=0
while(num!=0):
    temp=num%10
    sum=sum*10+temp
    num=num//10
print("Reversed:",sum)


