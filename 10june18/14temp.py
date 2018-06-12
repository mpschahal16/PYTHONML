
## THIS PROGRAM MAKES THE DICTIONARY of alphabet as a key with their occurance in word as value

word="HELLO"
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)





d.__delitem__("H")    ##delete key H with its vaue form d dictionary
print(d)
#delete item
d.pop("E")          ##delete key E with its vaue form d dictionary
print(d)




'''
O/P

{'H': 1, 'E': 1, 'L': 2, 'O': 1}
{'E': 1, 'L': 2, 'O': 1}
{'L': 2, 'O': 1}

'''