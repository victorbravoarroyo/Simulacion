import math

m = 2**32 
a = 1013904223
c = 1664525
seed = int((94335 + 93784 + 96626)/3)

# Método Lineal Congruente [Lehmer, 1949]
#U(n) = (a*U(n-1) + c) mod m

def fNormal(x):
    return (math.sqrt((2*math.pi)))**-1 * math.exp(x**2/-2)

def vNormal(u1, u2):
    return math.sqrt(-2*math.log(u1))*math.cos(u2)

def generateRandomUniform(a, c, m, seed):
    u = (a*seed + c) % m
    return {
        "nextSeed": u,
        "number": u/m
    }

for i in range(0, 10):
    u1 = generateRandomUniform(a, c, m, seed)
    seed = u1["nextSeed"]
    u2 = generateRandomUniform(a, c, m, seed)
    seed = u2["nextSeed"]
    z1 = vNormal(u1["number"], u2["number"])
    print('Generated u1 = ', u1["number"])
    print('Generated u2 = ', u2["number"])
    print('Generated z1 = ', z1)

# 100.000 valores pseudo random generados por metodo de la transformada inversa
# randomNums1 = list()
# for i in range(0,100000):
    # x = interpolarNormal()
    # randomNums1.insert(i,x)