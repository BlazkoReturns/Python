print('Informe a primeira nota:')
nNota1 = float(input())
print('Informe a segunda nota:')
nNota2 = float(input())

nNotaMedia = (nNota1+nNota2)/2

if nNotaMedia >= 7.0:
  print(f"Aprovado! Sua média foi: {nNotaMedia}")
elif nNotaMedia >= 5.0 and nNotaMedia <= 6.9:
  print(f"Recuperação. Sua média foi: {nNotaMedia}")
else:
  print(f"Reprovado. Sua nota média foi {nNotaMedia}")