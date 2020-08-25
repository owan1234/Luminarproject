lst=[1,2,3,4,5,6,7,8,9,10,11,12]
element=int(input("Enter element to search"))
for i in lst:
    if element==i:
        print("Found")
        exit()
print("Not Found")