a=[1,2,3]      ##list is initialized with []
print(a)            #will print all the element of the list
print(type(a))      # will print type of a i.e. list
print(type(a[1]))    #will print type of element present at index 1 of list a

b=['hello' ,'world',1 ,2, 5]
print(b)
print(b[1])     #will print element present at index 1 of list b
print(b[1][4])   #will print element present at index 4 of subtype (that can br tuple,list or set) present at index 1 of list  b


print(b[1:4])  #sub string the list b from index 1 to index (4-1)

c=a+b   #will join to list
print(c)

#length of list
print(a.__len__())
print(c.__len__())

c.append(5)   #will push 5 to list c at last
print(c)



a.pop(2)        #will remove element present at index 2
print(a)

#xyx=[1,2,3,[45,85,69,64,96,89],0]  ##will only work when their is no inner list
xyx=[1,2,3,0]
xyx.sort()    # will sort list in assending order
print(xyx)



xyx.reverse() #will reverse the list
print(xyx)


