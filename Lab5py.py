from math import sqrt
n=int(input("Input none-negative integer number n: "))
for a in range(0, int(sqrt(n))+1):
    for b in range(a, int(sqrt(n))+1):
        for c in range(b, int(sqrt(n))+1):
            for d in range(c, int(sqrt(n))+1):
                if( a*a + b*b + c*c + d*d == n ):
                    print("%4d"%a, end="")
                    print("%4d"%b, end="")
                    print("%4d"%c, end="")
                    print("%4d"%d, end="")
                    print()
                    
print("These are all combinations!\nWIN!")
