def play():
    print("*******************************")
    print("Welcome to the Divination Game!")
    print("*******************************")

    secret = "rike".upper()
    hits = ["_" for letter in secret]

    over = False
    right = False
    errors = 0

    print(hits)

    while not over and not right:
        kick = input("What's the letter?").strip().upper()

        if kick in secret:
            index = 0
            for letter in secret:
                if kick == letter:
                    hits[index] = letter
                index += 1
        else:
            errors += 1

        over = errors == 6
        right = "_" not in hits
        print(hits)

    if right:
        print("You Win!")
    else:
        print("You lost!")
    print("End Game!")


if __name__ == "__main__":
    play()
