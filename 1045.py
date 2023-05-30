valores = input().split()

v1 = float(valores[0])
v2 = float(valores[1])
v3 = float(valores[2])

lista = [v1, v2, v3]
lista_ordenada = sorted(lista)

a = float(lista_ordenada[2])
b = float(lista_ordenada[1])
c = float(lista_ordenada[0])

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a ** 2) == (b ** 2) + (c ** 2):
        print("TRIANGULO RETANGULO")
    if (a ** 2) > (b ** 2) + (c ** 2):
        print("TRIANGULO OBTUSANGULO")
    if (a ** 2) < (b ** 2) + (c ** 2):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b and c != b) or (a == c and b != c) or (b == c and a != c):
        print("TRIANGULO ISOSCELES")

