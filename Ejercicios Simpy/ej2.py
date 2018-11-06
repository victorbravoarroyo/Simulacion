# 70 seg de simulacion 50 personas entrando a un local, >=4min tiempo de atencion
# 50 clientes
# tiempo de atencion 4 +- 2 seg
import simpy
import random
# import numpy as np

def person(env):
  index = 1
  while True:
    print("Persona ", index)

    print("Comienzo de atencion en", round(env.now/60, 2), "minutos")
    duracionAtencion = random.randint(2, 6)
    yield env.timeout(duracionAtencion)

    index += 1
    if (index == 51): 
      return

environment = simpy.Environment()
environment.process(person(environment))
environment.run()

