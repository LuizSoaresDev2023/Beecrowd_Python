valores = input().split()

a = int(valores[0])
b = int(valores[1])

if b > a or b == a:
    if a == 0 or b % a == 0:
        print("Sao Multiplos")
    elif b % a != 0:
        print("Nao sao Multiplos")
else:
    if b == 0 or a % b == 0:
        print("Sao Multiplos")
    elif a % b != 0:
        print("Nao sao Multiplos")