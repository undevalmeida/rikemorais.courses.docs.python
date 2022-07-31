idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]

print(type(idades))
print(len(idades))

for elemento in idades:
  print("Recebi o elemento", elemento)
  
idades = [20, 39, 18]
idades.extend([27, 19])
print(idades)

for idade in idades:
  print(idade + 1)
  
idades_no_ano_que_vem = []
for idade in idades:
  idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)

idades_no_ano_que_vem = [idade+1 for idade in idades]
print(idades_no_ano_que_vem)

[idade for idade in idades if idade > 21]
print(idades)

def proximo_ano(idade):
  return idade+1

[proximo_ano(idade) for idade in idades if idade > 21]
print(idades)