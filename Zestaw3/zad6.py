def main(sekwecja):
    konwersja = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    procenty = [0 for _ in range(4)]
    for nucleon in sekwecja:
        procenty[konwersja[nucleon]] += 1 / len(sekwecja)

    for i, key in enumerate(konwersja):
        print(key, procenty[i])


if __name__ == '__main__':
    main(['A', 'G', 'C'])
