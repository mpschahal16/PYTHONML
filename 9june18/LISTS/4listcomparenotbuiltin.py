#list compare built in function
a=[1,2,3]
b=[1,2,3]

if(a.__len__()==b.__len__()):    #if length of a is equal to length of b then their is chance of equality and we need further checking
    #else not equal
    for i in range(1,a.__len__()):   ##for loop that run from starting index of list to end index
        if(a[i]!=b[i]):       #if their is any sitution when a[i] not equal to b [i] then flag c will become 1
            ct=1
        else:
            ct=0
    if(ct==0):              #checking flag c if 0 means their is no sitution found when a[i] not equal to b [i] and list a is equal to list b
        print("Equal")
    else:
        print("Not Equal")
else:
    print("Not equal")

