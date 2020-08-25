Low=int(input("Enter low number"))
High=int(input("Enter high number"))
for j in range(Low,High+1):
    flag=0
    for i in range(2,(j//2)+1):
        if j%i==0:
            flag+=1
            break
    if flag==0:
        print(j)
