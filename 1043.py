valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

perimetro = f"%.1f" % (a + b + c)

area = f"%.1f" % (((a + b) * c) / 2)

if abs(b-c) < a < (b + c) and abs(a-c) < b < (a + c) and abs(a-b) < c < (a + b):
    print(f'Perimetro = {perimetro}')
else:
    print(f'Area = {area}')