
def obcja4(baza):
    album = wprowadz_album()
    return dodaj_album_do_bazy(baza,album)

def wprowadz_album():
    tytul = input('Tytuł albumu:')
    wykonawca = input('Wykonawca: ')
    utwory = []
    while True:
        utwor = input('Tytuł utworu: ')
        if len(utwor) == 0:
            break
        else:
            utwory.append(utwor)

    rok_wydania = int(input('Rok wydania: '))

    return (tytul, wykonawca, utwory, rok_wydania)

def dodaj_album_do_bazy(baza, nowy_album):
    nowy_id = nowy_indeks(baza)  # stworzenie nowego indkesu dla bazy
    baza[nowy_id] = nowy_album  # dodanie nowego albumu pod indeksem nowy_id


def nowy_indeks(baza):
    if len(baza) == 0:
        return 1
    else:
        return max(baza.keys()) + 1


def usun_album_z_bazy(baza):
    wypiszAlbumy(baza)
    try:
        nrAlbumu = int(input("podaj nr albumu ktory chesz usunac:.. "))
        baza.pop(nrAlbumu,None)
    except ValueError:
        print("nie wlasciwy nr albumu")

def wypiszAlbumy(baza):
    print("Lista Albumow:")
    for key, value in baza.items():
        print(f"{key}. {value[0]}")

def wypisz_krotkie_info(baza):
    print('Liczba albumów w bazie: ', len(baza))