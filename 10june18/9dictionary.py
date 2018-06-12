dict={'fname':'manpreet'+'chahal','secondname':'singh','dob':'16/10/1997'}
print(dict)
print(dict['fname'])



#updation

dict['fname']="jaspreet"
print(dict)
dict['age']='16'
print(dict)


#empty dictionary
dict.clear()
print(dict)

'''
o/p

{'fname': 'manpreetchahal', 'secondname': 'singh', 'dob': '16/10/1997'}
manpreetchahal
{'fname': 'jaspreet', 'secondname': 'singh', 'dob': '16/10/1997'}
{'fname': 'jaspreet', 'secondname': 'singh', 'dob': '16/10/1997', 'age': '16'}
{}
'''




