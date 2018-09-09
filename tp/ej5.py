from math import floor

def generateRandomNumbers(a, c, m, times, u = 0):
  for i in range(times):
    u = ((a*u + c) % m) / m
    print('Iteration: ', i+1, ' Generated Number: ',  u)
    convertToFixedNumber(u)


def convertToFixedNumber(u):
  if (u <= .5):
    print('Generated Number: ', 1)
  elif (u > .5 and u <= .7):
    print('Generated Number: ', 2)
  elif (u > .7 and u <= .8):
    print('Generated Number: ', 3)
  elif (u > .8 and u <= 1):
    print('Generated Number: ', 4)

promPadron = floor((94335 + 93784) / 2)

generateRandomNumbers(1013904223, 1664525, 2**32, 100, promPadron)
