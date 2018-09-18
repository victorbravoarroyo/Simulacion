import math

m = 2**32 
a = 1013904223
c = 1664525
seed = int((94335 + 93784 + 96626)/3)

# Método Lineal Congruente [Lehmer, 1949]
#U(n) = (a*U(n-1) + c) mod m

Un = {}
Un[0] = seed

def U(n):
    if (n in Un) :
        return Un[n]
    else:
        Un[n] = (a*U(n-1) + c) % m
        return Un[n]

def fNormal(x):
    return (math.sqrt((2*math.pi)))**-1 * math.exp(x**2/-2)

def interpolarNormal():
    return 1

print(fNormal(1/2))

# 100.000 valores pseudo random generados por metodo de la transformada inversa
# randomNums1 = list()
# for i in range(0,100000):
    # x = interpolarNormal()
    # randomNums1.insert(i,x)