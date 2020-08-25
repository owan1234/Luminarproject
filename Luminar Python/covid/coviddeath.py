f=open("covid_19_india.csv","r")
dict={}
death=list()
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    Death=data[7]
    if(state not in dict):
        dict[state]=Death
    else:
        dict[state]=Death
for v in dict.values():
    death.append(int(v))
for k,v in dict.items():
    if max(death)==int(v):
        print(k,"has Highest rate of death:",v)
        exit()

#print which state has highest death
#print which state has highest case
#calculate total number of confirmed
#calculate total no death death in india