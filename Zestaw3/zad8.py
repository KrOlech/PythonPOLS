def main(sekwecja, tablicaposzukiwan):
    poszukiwaneIndeksy = []

    for i in range(len(tablicaposzukiwan) - len(sekwecja)):

        if sekwecja == tablicaposzukiwan[i:i + len(sekwecja)]:
            poszukiwaneIndeksy.append(i)

    return poszukiwaneIndeksy


if __name__ == '__main__':
    print(main([1, 2,3], [1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 1, 4, 3, 4, 5,4 ,1, 2, 3, 4]))
