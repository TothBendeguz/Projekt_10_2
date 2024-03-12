from koktel import *
import random
import os
import sys
import time

os.system('cls')
def slowPrint(string, speed=0.001):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


'''
slowPrint('Üdvözöllek Rick bárjában, ahol minden korty egy kaland! Itt a koktélok varázslatos világába kalandozhatunk, és minden korty új élményeket hoz. Csípős szózat a bárpultnál, hűsítő ízek a poharadban, itt minden hangulat megtalálható. Készen állsz, hogy együtt élvezzük az ízek örömét és a jó társaságot?')


input("\n\nHa készen álasz nyomd meg az entert!")
os.system('cls')
'''

koktelok: list[Koktel] = []
alapanyagok: list[Alapanyag] = []

def main():
    beolvasas()
    print('███╗   ███╗ ██████╗      ██╗██╗████████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ███╗   ██╗███████╗███████╗███████╗')
    print('████╗ ████║██╔═══██╗     ██║██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝')
    print('██╔████╔██║██║   ██║     ██║██║   ██║   ██║   ██║    ██╔████╔██║███████║██║  ██║██╔██╗ ██║█████╗  ███████╗███████╗')
    print('██║╚██╔╝██║██║   ██║██   ██║██║   ██║   ██║   ██║    ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║')
    print('██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║   ██║   ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚████║███████╗███████║███████║')
    print('╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝   ╚═╝    ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝')
    print()                                                                                                                                                                                                                                   
    print('1 >> Koktél menü')
    print('2 >> Alapanyag menü')
    print('3 >> Kilépés')

    v = input('A választás száma: ')
    match v:
        case '1':
            return 'koktelMenu'
        case '2':
            return 'alapanyagMenu'

def beolvasas():
    f = open('koktelok.csv', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        koktelok.append(Koktel(sor))
    f.close()
    f = open('alapanyagok.csv', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        alapanyagok.append(Alapanyag(sor))
    f.close()

def koktelMenu():
    os.system('cls')
    print('███╗   ███╗ ██████╗      ██╗██╗████████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ███╗   ██╗███████╗███████╗███████╗')
    print('████╗ ████║██╔═══██╗     ██║██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝')
    print('██╔████╔██║██║   ██║     ██║██║   ██║   ██║   ██║    ██╔████╔██║███████║██║  ██║██╔██╗ ██║█████╗  ███████╗███████╗')
    print('██║╚██╔╝██║██║   ██║██   ██║██║   ██║   ██║   ██║    ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║')
    print('██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║   ██║   ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚████║███████╗███████║███████║')
    print('╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝   ╚═╝    ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝')
    print()
    print('Koktél menü')
    print(f'Jelenleg elérhető koktélok száma: {len(koktelok)}')
    print('1 >> Koktélok nevei: ')
    print('2 >> Koktélok árak: ')
    print('3 >> Kilépés')

    v = input('A választás száma: ')
    match v:
        case '1':
            os.system('cls')
            i = 1
            for koktel in koktelok:
                print(f'{i}. {koktel.nev}')
                i += 1
            input('Enter a key to continue')
            return 'koktelMenu'
        case '2':
            os.system('cls')
            i = 1
            for koktel in koktelok:
                print(f'{i}. {koktel.nev} {koktel.ar}')
                i += 1
        case '3':
            return 'pult'

def alapanyagMenu():
    pass


pult = main()
while pult != 'kilep':
    match pult:
        case 'pult':
            pult = main()
        case 'koktelMenu':
            pult = koktelMenu()
        case 'alapanyagMenu':
            pult = alapanyagMenu
