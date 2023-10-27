import math


def feladat_1():
    i = 0
    while i < 150:
        if i % 2 == 0:
            print(i, end=";")
        i += 2
    print(i, end=" ")


def feladat_2():
    osztharom = 0
    sorszam = 1
    while sorszam <= 10:
        szam = int(input("Kérek számot a "+str(sorszam)+". számot: "))
        if szam % 3 == 0:
            osztharom += 1
        sorszam += 1
    print(" A bekért számok alapján "+str(osztharom) + " olyan szám található amely osztható 3-mal.")


def feladat_3():
    n = int(input("Kérek egy számot: "))
    while not (n % 10 == 0):
        n = int(input("Hibás szám! Kérek még egy számot: "))
    print("Ön nyert egy Gucci táskát!.")


def feladat_4():
    n = int(input("Kétjegyű, páros szám: "))
    while not (n % 2 == 0 and (100 > n > 9 or -100 < -9)):
        n = int(input("Hibás szám! Kétjegyű páros szám: "))
    print("Ön nyert egy Gucci táskát!.")


def feladat_5():
    n = int(input("Páratlan szám: "))
    while not ((n > 0) and (n % 2 == 1)):
        n = int(input("Hibás szám! Páratlan szám: "))
    print("Ön nyert egy Gucci táskát!.")


def feladat_6():
    n = int(input("3-mal osztható szám vagy négyzet szám: "))
    while not ((n % 3 == 0) or (math.sqrt(n).is_integer())):
        n = int(input("Hibás szám! 3-mal osztható vagy négyzetszám: "))
    print("Ön nyert egy Gucci táskát!.")


def feladat_7():
    a = float(input("Kérek adjon egy valós számot: "))
    b = float(input("Kérek adjon egy valós számot: "))
    c = float(input("Kérek adjon egy valós számot: "))
    if (a < b+c) and (b < a+c) and (c > a+b):
        print("A három szerkezthető")
    else:
        print("Nem szerkezthető")


def feladat_8():
    szoveg = input("kérek be egy szöveget: ")
    while not (len(szoveg) >= 3 and szoveg.islower()):
        szoveg = int(input("Hibás szöveg! 3 karakteres szöveget kérek: "))
    print(szoveg.upper())
    print("Ön nyert egy Gucci táskát!.")


def feladat_9():
    szoveg = input("kérek be egy szöveget: ")
    while not (len(szoveg) >= 4 and szoveg.islower()):
        szoveg = input("Hibás szöveg! 4 karakteres szöveget kérek: ")
    print(szoveg.islower())
