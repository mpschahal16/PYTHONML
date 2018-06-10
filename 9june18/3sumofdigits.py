a=int(input("Enter the no :"))
sum=0
while(a!=0):
    r=a%10
    sum=sum+r
    a=a//10
print("Sum of digits :",sum)