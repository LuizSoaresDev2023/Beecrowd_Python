idade = int(input())

anos = idade // 365
sobraanos = idade % 365

meses = sobraanos // 30
sobrameses = sobraanos % 30

dias = sobrameses // 1

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')