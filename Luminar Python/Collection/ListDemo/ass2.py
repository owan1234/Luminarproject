lst=[1,2,3,4,5]
element=int(input("Enter value"))
lst.sort()
low=0
upp=len(lst)-1
while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==element):
        print("pair",lst[low],",",lst[upp])
        break
    elif(data>element):
        upp-=1
    else:
        low-=1