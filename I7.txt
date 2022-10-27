## Chinmay D. 10/27/2022 Hg5590
def IssueSeven(a, b, c):
# Naming and starting the function with multiple parameters
    x=(b-c)/(3*a)
    return x
def Cpl( a,d, c):
    y=(c-d)/(3*a)
    return y
def Cpk(x,y):
    if(x>y):
        a=y
    else:
        a=x
    print("Cpk= "+str(a))
# Prints out the Cpk which is the miniumim of (x,y)
    return 0
b=17.5
d=15.5
e=2.326
c=16.507
f=0.561
a=f/e
x=IssueSeven(a,b,c)
y=Cpl(a,d,c)
print("x = "+str(x))
print("y = "+str(y))
Cpk(x,y)
# End of the function and fullfills all the criteria 