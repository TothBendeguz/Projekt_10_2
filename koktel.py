class Koktel:
    def __init__(self, sor: str) -> None:
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.db = int(adatok[1])
        self.ar = int(adatok[2])

class Alapanyag:
    def __init__(self, sor: str) -> None:
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.mennyiseg = int(adatok[1])
        self.ar = int(adatok[2])