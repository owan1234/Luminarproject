f=open("covid_19_india.csv","r")
dict={}
sum=0
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    if(state not in dict):
        dict[state]=death
    else:
        dict[state]=death
for v in dict.values():
    sum=sum+int(v)
print("Total No of Death:",sum)