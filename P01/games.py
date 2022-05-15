import divination
import wordwall

print("*******************************")
print("******Escolhe o seu jogo!******")
print("*******************************")

print("(1) Wordwall (2) Divination")

game = int(input("Qual jogo?"))

if game == 1:
    print("Playing Wordwall")
elif game == 2:
    print("Playing Divination")
