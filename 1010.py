entrada1 = input().split()
codigo_peca1 = int(entrada1[0])
numero_de_pecas1 = int(entrada1[1])
valor_unitario1 = float(entrada1[2])
valor_a_pagar1 = numero_de_pecas1 * valor_unitario1

entrada2 = input().split()
codigo_peca2 = int(entrada2[0])
numero_de_pecas2 = int(entrada2[1])
valor_unitario2 = float(entrada2[2])
valor_a_pagar2 = numero_de_pecas2 * valor_unitario2

valor_total = valor_a_pagar1 + valor_a_pagar2

print(f'VALOR A PAGAR: R$ {f"%.2f" % valor_total}')


