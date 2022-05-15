def play():
    print("*******************************")
    print("Welcome to the Divination Game!")
    print("*******************************")

    secret = "banana"

    over = False
    right = False

    while not over and not right:
        kick = input("What's the letter?").strip().upper()

        index = 0
        for letter in secret:
            if kick == letter.upper():
                print(f"Encontrei a letra {letter.upper()} na posição {index}")
            index = index + 1

        print("Jogando!")

    print("Fim do Jogo!")


if __name__ == "__main__":
    play()
