#simple calculater
print("Enter the two no")
a=int(input("ENTER THE FIRDT NO"))
b=int(input("Enter the second no"))
print("press + for add")
print("press - for sub")
print("press * for mul")
print("press / for real dev")
print("press // for floor div")
print("press % for rem")
print("Enter ur choice")
ch=input()
if(ch=='+'):
    print(a+b)
elif(ch=='-'):
    print(a-b)
elif(ch=='*'):
    print(a*b)
elif(ch=='/'):
    print(a/b)
elif(ch=="//"):
    print(a//b)
elif(ch=="%"):
    print(a%b)
else:
    print("wrong input")