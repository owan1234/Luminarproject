f=open("movies.csv","r")
dict={}
count=list()
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
for value in sorted(dict.values()):
    count.append(value)
a=int(max(count))
for k,v in dict.items():
    if a==v:
        print("Max No of movies is",k,"in",v)
