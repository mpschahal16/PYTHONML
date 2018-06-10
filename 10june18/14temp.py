word="HELLO"
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)
d.__delitem__("H")
print(d)
#delete item
d.pop("E")
print(d)