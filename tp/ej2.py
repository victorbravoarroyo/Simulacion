import numpy as np
from math import log
import matplotlib.pyplot as plt

alfa = 1/15
m = 2**32
c = 1664525
a = 1013904223
seed = 94059
nums = list()
numsExp = list()
exp = 0

for i in range(0,100000):

    x = ((a*seed + c) % m)
    nums.insert(i,x/m)
    seed = x

for i in range(0,100000):

    exp = (log(1-(nums[i]))/alfa)*(-1)
    numsExp.insert(i,exp)

print('Varianza = ' + str(np.var(numsExp)))
print('Media = ' + str(np.median(numsExp)))
#print('Moda = ' + str(np.mod(numsExp)))

plt.hist(numsExp,bins = 150,color='green')
plt.title('Distribucion de los numeros aleatorios obtenidos',color = 'blue')
plt.xlabel('Numeros obtenidos', color = 'blue')
plt.ylabel('Cantidad de apariciones',color = 'blue')
plt.show()