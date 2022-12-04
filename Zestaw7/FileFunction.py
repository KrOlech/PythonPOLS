import pickle
from os import walk, curdir

def zapisz_do_pliku(baza,fileName):
    pickle.dump(baza, open(fileName, 'wb'))


def zaladu_z_pliku(fileName):
    try:
        print(f"Próba odczytu bazy danych ({fileName})")
        print(f"Zaladowano baze danych z pliku {fileName}")
        return pickle.load(open(fileName, 'rb'))
    except FileNotFoundError:
        print(f"Brak pliku z bazy danych ({fileName})")
        return {}

def zaladuj_z_pliku_fileName():
    filenames = next(walk(curdir), (None, None, []))[2]
    i = 0
    map = {}
    for nr,file in enumerate(filenames):
        if file[-5:] == '.base':
            print(f"{i}. {file}")
            i+=1
            map[i] = nr

    try:
        return zaladu_z_pliku(map[int(input("podaj nr pliku ktory chcesz otrozyc"))])
    except ValueError:
        print("Unsuportet value for file")
        return zaladuj_z_pliku_fileName()


def zapisz_do_pliku_fileName(baza):
    fileName = input("podaj nazwe bazy")
    zapisz_do_pliku(baza,fileName+'.base')
