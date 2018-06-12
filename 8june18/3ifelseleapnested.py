#nested if else
year=(int)(input("Enter the year :"))
if(year%100==0):
    if(year%400==0):
        print(year, ": is leap year")
    else:   
        print(year, "is not a leap year")
else:
    if (year % 4 == 0):
        print(year, ": is leap year")
    else:
        print(year, "is not a leap year")



'''
#O/P
Enter the year :1700
1700 is not a leap year
'''