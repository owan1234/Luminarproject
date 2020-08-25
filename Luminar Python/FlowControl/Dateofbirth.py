year1=int(input("Enter Current year"))
month1=int(input("Enter Current month"))
day1=int(input("Enter Current day"))
year2=int(input("Enter birth year"))
month2=int(input("Enter birth month"))
day2=int(input("Enter birth day"))
if(year1>year2):
    actualage=year1-year2
    if(month1<month2):
        actualage-=1
    elif (month1==month2):
        if(day1<day2):
            actualage-=1
elif (year1<year2):
    print("Invalid Birth Year")
    exit()
else:
    print("Age is zero")
    exit()
print("Age is",actualage)



