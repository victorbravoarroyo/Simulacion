import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp, pi

c= sqrt(2*exp(1)/pi)

#GENERO N MUESTRAS EXPONENCIALES DE MEDIA 1
n = 10
numsExp = list()
probabilidadDeAceptar = list()

#NORMAL DE MEDIA 35 Y VARIANZA 25
def normal(x):

    return ((exp(-0.5*(((x-35)/5)**2)))/sqrt(25*2*pi))


def prob(x):

    return (normal(x)/(c*exp(-x)))


for i in range(0,n):
    t = np.random.exponential(1, 1)
    numsExp.insert(i, t)
    probabilidadDeAceptar.insert(i,prob(t))

numsGauss = list()
for i in range(0,n):

    r = np.random.uniform()
    if r < p(n):
        r2 = np.random.uniform()
        if r2 < 0.5:
            numsGauss.insert(i,numsExp[i])
        else:
            numsGauss.insert((i,(numsExp[i]*(-1))))

plt.hist(numsGauss)
plt.show()