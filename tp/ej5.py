from math import floor

def generateRandomNumbers(a, c, m, times, u = 0):
  for i in range(times):
    u = ((a*u + c) % m) / m
    print('Iteration: ', i+1, ' Generated Number: ',  u)

promPadron = floor((94335 + 93784) / 2)

generateRandomNumbers(1013904223, 1664525, 2**32, 10, promPadron)
