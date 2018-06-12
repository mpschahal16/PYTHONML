#this program counts the occursnce of any digit in entered no
num=int(input("Enter the no :"))
d=int(input("Enter the digit to count :"))
c=0
while(num!=0):
    r=num%10
    print("Value of r :",r)           ##print command to better understand logic
    num=num//10
    print("Value of num :",num)          ##print command to better understand logic
    if(d==r):
        c=c+1
        print("Value of c :",c)        ##print command to better understand logic
    print()
print(d,"Exist ",c,"times in number")


'''
O/P

Enter the no :1555
Enter the digit to count :5
Value of r : 5
Value of num : 155
Value of c : 1

Value of r : 5
Value of num : 15
Value of c : 2

Value of r : 5
Value of num : 1
Value of c : 3

Value of r : 1
Value of num : 0

5 Exist  3 times in number
'''