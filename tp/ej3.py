from math import log
import matplotlib.pyplot as plt

m = 2**32
c = 1664525
a = 1013904223
seed = 94059
nums = list()
for i in range(0,100000):

    x = ((a*seed + c) % m)/m
    nums.insert(i,x)
    seed = x