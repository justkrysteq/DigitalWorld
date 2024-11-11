# Import
from abc import ABC, abstractmethod

# Abstrakcyjna klasa Organizm
class Organizm(ABC):
    def __init__(self, sila, inicjatywa, wiek, pozycja, swiat, znak, rozmnozyc=False):
        # Podstawowe pola
        # sila: int = 0 # statystka siły
        # inicjatywa: int = 0 # statystyka inicjatywy
        # polozenie: list[int] = [0, 0] # położenie (x, y) na siatce
        # świat - referencja do świata w którym znajduje się organizm
        ...

    # Podstawowe metody
    @abstractmethod
    def akcja(self): # zachowanie organizmu w trakcie tury
        pass

    @abstractmethod
    def kolizja(self): # zachowanie organizmu w trakcie kolizji
        pass

    @abstractmethod
    def rysowanie(self): # rysowanie organizmu na siatce
        pass

    # FIXME - nazwać to jakoś idk
    def get_sila(self):
        return self.sila

    def set_sila(self, new_sila):
        self.sila = new_sila

    def get_inicjatywa(self):
        return self.inicjatywa

    def set_inicjatywa(self, new_inicjatywa):
        self.inicjatywa = new_inicjatywa

    def get_wiek(self):
        return self.wiek
  
    def set_wiek(self, new_wiek):
        self.wiek = new_wiek

    def get_pozycja(self):
        return self.pozycja

    def set_pozycja(self, new_pozycja):
        self.pozycja = new_pozycja

    def get_swiat(self):
        return self.swiat

    def set_swiat(self, new_swiat):
        self.swiat = new_swiat

    def get_znak(self):
        return self.znak

    def set_znak(self, new_znak):
        self.znak = new_znak

    def get_rozmnozyc(self):
        return self.rozmnozyc

    def set_rozmnozyc(self, new_rozmnozyc):
        self.rozmnozyc = new_rozmnozyc
