from abc import ABC, abstractmethod
from Swiat.Exceptions import LanuchedModuleException


# Abstrakcyjna klasa Organizm
class Organizm(ABC):
    def __init__(
        self, pozycja: list[int], swiat: object, wiek: int = 0, rozmnozyc: bool = False
    ):
        # self.sila = sila # to chyba nie ma sensu tutaj, choć w pliku jest napisane, żeby było
        # self.inicjatywa = inicjatywa

        self.position = pozycja
        self.swiat = swiat

        # Podstawowe pola
        # sila: int = 0 # statystka siły
        # inicjatywa: int = 0 # statystyka inicjatywy
        # polozenie: list[int] = [0, 0] # położenie (x, y) na siatce
        # świat - referencja do świata w którym znajduje się organizm

    # Podstawowe metody
    @abstractmethod
    def akcja(self):
        """
        Metoda ustalająca zachowanie organizmu w trakcie tury
        """
        pass

    @abstractmethod
    def kolizja(self):
        """
        Metoda ustalająca zachowanie organizmu w trakcie kolizji
        """
        pass

    @abstractmethod
    def rysowanie(self):
        """
        Metoda powodująca narysowanie organizmu na siatce
        """
        pass

    def get_sila(self):
        """
        Metoda zwracająca siłę organizmu

        :Przykład użycia:
        >>> wilk.get_sila()
        9
        """
        return self.sila

    def set_sila(self, new_sila):
        """
        Metoda ustawiająca inicjatywę organizmu

        :Przykład użycia:
        >>> wilk.set_inicjatywa(9)
        """
        self.sila = new_sila

    def get_inicjatywa(self) -> int:
        """
        Metoda zwracająca inicjatywę organizmu

        :Przykład użycia:
        >>> wilk.get_inicjatywa()
        5
        """
        return self.inicjatywa

    def set_inicjatywa(self, new_inicjatywa):
        """
        Metoda ustawiająca inicjatywę organizmu

        :Przykład użycia:
        >>> wilk.set_inicjatywa(5)
        """
        self.inicjatywa = new_inicjatywa

    def get_wiek(self):
        """
        Metoda zwracająca wiek organizmu

        :Przykład użycia:
        >>> wilk.get_wiek()
        3
        """
        return self.wiek

    def set_wiek(self, new_wiek):
        """
        Metoda ustawiająca wiek organizmu

        :Przykład użycia:
        >>> wilk.set_wiek(5)
        """
        self.wiek = new_wiek

    def get_position(self) -> list[int]:
        """
        Metoda zwracająca pozycję organizmu

        :Przykład użycia:
        >>> wilk.get_position()
        [1, 2]
        """
        return self.position

    def set_position(self, new_pozycja: list[int]):
        """
        Metoda ustawiająca pozycję organizmu

        :Przykład użycia:
        >>> wilk.set_position(1, 2)
        """
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
        raise LanuchedModuleException(
            "Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę"
        )
    except LanuchedModuleException as e:
        print(e)
