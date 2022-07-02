# Bloco 01
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print("Bloco 01")
print("Lista: ", assistiram)
print("Lista Completa: ", len(assistiram))
print("Lista Resumida: ", len(set(assistiram)))
print("\n")

# Bloco 02
print("Bloco 02")
for usuario in set(assistiram):
    print(usuario)
print("\n")
