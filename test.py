from koktel import *

koktelok: list[Koktel] = []
alapanyagok: list[Alapanyag] = []

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

from rich.console import Console
from rich.table import Table

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