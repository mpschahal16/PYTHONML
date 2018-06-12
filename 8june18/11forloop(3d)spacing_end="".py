x=1
for i in range(1,6):
    for j in range(1,6):
        print("%3d"%x,end="\t")#in printf 3 means spacing and d is related to allignement where '+' sign with d will allign right to left
        # '-' sign with d will allign left to right
        x+=10
    print()

print("\n")



x=1
for i in range(1,6):
    for j in range(1,6):
        print("%-3d"%x,end="\t")   #'-' sign with d
        x+=10
    print()



print("\n")

x=1
for i in range(1,6):
    for j in range(1,6):
        print("%-10d"%x,end="\t") ###more value with d for more spacing
        x+=10
    print()