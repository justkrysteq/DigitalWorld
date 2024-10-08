from abc import ABC, abstractmethod

class Organizm(ABC):

    sila = 0
    inicjatywa = 0
    location = [0, 0]
    # świat - referencja do świata w którym znajduje się organizm

    def akcja(self):
        pass

    def kolizja(self):
        pass

    def rysowanie(self):
        pass