def podpunktA(wykladnik=2):
    # Funkcja wypisuje potęgi zadanego wykładnika dla liczb od 1 do 199
    for i in range(1, 200):  # pętla od 1 do 199
        print(pow(i, wykladnik))


def podpunktB():
    # Funkcja pobierająca impute od użytkownika i wypisująca od 1 do 199 protege dla tego wykładnika

    try:  # rozpoczęcie initialization wyłapania potencjalnego blendnego impute

        # odczyt impute
        wykladnik = input("Podaj wykładnik (int): ")

        # sprawdzenie, czy wykładnik jest dodatni oraz konwersja go na liczba całkowita
        if (wykladnik := int(wykladnik)) < 0:
            raise ValueError

        '''
        #Wersja przed python 3.8:
        wykładnik = int(wykładnik) # konwersja na liczbę całkowita
        if wykładnik < 0: 
            raise ValueError
        '''

        # wywołanie skryptu wypisującego potęgi
        podpunktA(wykladnik)

    except ValueError:
        # obsłużenie potencjalnego biednego impute
        print("Program obsługuje tylko i wyłącznie dodatnie całkowite wykładniki")

def alternatywnyPodpunktA(mianownik=1.0):
    if mianownik!=0:
        for i in range(1, 200):  # pętla od 1 do 199
            print(i/ mianownik)

def alternatywnyPodpunktB():
    try:  # rozpoczęcie initialization wyłapania potencjalnego blendnego impute

        # odczyt impute
        mianownik = input("Podaj wykładnik (int): ")


        # wywołanie skryptu wypisującego potęgi
        alternatywnyPodpunktA(float(mianownik))

    except ValueError:
        # obsłużenie potencjalnego biednego impute
        print("Program obsługuje tylko i wyłącznie dodatnie całkowite wykładniki")


if __name__ == '__main__':
    podpunktB()
