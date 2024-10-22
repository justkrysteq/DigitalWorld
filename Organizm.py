from abc import ABC


class Organizm(ABC):
    sila: int = 0
    inicjatywa: int = 0
    polozenie: list[int] = [0, 0]

    # świat - referencja do świata w którym znajduje się organizm

    def akcja(self):
        pass

    def kolizja(self):
        pass

    def rysowanie(self):
        pass
