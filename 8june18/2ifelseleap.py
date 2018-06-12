#leap year basic
year=(int)(input("Enter the year :"))
if(year%4==0):##if(boolean true or false) true next step false jump to else
    print(year, ": is leap year")
else:
    print(year, "is not a leap year")



'''
O/P

Enter the year :1700
1700 : is leap year
'''