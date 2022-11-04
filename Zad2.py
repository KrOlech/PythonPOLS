from inspect import signature


def ciongA(wyrazPoprzedni):
    return 2 * wyrazPoprzedni,


def ciagB(wyrazPoprzedni, wyrazPoprzedniejszy):
    return (wyrazPoprzedni + wyrazPoprzedniejszy) / 2, wyrazPoprzedni


def touple(param):
    pass


def main(N=10, ciag=ciongA, wartościPoczatkowe=None, zapis=False):
    if wartościPoczatkowe == None:
        wartościPoczatkowe = [_ for _ in range(len(signature(ciag).parameters))]
    print(wartościPoczatkowe)

    tab = []

    if zapis:
        try:
            [tab.append(wartosc) for wartosc in wartościPoczatkowe]
        except TypeError:
            tab.append(wartościPoczatkowe)

    for _ in range(N):
        wartościPoczatkowe = ciag(*wartościPoczatkowe)
        print(wartościPoczatkowe[0])

        if zapis:
            tab.append(wartościPoczatkowe[0])

    if zapis:
        print(tab)


if __name__ == '__main__':
    main(ciag=ciagB, zapis=True)
