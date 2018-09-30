import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from math import sqrt, exp, pi, log

c = sqrt(2*exp(1)/pi)

n = 100000
aceptados = list() #VALORES ACEPTADOS SEGUN DISTRIBUCIÓN NORMAL, MEDIA 35 Y DESVÍO 5

#NORMAL DE MEDIA 35 Y VARIANZA 25
def X(t):
    return exp(-0.5*(((t-35)/5)**2))/(5*sqrt(2*pi))

def Y(t):
    return exp(-t)

def prob(t):
    return (X(t)/(c*Y(t)))

for i in range(0,n):
    u = np.random.uniform()
    
    j = (log(1-(np.random.uniform())))*(-1)

    if(u > prob(j)):
        if(u >= 0.5):
            aceptados.append((j*5)+35)
        else:
            aceptados.append(((-1*j)*5)+35)

print('Varianza = ' + str(np.var(aceptados)))
print('Media = ' + str(np.median(aceptados)))
print('Moda = ' + str(st.mode(aceptados)[0][0]))
print('cantidad de aceptados ' + str(len(aceptados)))