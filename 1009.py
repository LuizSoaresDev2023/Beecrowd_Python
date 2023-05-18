nome_vendedor = input()
salario_fixo = float(input())
total_de_vendas_efetuadas_por_mes = float(input())

percentual_de_vendas = total_de_vendas_efetuadas_por_mes * 0.15

total_a_receber = salario_fixo + percentual_de_vendas

print(f'TOTAL = R$ {f"%.2f" % (total_a_receber)}')



