from Zestaw7.FileFunction import zaladu_z_pliku
from Zestaw7.OptionFunction import sortujObcje, wybor_opcji

if __name__ == "__main__":
    fileName = "tak"

    print("Witamy w prostym programie do obsługi bazy danych plyt muzycznych")

    baza = zaladu_z_pliku(fileName)
    pentla = True

    while pentla:
        pentla, baza = sortujObcje(wybor_opcji(), baza)

    print('Dziękujemy za używanie niezmiernie fajnej aplikacji')
