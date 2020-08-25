f=open("Tempdata","r")
dict={}
for lines in f:
    words,temp = lines.rstrip("\n").split(",")
    if words not in dict:
        dict[words]=temp
    else:
        if dict[words]<temp:
            dict[words]=temp
for k,v in dict.items():
    print("Max temp of",k,"is",v)