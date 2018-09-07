from math import log
import matplotlib.pyplot as plt
alfa = 1/15
m = 2**32
c = 1664525
a = 1013904223
seed = 94335
nums = list()
exp = 0
for i in range(0,100000):

    x = ((a*seed + c) % m)/m
    exp = (log(1-x)/alfa)*(-1)
    nums.insert(i,exp)
    seed = x

plt.hist(nums,color='green')
plt.title('Distribucion de los numeros aleatorios obtenidos',color = 'blue')
plt.xlabel('Numeros obtenidos', color = 'blue')
plt.ylabel('Cantidad de apariciones',color = 'blue')
plt.show()