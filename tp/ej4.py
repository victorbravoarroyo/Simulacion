import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from math import sqrt, exp, pi

c= sqrt(2*exp(1)/pi)

#GENERO N MUESTRAS EXPONENCIALES DE MEDIA 1
n = 100000
numsExp = list()
probabilidadDeAceptar = list()
numsGauss = list() #ACA GUARDO LOS VALORES ACEPTADOS COMO GAUSSIANOS

#NORMAL DE MEDIA 35 Y VARIANZA 25
def normal(x):

    return ((exp(-0.5*(((x-35)/5)**2)))/sqrt(50*pi))

#PROBABILIDAD DE ACPTAR EL VALOR GENERADO
def prob(x):

    return (normal(x)/(c*exp(-x)))

#GENERO MUESTRAS DE EXPONENCIALES DE MEDIA 1 Y GENERO UN VECTOR DE PROBABILIDADES
#DE ACEPTAR CADA VALOR GENERADO
for i in range(0,n):
    t = np.random.exponential(1)
    numsExp.insert(i, t)
    probabilidadDeAceptar.insert(i,prob(t))

for i in range(0,n):
    r = np.random.uniform()

    if r > probabilidadDeAceptar[i]:
        r2 = np.random.uniform()
        if r2 < 0.5:
            numsGauss.insert(i,numsExp[i])
        else:
            numsGauss.insert(i,numsExp[i]*(-1))

print('Porcentaje de rechazo = ' + str((n-len(numsGauss))/n))


print('Varianza = ' + str(np.var(numsGauss)))
print('Media = ' + str(np.median(numsGauss)))
print('Moda = ' + str(st.mode(numsGauss)))

plt.hist(numsGauss,bins=1000)
plt.show()