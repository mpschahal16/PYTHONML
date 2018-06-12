## function defined here will be used in another .py python file

def add(*no):   ##add unknown no. of element by feeding them list feed the for loop means at every itration the value of x will be next value
    sum=0
    for x in no:
        sum+=x
    return sum

def add0(x,y):
    return x+y
