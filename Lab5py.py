from math import sqrt
#ввод числа N
n=int(input("Input none-negative integer number n: "))
#перебор комбинаций чисел a<=b<=c<=d
for a in range(0, int(sqrt(n))+1):
    for b in range(a, int(sqrt(n))+1):
        for c in range(b, int(sqrt(n))+1):
            for d in range(c, int(sqrt(n))+1):
                #Если комбинация подошла, выводим её
                if( a*a + b*b + c*c + d*d == n ):
                    print("%4d"%a, end="")
                    print("%4d"%b, end="")
                    print("%4d"%c, end="")
                    print("%4d"%d, end="")
                    print()
                    
print("These are all combinations!\nWIN!")
