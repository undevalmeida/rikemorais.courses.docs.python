import random


def play():

    oppening()
    secret = loadWords()
    hits = loadLetters(secret)
    print(hits)

    over = False
    right = False
    errors = 0

    while not over and not right:
        kick = getKick()

        if kick in secret:
            markHit(secret, kick, hits)
        else:
            errors += 1
            draw(errors)

        over = errors == 6
        right = "_" not in hits
        print(hits)

    if right:
        win()
    else:
        lost(secret)

    print("End Game!")


def oppening():
    print("*******************************")
    print("Welcome to the Divination Game!")
    print("*******************************")


def loadWords():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)
    file.close()
    number = random.randrange(0, len(words))
    secret = words[number].upper()
    return secret


def loadLetters(secret):
    return ["_" for _ in secret]


def getKick():
    kick = input("What's the letter?").strip().upper()
    return kick


def markHit(secret, kick, hits):
    index = 0
    for letter in secret:
        if kick == letter:
            hits[index] = letter
        index += 1


def win():
    print("You Win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def lost(secret):
    print("You Lost!")
    print(f"A palavra era {secret}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
