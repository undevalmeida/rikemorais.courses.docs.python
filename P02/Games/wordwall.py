import random


def play():
    print("*******************************")
    print("Welcome to the Divination Game!")
    print("*******************************")

    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)
    file.close()
    number = random.randrange(0, len(words))
    secret = words[number].upper()

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
