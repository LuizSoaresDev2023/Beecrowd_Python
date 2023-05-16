numero = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

print(f'NUMBER = {numero}')
print(f'SALARY = U$ {f"%.2f" % (horas_trabalhadas * valor_por_hora)}')