import numpy as np

def serviceCall():
  return np.random.exponential(1/4)

def distributedDBProcessTime():
  if (np.random.rand() <= 0.6):
    return np.random.exponential(10/7)
  else:
    return np.random.exponential(1)

def centralDBProcessTime():
  return np.random.exponential(10/8)
  
def meanInstantProcessedServiceCalls(waitTimes):
  return waitTimes.count(0) / len(waitTimes)

def simulateWaitTimes(processFn, times):
  serviceCallTime = 0
  readyAtTime = 0
  waits = list()

  for i in range(0, times):
    serviceCallTime += serviceCall()
    processTime = processFn()
    waitTime = readyAtTime - serviceCallTime

    if (waitTime > 0):
      waits.append(waitTime)
    else:
      waits.append(0)

    readyAtTime = serviceCallTime + processTime

  return waits

distributedWaitTimes = simulateWaitTimes(distributedDBProcessTime, 100000)
centralWaitTimes = simulateWaitTimes(centralDBProcessTime, 100000)

print('Tiempo medio de espera - 2 bases de datos distribuidas', np.mean(distributedWaitTimes))
print('Tiempo medio de espera - 1 base de datos central', np.mean(centralWaitTimes))

print('Fracción de solicitudes que no esperaron para ser procesadas - 2 bases de datos distribuidas', meanInstantProcessedServiceCalls(distributedWaitTimes))
print('Fracción de solicitudes que no esperaron para ser procesadas - 1 base de datos central', meanInstantProcessedServiceCalls(centralWaitTimes))

