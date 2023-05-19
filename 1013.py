valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maiorab = int((a + b + abs(a - b)) / 2)

maiorabc = int((maiorab + c + abs(maiorab - c)) / 2)

print(f'{maiorabc} eh o maior')