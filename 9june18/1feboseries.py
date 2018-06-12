a=0
b=1
sum=a+b
num=int(input("Enter the Last tesrm range :"))
print(a,"\t",b,end="\t")
while(sum<=num):
    print(sum,end="\t")
    a=b
    b=sum
    sum=a+b


'''
O/P

Enter the Last tesrm range :6
0 	 1	1	2	3	5	
'''
