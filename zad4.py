def main(wektor):
    iloczyn = 1
    for el in wektor:
        if el:
            iloczyn *= el

    print("iloczyn: ", iloczyn)

    if not all(wektor):
        print("warning w wektorze conajmniej raz pojawia sie wartosc zero")


if __name__ == '__main__':
    main([7, 9, 11, 27, 1])
