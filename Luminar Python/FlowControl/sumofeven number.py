low=int(input("Enter lower limit"))
high=int(input("enter high limit"))
sumodd=0
sumeven=0
for i in range(low,high+1):
    if i%2==0:
        sumodd+=i
    else:
        sumeven+=i
print("sum of even:",sumodd)
print("sum of odd:",sumeven)