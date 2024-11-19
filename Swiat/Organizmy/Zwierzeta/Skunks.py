# Importowanie potrzebnych modułów
from Swiat.Organizmy.Zwierze import Zwierze

# Klasa dla Skunka
class Skunks(Zwierze):
    """Klasa odpowiedzialna za stworzenie Skunksa"""
    # Podstawowe statystyki
    _sila = 5
    _inicjatywa = 5

    # Ubniża inicjatywę wszyskim w około, których inicjatywa jest większa od 0 o 1 (na stałe), chyba że tyczy się to innego Skunksa
    def akcja(self, all_positions: list[list[int]], all_organizmy: list[object]):
        super().akcja(all_positions)
        available_positions = self.get_available_positions()
        for position in available_positions:
            if position is not None and position in all_positions:
                for organizm in all_organizmy:
                    if self.__class__ != organizm.__class__:
                        org_position = organizm.get_position()
                        if position == org_position:
                            if organizm.get_inicjatywa() > 0:
                                organizm.set_inicjatywa(organizm.get_inicjatywa()-1)
                                self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {self.get_position()} obniżył inicjatywę {organizm.__class__.__name__} na polu {organizm.get_position()} o 1, teraz jego inicjatywa wynosi {organizm.get_inicjatywa()}")
                            else:
                                self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {self.get_position()} nie mógł obniżyć inicjatywy {organizm.__class__.__name__}, ponieważ ta wynosi {organizm.get_inicjatywa()}")