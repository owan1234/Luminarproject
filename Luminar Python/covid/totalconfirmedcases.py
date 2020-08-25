f=open("covid_19_india.csv","r")
dict={}
sum=0
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    case=data[8]
    if(state not in dict):
        dict[state]=case
    else:
        dict[state]=case
for v in dict.values():
    sum=sum+int(v)
print("Total No of Confirmed Cases:",sum)