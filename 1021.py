valor = float(input())

nota100 = f"%.0f" % (float(valor) // 100)
sobranota100 = f"%.2f" % (float(valor) % 100)
nota50 = f"%.0f" % (float(sobranota100) // 50)
sobranota50 = f"%.2f" % (float(sobranota100) % 50)
nota20 = f"%.0f" % (float(sobranota50) // 20)
sobranota20 = f"%.2f" % (float(sobranota50) % 20)
nota10 = f"%.0f" % (float(sobranota20) // 10)
sobranota10 = f"%.2f" % (float(sobranota20) % 10)
nota5 = f"%.0f" % (float(sobranota10) // 5)
sobranota5 = f"%.2f" % (float(sobranota10) % 5)
nota2 = f"%.0f" % (float(sobranota5) // 2)
sobranota2 = f"%.2f" % (float(sobranota5) % 2)
moeda1 = f"%.0f" % (float(sobranota2) // 1.00)
sobramoeda1 = f"%.2f" % (float(sobranota2) % 1.00)
moeda050 = f"%.0f" % (float(sobramoeda1) // 0.50)
sobramoeda050 = f"%.2f" % (float(sobramoeda1) % 0.50)
moeda025 = f"%.0f" % (float(sobramoeda050) // 0.25)
sobramoeda025 = f"%.2f" % (float(sobramoeda050) % 0.25)
moeda010 = f"%.0f" % (float(sobramoeda025) // 0.10)
sobramoeda010 = f"%.2f" % (float(sobramoeda025) % 0.10)
moeda005 = f"%.0f" % (float(sobramoeda010) // 0.05)
sobramoeda005 = f"%.2f" % (float(sobramoeda010) % 0.05)
moeda001 = f"%.0f" % (float(sobramoeda005) / 0.01)

print("NOTAS:")
print(f'{nota100} nota(s) de R$ 100.00')
print(f'{nota50} nota(s) de R$ 50.00')
print(f'{nota20} nota(s) de R$ 20.00')
print(f'{nota10} nota(s) de R$ 10.00')
print(f'{nota5} nota(s) de R$ 5.00')
print(f'{nota2} nota(s) de R$ 2.00')
print("MOEDAS:")
print(f'{moeda1} moeda(s) de R$ 1.00')
print(f'{moeda050} moeda(s) de R$ 0.50')
print(f'{moeda025} moeda(s) de R$ 0.25')
print(f'{moeda010} moeda(s) de R$ 0.10')
print(f'{moeda005} moeda(s) de R$ 0.05')
print(f'{moeda001} moeda(s) de R$ 0.01')
