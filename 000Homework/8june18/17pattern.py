k=1
for i in range(5,0,-1):
    for j in range(1,k+1):
        if(j%2==0):
            print("0",end="")
        else:
            print("1", end="")
    k=k+1
    print()