import random


def play():
    print("Welcome to the Divination Game!")
    print("*"*31)
    print("*"*31)

    secret = random.randrange(1, 101)
    attempts = 0
    points = 1000

    print("Qual o nílvel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        attempts = 20
    elif nivel == 2:
        attempts = 10
    else:
        attempts = 5

    for rodada in range(1, attempts + 1):
        print(f"Tentativa {rodada} de {attempts}")

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute)

        if chute < 1 or chute >= 100:
            print("Você desve digitar um número entre 1 e 100!")
            continue

        acertou = chute == secret
        maior = chute > secret
        menor = chute < secret

        if acertou:
            print(f"Você acertou e fez {points} pontos")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto!")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(secret - chute)
            pontos = points - pontos_perdidos

    print("Fim do Jogo!")

    if __name__ == "__main__":
        play()
