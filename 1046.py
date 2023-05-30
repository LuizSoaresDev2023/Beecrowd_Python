horarios = input().split()

hora_inicial = int(horarios[0])
hora_final = int(horarios[1])

if hora_inicial == hora_final:
    print('O JOGO DUROU 24 HORA(S)')
elif hora_inicial < hora_final:
    print(f'O JOGO DUROU {hora_final - hora_inicial} HORA(S)')
elif hora_inicial > hora_final:
    print(f'O JOGO DUROU {(hora_final + 24) - hora_inicial} HORA(S)')