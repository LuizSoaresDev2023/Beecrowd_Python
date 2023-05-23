tempo = int(input())

horas = tempo // 3600
sobrahoras = tempo % 3600

minutos = sobrahoras // 60
sobraminutos = sobrahoras % 60

segundos = sobraminutos // 1

print(f'{horas}:{minutos}:{segundos}')