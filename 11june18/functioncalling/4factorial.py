##recursive function to find the factorial of no

##recursion is less preffered in python coz it take more memory

def fact(x):
    if(x==1):
        return 1
    else:
        return(fact(x-1)*x)


print('FACTORIAL :',fact(5))


'''
o/pS
FACTORIAL : 120

'''