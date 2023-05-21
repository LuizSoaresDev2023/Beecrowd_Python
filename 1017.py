tempo_gasto = int(input())
velocidade_media = int(input())

Kilometragem_feita = velocidade_media * tempo_gasto

litros = f"%.3f" % (Kilometragem_feita / 12)

print(litros)



