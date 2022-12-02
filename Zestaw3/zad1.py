from itertools import count


def main():

    #deklaracja tabel na dane pobrane od uzytkownika
    wyrazy = []
    liczby = []

    for _ in count(): #najszybsza nieskonczona pentla w pythonie
        # ciekawostka _ nie jest jakas magicnza nazwom ignorujaca wartosc zostaje do niej przypisana zadana wartosc poprostu zwyczajowo jest ignorowana

        #pobranie danych od uzytkownika
        userInput = input("podaj liczbę lub wyraz naciśnij enter zeby zakończy")

        #sortowanie danych od uzytkownika
        if userInput.isnumeric():
            liczby.append(int(userInput))
        elif len(userInput):
            wyrazy.append(userInput)
        else:
            break

    print("ilosc wprowadzonych wyrazów", len(wyrazy))

    print("ilosc wprowadzonych znaków", sum([len(wyraz) for wyraz in wyrazy]))

    print("liczba wprowadzonych cyfr", len(liczby))

    print("suma wprowadzonych cyfr", sum(liczby))


if __name__ == '__main__':
    main()
