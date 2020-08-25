f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    rate=data[3]
    if(rate not in dict):
        dict[rate]=1
    else:
        dict[rate]+=1
for k,v in sorted(dict.items()):
    if k=="":
        pass
    else:
        print("Rate:",k,"No of Movie:",v)
