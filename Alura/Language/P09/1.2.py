# Exemplo 01
idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

idades = [39, 30, 27, 18]

print(type(idades))
print(len(idades))
print(idades[0], idades[1], idades[2], idades[3])
print(idades)

for idade in idades:
  print(idade)

idades.remove(30)
print(idades)
idades.append(15)
print(idades)