#list compare built in function
a=[1,2,3]
b=[1,2,3]

if(a.__len__()==b.__len__()):
    for i in range(1,a.__len__()):
        if(a[i]!=b[i]):
            ct=1
        else:
            ct=0
    if(ct==0):
        print("Equal")
    else:
        print("Not Equal")
else:
    print("Not equal")

