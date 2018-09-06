import matplotlib.pyplot as plt
import numpy as np

#Xn+1 = (Xn + c) mod m

m = 2**32
c = 1664525
a = 1013904223
seed = 94335 #CAMBIAR POR EL PROMEDIO DE NUESTROS PADRONES

#IMPRIMIR LOS PRIMEROS 6
for i in range(0,6):

    x = (a*seed + c) % m
    print(x)
    seed = x
