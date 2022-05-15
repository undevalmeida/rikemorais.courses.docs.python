def play():
    print("*******************************")
    print("Welcome to the Divination Game!")
    print("*******************************")

    secret = "banana"
    hits = ["_", "_", "_", "_", "_", "_"]

    over = False
    right = False

    print(hits)

    while not over and not right:
        kick = input("What's the letter?").strip().upper()

        index = 0
        for letter in secret:
            if kick == letter.upper():
                hits[index] = letter
            index = index + 1

        print(hits)

    print("Fim do Jogo!")


if __name__ == "__main__":
    play()
