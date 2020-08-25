lst=[1,2,3,4,5,6]
element=int(input("Enter element"))
for i in lst:
    for j in lst:
        if (i+j==element):
            print("Elements are",i,j)
#[2,4,6]   [10,8,6]
#[3,5,8]   [13,11,8]