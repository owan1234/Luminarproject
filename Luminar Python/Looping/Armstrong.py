num=int(input("Enter the number:"))
temp1=num
sum=0
temp=0
while(num!=0):
    temp=num%10
    sum=sum+temp**3
    num=num//10
if (temp1==sum):
    print("Armstrong")
else:
    print("Not Armstrong")