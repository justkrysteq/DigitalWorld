from abc import ABC, abstractmethod

from Swiat.Exceptions import LanuchedModuleException

# Abstrakcyjna klasa Organizm
class Organizm(ABC):
    def __init__(self, pozycja: list[int], swiat: object, wiek: int=0, rozmnozyc: bool=False):
        # self.sila = sila # to chyba nie ma sensu tutaj, choć w pliku jest napisane, żeby było
        # self.inicjatywa = inicjatywa
        
        self.position = pozycja
        self.swiat = swiat

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

    # @abstractmethod
    # def rysowanie(self): # rysowanie organizmu na siatce
    #     pass

    # FIXME - nazwać to jakoś idk
    # def get_sila(self):
    #     return self.sila

    # def set_sila(self, new_sila):
    #     self.sila = new_sila

    def get_inicjatywa(self) -> int:
        return self.inicjatywa

    # def set_inicjatywa(self, new_inicjatywa):
    #     self.inicjatywa = new_inicjatywa

    # def get_wiek(self):
    #     return self.wiek
  
    # def set_wiek(self, new_wiek):
    #     self.wiek = new_wiek

    def get_position(self) -> list[int]:
        """
        Metoda zwracająca pozycję organizmu

        :Przykład użycia:
        >>> wilk.get_position()
        [1, 2]
        """
        return self.position

    def set_position(self, new_pozycja: list[int]):
        self.pozycja = new_pozycja

    # def get_swiat(self):
    #     return self.swiat

    # def set_swiat(self, new_swiat):
    #     self.swiat = new_swiat

    # def get_znak(self):
    #     return self.znak

    # def set_znak(self, new_znak):
    #     self.znak = new_znak

    # def get_rozmnozyc(self):
    #     return self.rozmnozyc

    # def set_rozmnozyc(self, new_rozmnozyc):
    #     self.rozmnozyc = new_rozmnozyc

if __name__ == "__main__":
    try:
        raise LanuchedModuleException("Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
    except LanuchedModuleException as e:
        print(e)