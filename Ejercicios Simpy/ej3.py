# 70 seg de simulacion 50 personas entrando a un local, >=4min tiempo de atencion
# 50 clientes
# tiempo de atencion 4 +- 2 seg
import simpy
import random

simulation_time = 600
# index = 1

def auto(env):
  index = 1
  while True:
    arriboEntreAutos = random.expovariate(1/2)
    yield env.timeout(arriboEntreAutos)
    env.process(auto2(env, index))
    index +=1

def auto2(env, index):
  print("Auto ", index)
  print("Comienzo de atencion en", round(env.now/60, 2), "minutos")
  duracionEstacionamiento = 3
  yield env.timeout(duracionEstacionamiento)
  

environment = simpy.Environment()
environment.process(auto(environment))
environment.run(until=simulation_time)

