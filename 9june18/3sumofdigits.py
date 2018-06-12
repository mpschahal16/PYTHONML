a=int(input("Enter the no :"))
sum=0
while(a!=0):
    print("Value of a:",a)
    r=a%10
    print("Value of r:", r)
    sum=sum+r
    print("Value of sum:", sum)
    a=a//10
    print()
print("Sum of digits :",sum)


'''
O/P

Enter the no :153
Value of a: 153
Value of r: 3
Value of sum: 3

Value of a: 15
Value of r: 5
Value of sum: 8

Value of a: 1
Value of r: 1
Value of sum: 9

Sum of digits : 9
'''