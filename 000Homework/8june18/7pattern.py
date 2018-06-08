for i in range(1,6):
    k=1
    for j in range (1,6):
        if(j%2==0):
            print(k,end="")
            k=k+1
        else:
            print("*",end="")
    print()