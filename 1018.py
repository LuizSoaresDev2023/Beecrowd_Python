valor = int(input())

valor100 = valor // 100
sobra100 = valor % 100

valor50 = sobra100 // 50
sobra50 = sobra100 % 50

valor20 = sobra50 // 20
sobra20 = sobra50 % 20

valor10 = sobra20 // 10
sobra10 = sobra20 % 10

valor5 = sobra10 // 5
sobra5 = sobra10 % 5

valor2 = sobra5 // 2
sobra2 = sobra5 % 2

valor1 = sobra2 // 1

print(valor)
print(f'{valor100} nota(s) de R$ 100,00')
print(f'{valor50} nota(s) de R$ 50,00')
print(f'{valor20} nota(s) de R$ 20,00')
print(f'{valor10} nota(s) de R$ 10,00')
print(f'{valor5} nota(s) de R$ 5,00')
print(f'{valor2} nota(s) de R$ 2,00')
print(f'{valor1} nota(s) de R$ 1,00')


