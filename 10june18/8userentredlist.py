# program to take input from user and store it in in the list

a=(int)(input("Enter the range :"))
temp=[]
for i in range(1,a):
    b=(int)(input("Enter no :"))
    temp.append(b)
print(temp)




'''
O/p

Enter the range :5
Enter no :1
Enter no :6
Enter no :6
Enter no :5
[1, 6, 6, 5]


'''