pedido = input().split()
codigo = int(pedido[0])
quantidade = int(pedido[1])

if codigo == 1:
    print(f'Total: R$ {f"%.2f" % (quantidade * 4.00)}')
if codigo == 2:
    print(f'Total: R$ {f"%.2f" % (quantidade * 4.50)}')
if codigo == 3:
    print(f'Total: R$ {f"%.2f" % (quantidade * 5.00)}')
if codigo == 4:
    print(f'Total: R$ {f"%.2f" % (quantidade * 2.00)}')
if codigo == 5:
    print(f'Total: R$ {f"%.2f" % (quantidade * 1.50)}')