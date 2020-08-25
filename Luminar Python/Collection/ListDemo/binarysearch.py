num1=int(input("enter the no element"))
lst=list()
for i in range(0,num1):
    lst[i]=int(input())
lst.sort()
print(lst)
low=0
upp=len(lst)-1
element=int(input("enter element to search"))
flag=0
while(low<=upper):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        high=mid-1
    elif(element==lst[mid]):
        flag+=1
if flag>0:
    print("Element found")
else:
    print("Element not found")
