# Bloco 01 - Contando Elementos
from attr import frozen
QUANTIDADE = "Quantidade: "
USERS = "Users: "

usuarios = {1, 5, 76, 34, 52, 13, 17}
print("Bloco 01")
print(USERS, usuarios)
print(QUANTIDADE, len(usuarios))
print("\n")

# Bloco 02 - Adicionando Elementos
print("Bloco 02")
usuarios.add(666)
print(USERS, usuarios)
print(QUANTIDADE, len(usuarios))
print("\n")

# Bloco 03 - Congelando o Incremento
# usuarios = frozenset(usuarios) # Essa linha impede o uso do add.
print(usuarios)
print("Bloco 02")
usuarios.add(667)
print(USERS, usuarios)
print(QUANTIDADE, len(usuarios))
print("\n")

# Bloco 04 - Fatiando um Texto
texto = "Eu gosto bastante de chocolate amargo."
print("Bloco 04")
print("Texto: ", texto)
print("Split: ", texto.split())
print("Set e Split: ", set(texto.split()))
