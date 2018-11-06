import simpy

# environment = simpy.Environment
# environment.run()
# environment.now
# environment.active_process
# environment.process(generator)

def loop():
  index = 1
  while index <= 10:
    yield index*2
    index += 1

for i in loop():
  print(i)
  