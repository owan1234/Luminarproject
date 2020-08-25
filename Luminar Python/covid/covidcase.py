f=open("covid_19_india.csv","r")
dict={}
case=list()
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    Death=data[8]
    if(state not in dict):
        dict[state]=Death
    else:
        dict[state]=Death
for v in dict.values():
    case.append(int(v))
for k,v in dict.items():
    if max(case)==int(v):
        print(k,"has Highest rate of Case:",v)
        exit()