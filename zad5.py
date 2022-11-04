def main(sekwecja):
    odczyt = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    [print(nucleon,' ',odczyt[nucleon]) for nucleon in sekwecja]


if __name__ == '__main__':
    main(['A','G','C'])
