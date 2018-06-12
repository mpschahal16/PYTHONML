# sum of list element


a=[23,45,56,78]
sum=0
for i in range(0,a.__len__()):    #for loop to intitrate from 0 index to last index(i.e = to length of list -1)
    sum=sum+a[i]    #using i to acess list element prestnt at index i
print(sum)