from Zestaw7.BaseFunction import usun_album_z_bazy, obcja4
from Zestaw7.FileFunction import zapisz_do_pliku, zaladuj_z_pliku_fileName, zapisz_do_pliku_fileName


def wybor_opcji():
    print('Wybierz opcję:')
    print('1. Załaduj z pliku')
    print('2. Zapisz do pliku')
    print('3. Wypisz całą bibliotekę')
    print('4. Dodaj album')
    print('5. Usuń album')
    print('6. Wyszukaj...')
    print('0. Koniec')
    wybrana_opcja = input('Wybierz polecenie: ...')
    try:
        return int(wybrana_opcja)
    except ValueError:
        print("nie wlasciwa obcja")
        return 0

def sortujObcje(opcja,baza):

    if opcja == 0:
        return None, baza #dzila
    elif opcja == 1:
        zaladuj_z_pliku_fileName() #dzila
        return True, baza
    elif opcja == 2:
        zapisz_do_pliku_fileName(baza) #dzila
        return True, baza
    elif opcja == 3:
        print(baza) #dziala
        return True, baza
    elif opcja == 4:
        obcja4(baza) #dzila
        return True, baza
    elif opcja == 5:
        usun_album_z_bazy(baza) #dzila
        return True, baza
    else:
        return None, baza

