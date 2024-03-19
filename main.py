from koktel import *
import random
import os
import sys
import time
from time import sleep
from rich.progress import track
from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table

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

koktelok: list[Koktel] = []
alapanyagok: list[Alapanyag] = []
beolvasas()
for szam in track(range(10)):
    sleep(0.25)
input('Enter a key to continue')


def main():
    os.system('cls')
    print('███╗   ███╗ ██████╗      ██╗██╗████████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ███╗   ██╗███████╗███████╗███████╗')
    print('████╗ ████║██╔═══██╗     ██║██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝')
    print('██╔████╔██║██║   ██║     ██║██║   ██║   ██║   ██║    ██╔████╔██║███████║██║  ██║██╔██╗ ██║█████╗  ███████╗███████╗')
    print('██║╚██╔╝██║██║   ██║██   ██║██║   ██║   ██║   ██║    ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║')
    print('██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║   ██║   ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚████║███████╗███████║███████║')
    print('╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝   ╚═╝    ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝')
    print()                                                                                                                                                                                                                                   
    print('1 >> Koktél menü')
    print('2 >> Alapanyag menü')
    print('3 >> Eladás/Beszerzés menü')
    print('4 >> Keverés menü')
    print('5 >> Kilépés')

    v = input('A választás száma: ')
    match v:
        case '1':
            return 'koktelMenu'
        case '2':
            return 'alapanyagMenu'
        case '3':
            return 'eladasBeszerzesMenu'
        case '4':
            return 'keveresMenu'
        case '5':
            return 'kilep'



def koktelMenu():
    os.system('cls')
    print('███╗   ███╗ ██████╗      ██╗██╗████████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ███╗   ██╗███████╗███████╗███████╗')
    print('████╗ ████║██╔═══██╗     ██║██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝')
    print('██╔████╔██║██║   ██║     ██║██║   ██║   ██║   ██║    ██╔████╔██║███████║██║  ██║██╔██╗ ██║█████╗  ███████╗███████╗')
    print('██║╚██╔╝██║██║   ██║██   ██║██║   ██║   ██║   ██║    ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║')
    print('██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║   ██║   ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚████║███████╗███████║███████║')
    print('╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝   ╚═╝    ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝')
    print()
    '''
    MARKDOWN = """
    # Koktél menü

    1. >> Koktélok nevei
    2. >> Koktélok árak
    3. >> Kilépés
    """
    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)
    '''
    print(f'Jelenleg elérhető koktélok száma: {len(koktelok)}')
    print('1 >> Koktélok nevei: ')
    print('2 >> Koktélok árak: ')
    print('3 >> Kilépés')

    v = input('A választás száma: ')
    match v:
        case '1':
            os.system('cls')
            console = Console()

            table = Table(title="Koktél menü")
            table.add_column("Név", style="cyan", justify="center")
            table.add_column("Elérhető mennyiség", style="yellow", justify="right")

            for koktel in koktelok:
                table.add_row(
                    koktel.nev,
                    str(koktel.db),
                )

            console.print(table)
            input('Enter a key to continue')
            return 'koktelMenu'
        case '2':
            os.system('cls')
            console = Console()

            table = Table(title="Koktél menü")
            table.add_column("Név", style="cyan", justify="center")
            table.add_column("Elérhető mennyiség", style="yellow", justify="right")
            table.add_column("Ár", style="green", justify="right")

            for koktel in koktelok:
                table.add_row(
                    koktel.nev,
                    str(koktel.db),
                    str(koktel.ar),
                )

            console.print(table)
            input('Enter a key to continue')
            return 'koktelMenu'
        case '3':
            return 'pult'

def alapanyagMenu():
    os.system('cls')
    print('███╗   ███╗ ██████╗      ██╗██╗████████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ███╗   ██╗███████╗███████╗███████╗')
    print('████╗ ████║██╔═══██╗     ██║██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝')
    print('██╔████╔██║██║   ██║     ██║██║   ██║   ██║   ██║    ██╔████╔██║███████║██║  ██║██╔██╗ ██║█████╗  ███████╗███████╗')
    print('██║╚██╔╝██║██║   ██║██   ██║██║   ██║   ██║   ██║    ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║')
    print('██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║   ██║   ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚████║███████╗███████║███████║')
    print('╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝   ╚═╝    ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝')
    print()
    print('alapanyag menü')
    print(f'Jelenleg elérhető alapanyagok száma: {len(alapanyagok)}')
    print('1 >> Alapanyagok nevei: ')
    print('2 >> Alapanyagokból elérhető mennyiség: ')
    print('3 >> Hiányzó alapanyagok: ')
    print('4 >> Kilépés')

    v = input('A választás száma: ')
    match v:
        case '1':
            os.system('cls')
            console = Console()

            table = Table(title="Alapanyag menü")
            table.add_column("Név", style="cyan", justify="center")

            for alapanyag in alapanyagok:
                table.add_row(
                    alapanyag.nev,
                )

            console.print(table)
            input('Enter a key to continue')
            return 'alapanyagMenu'
        case '2':
            os.system('cls')
            console = Console()

            table = Table(title="Alapanyag menü")
            table.add_column("Név", style="cyan", justify="center")
            table.add_column("Mennyiség", style="cyan", justify="center")

            for alapanyag in alapanyagok:
                table.add_row(
                    alapanyag.nev,
                    str(alapanyag.mennyiseg),
                )

            console.print(table)
            input('Enter a key to continue')
            return 'alapanyagMenu'
        case '3':
            os.system('cls')
            i = 1
            for alapanyag in alapanyagok:
                i += 1
                if alapanyag.mennyiseg == 0:
                    print(f'{i}. {alapanyag.nev} - {alapanyag.mennyiseg} mennyiség')
            input('Enter a key to continue')
            return 'alapanyagMenu'
        case '4':
            return 'pult'
        
def eladasBeszerzesMenu():
    pass

def koktelKeverese(koktel: int):
    match koktel:
        case 1:
            pass
        case 2:
            pass
        
def keveresMenu():
    os.system('cls')
    print('███╗   ███╗ ██████╗      ██╗██╗████████╗ ██████╗     ███╗   ███╗ █████╗ ██████╗ ███╗   ██╗███████╗███████╗███████╗')
    print('████╗ ████║██╔═══██╗     ██║██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝')
    print('██╔████╔██║██║   ██║     ██║██║   ██║   ██║   ██║    ██╔████╔██║███████║██║  ██║██╔██╗ ██║█████╗  ███████╗███████╗')
    print('██║╚██╔╝██║██║   ██║██   ██║██║   ██║   ██║   ██║    ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║')
    print('██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║   ██║   ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚████║███████╗███████║███████║')
    print('╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝   ╚═╝    ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝')
    print()
    print('Keverés menü')
    print('1 >> Készlethiányos koktélok: ')
    print('2 >> Koktél keverése: ')
    print('3 >> Hiányzó alapanyagok: ')
    print('4 >> Kilépés')

    v = input('A választás száma: ')
    match v:
        case '1':
            os.system('cls')
            van = False
            console = Console()

            table = Table(title="Készlethiányos koktélok")
            table.add_column("Név", style="cyan", justify="center")
            table.add_column("Elérhető mennyiség", style="yellow", justify="right")

            for koktel in koktelok:
                if koktel.db < 1:
                    van = True
                    table.add_row(
                        koktel.nev,
                        str(koktel.db),
                    )
            if van == True:
                console.print(table)
            else:
                print('Nincsenek készlethiányos koktelok')
            input('Enter a key to continue')
            return 'keveresMenu'
        case '2':
            os.system('cls')
            v = ''
            while v == '':
                v = input('Melyik koktélt szertnéd keverni? (Ha nem tudod a számot írd be, hogy "segitseg"): ')
            match v:
                case 'segitseg':
                    os.system('cls')
                    console = Console()

                    table = Table(title="Koktélok")
                    table.add_column("Név", style="cyan", justify="center")
                    table.add_column("Elérhető mennyiség", style="yellow", justify="right")

                    for koktel in koktelok:
                        table.add_row(
                            koktel.nev,
                            str(koktel.db),
                        )

                    console.print(table)
                    v2 = input('Melyik koktélt szertnéd keverni?: ')
                    koktelKeverese(int(v2))
                case _:
                    koktelKeverese(int(v))


pult = main()
while pult != 'kilep':
    match pult:
        case 'pult':
            pult = main()
        case 'koktelMenu':
            pult = koktelMenu()
        case 'alapanyagMenu':
            pult = alapanyagMenu()
        case 'eladasBeszerzesMenu':
            pult = eladasBeszerzesMenu()
        case 'keveresMenu':
            pult = keveresMenu()
