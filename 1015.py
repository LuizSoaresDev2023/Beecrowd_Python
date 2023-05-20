import math

linha_1 = input().split()
x1 = float(linha_1[0])
y1 = float(linha_1[1])

linha_2 = input().split()
x2 = float(linha_2[0])
y2 = float(linha_2[1])

distancia = f"%.4f" % (math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))

print(distancia)

