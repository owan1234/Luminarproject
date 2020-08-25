f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    Death=data[8]
    if(state not in dict):
        dict[state]=Death
    else:
        dict[state]=Death
for k,v in dict.items():
    print("State:",k,"     Cases:",v)

