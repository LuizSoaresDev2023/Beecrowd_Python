notas = input().split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
p1 = 2
p2 = 3
p3 = 4
p4 = 1
mediaponderada = ((n1*p1) + (n2*p2) + (n3*p3) + (n4*p4)) / (p1 + p2 + p3 + p4)
mediaponderadaarred = (round(mediaponderada,1))
print(f'Media: {mediaponderadaarred}')
if mediaponderadaarred >= 7.0:
  print("Aluno aprovado.")
elif mediaponderadaarred < 5.0:
  print("Aluno reprovado.")
else:
  print("Aluno em exame.")
  notaexame = float(input())
  print(f'Nota do exame: {notaexame}')
  mediafinal = (notaexame + mediaponderadaarred)/2
  mediafinalarred = (round(mediafinal,1))
  if mediafinalarred >= 5.0:
    print("Aluno aprovado.")
    print(f'Media final: {mediafinalarred}')
  else:
    print("Aluno reprovado.")
    print(f'Media final: {mediafinalarred}')