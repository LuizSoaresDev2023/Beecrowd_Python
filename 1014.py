distancia_total_percorrida = int(input())
combustivel_gasto = float(input())

consumo_medio = f"%.3f" % (distancia_total_percorrida/combustivel_gasto)

print(f'{consumo_medio} km/l')

