f=open("words","r")
dict={}
for line in f:
    words=line.rstrip("\n").split(" ")
    if (words not in dict):
        dict[words]=1
    else:
        dict[words]+=1
for k,v in dict.items():


