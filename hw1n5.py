a = float( input())
b = float( input())
c = float( input())
D = b**2 - 4*a*c
if (D > 0 and a > 0):
    x1 = (-b + D**0.5 )/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    print("X1:",x1,"X2:", x2)
elif (D == 0 and a > 0):
    x1=(-b)/(2*a)
    print("X1:", x1)
elif (D < 0 and a >0):
    print("")
else:
    print('')  
    
