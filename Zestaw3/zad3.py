def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


def main():
    vector = []

    i = 0
    while i < 3:
        userInput = input("podaj liczbę: ")
        if userInput.isnumeric():
            userInput = float(userInput)

        if is_integer_num(userInput):
            if userInput == 1:
                i += 1
            vector.append(userInput)
        else:
            print("Podano liczba nie całkowita")

    print("suma: ", sum(vector))
    print("srednia: ", sum(vector) / len(vector))


if __name__ == '__main__':
    main()
