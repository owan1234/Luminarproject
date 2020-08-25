num1=input("Enter three Element")
l1=num1.split()
print("Entered List is:",l1)
for i in  range(0,2):
    l1[i]=int(l1[i])+int(l1[2])
for i in range(0,2):
    for j in range(2-i):
        if int(l1[j])<int(l1[j+1]):
            l1[j],l1[j+1]=l1[j+1],l1[j]
print("Output:",l1)

