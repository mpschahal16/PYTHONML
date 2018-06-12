dict1={"name":'manpreet','middle':'singh'}
dict2={"last":"chahal"}


#updating dictionary
dict1.update(dict1)   #   a.update(b)  will append those values from b which are not present in a
print(dict1)
dict1.update(dict2)
print(dict1)
print(dict1.items())

dict2.update(dict1)
print(dict2)

print(dict)
d=dict()    ###using function by assigning that function to a variable
print(d)
print(type(d))

'''
O/P

{'name': 'manpreet', 'middle': 'singh'}
{'name': 'manpreet', 'middle': 'singh', 'last': 'chahal'}
dict_items([('name', 'manpreet'), ('middle', 'singh'), ('last', 'chahal')])
{'last': 'chahal', 'name': 'manpreet', 'middle': 'singh'}
<class 'dict'>
{}
<class 'dict'>

'''