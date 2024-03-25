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
    print('3 >> Vissza')

    v = input('A választás száma: ')
    match v:
        case '1':
            os.system('cls')
            console = Console()

            table = Table(title="Koktél menü")
            table.add_column("Szám", style="red", justify="center")
            table.add_column("Név", style="cyan", justify="center")
            table.add_column("Elérhető mennyiség", style="yellow", justify="right")
            i = 1
            for koktel in koktelok:
                table.add_row(
                    str(i),
                    koktel.nev,
                    str(koktel.db),
                )
                i += 1

            console.print(table)
            input('Enter a key to continue')
            return 'koktelMenu'
        case '2':
            os.system('cls')
            console = Console()

            table = Table(title="Koktél menü")
            table.add_column("Szám", style="red", justify="center")
            table.add_column("Név", style="cyan", justify="center")
            table.add_column("Elérhető mennyiség", style="yellow", justify="right")
            table.add_column("Ár", style="green", justify="right")
            i = 1
            for koktel in koktelok:
                table.add_row(
                    str(i),
                    koktel.nev,
                    str(koktel.db),
                    str(koktel.ar),
                )
                i += 1

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
    print('Alapanyag menü')
    print(f'Jelenleg elérhető alapanyagok száma: {len(alapanyagok)}')
    print('1 >> Alapanyagok nevei: ')
    print('2 >> Alapanyagokból elérhető mennyiség: ')
    print('3 >> Hiányzó alapanyagok: ')
    print('4 >> Vissza')

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
            table.add_column("Mennyiség", style="yellow", justify="right")

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

#-----------------------------------------------------------------------------------------------------------------

def beolvas_receptek():
    receptek = {}
    with open('receptek.txt', 'r', encoding='utf-8') as f:
        for line in f:
            ingredients, cocktail_name = line.strip().split(' - ')
            ingredients = [ingredient.strip() for ingredient in ingredients.split(',')]
            receptek[cocktail_name] = ingredients
    return receptek

receptek = beolvas_receptek()

def koktelKeverese(koktel: int):
    global alapanyagok
    global koktelok

    # Koktél kiválasztása az index alapján
    koktel = koktelok[koktel - 1]  

    ingredients_needed = receptek[koktel.nev]  # A koktélhoz szükséges alapanyagok
    for ingredient in ingredients_needed:
        found = False
        for i, alapanyag in enumerate(alapanyagok):
            if alapanyag.nev.lower() == ingredient.lower():
                found = True
                # Módosítás az alapanyag mennyiségénél
                alapanyag.mennyiseg -= 1  # Alapanyag mennyiségének csökkentése
                break
        if not found:
            print(f"A(z) {koktel.nev} koktélhoz hiányzik {ingredient}!")

    # Alapanyagok.csv frissítése
    with open('alapanyagokuj.csv', 'w', encoding='utf-8') as f:
        f.write("alapanyag neve;elérhető mennyiség\n")
        for alapanyag in alapanyagok:
            f.write(f"{alapanyag.nev};{alapanyag.mennyiseg}\n")

    # Koktelok.csv frissítése
    with open('koktelokuj.csv', 'w', encoding='utf-8') as f:
        f.write("név;darab raktáron;ár\n")
        for k in koktelok:
            if k.nev == koktel.nev:
                k.db += 1  # A kevert koktél darabszámának növelése
            f.write(f"{k.nev};{k.db};{k.ar}\n")

    for szam in track(range(10)):
        sleep(0.5)

    input('Nyomj Enter-t a folytatáshoz...')
    return 'keveresMenu'


#-----------------------------------------------------------------------------------------------------------------

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

                    table = Table(title="Koktél menü")
                    table.add_column("Szám", style="red", justify="center")
                    table.add_column("Név", style="cyan", justify="center")
                    table.add_column("Elérhető mennyiség", style="yellow", justify="right")
                    i = 1
                    for koktel in koktelok:
                        table.add_row(
                            str(i),
                            koktel.nev,
                            str(koktel.db),
                        )
                        i += 1

                    console.print(table)
                    v2 = input('Melyik koktélt szertnéd keverni?: ')
                    return koktelKeverese(int(v2))
                case _:
                    return koktelKeverese(int(v))


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
