entrada = input().split()

valor1 = int(entrada[0])
valor2 = int(entrada[1])
valor3 = int(entrada[2])

lista = [valor1, valor2, valor3]

lista_crescente = sorted(lista)

print(lista_crescente[0])
print(lista_crescente[1])
print(lista_crescente[2])
print("")
print(valor1)
print(valor2)
print(valor3)