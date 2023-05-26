import math

valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = float((b ** 2) - (4 * a * c))

if (2 * a) == 0 or delta < 0:
    print("Impossivel calcular")
else:
    x1 = -(b) + (math.sqrt(delta)) / (2 * a)
    x2 = -(b) - (math.sqrt(delta)) / (2 * a)
    print(f'R1 = {f"%.5f" % x1}')
    print(f'R2 = {f"%.5f" % x2}')