import math

valoresabc = input().split()

a = float(valoresabc[0])
b = float(valoresabc[1])
c = float(valoresabc[2])

delta = (b**2)-4*a*c
base = 2*a

if delta < 0 or base == 0:
  print('Impossivel calcular')
else:
  x1 = (-b + math.sqrt(delta)) / base
  x2 = (-b - math.sqrt(delta)) / base
  print(f'R1 = {f"%.5f" % x1}')
  print(f'R2 = {f"%.5f" % x2}')