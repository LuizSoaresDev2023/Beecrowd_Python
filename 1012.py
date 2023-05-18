valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

area_triangulo_retangulo = float(a * c)/2
area_circulo = float(3.14159 * (c ** 2))
area_trapezio = float(((a + b) * c)/2)
area_quadrado = float(b ** 2)
area_retangulo = float(a * b)

print(f'TRIANGULO: {f"%.3f" % area_triangulo_retangulo}')
print(f'CIRCULO: {f"%.3f" % area_circulo}')
print(f'TRAPEZIO: {f"%.3f" % area_trapezio}')
print(f'QUADRADO: {f"%.3f" % area_quadrado}')
print(f'RETANGULO: {f"%.3f" % area_retangulo}')



