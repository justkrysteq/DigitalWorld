# Import
# import pygame as pg
# import pygame_gui as gui
# from random import randint
from Zwierzeta import Wilk, Owca, Lis, Mysz, Skunks
from Rosliny import Mlecz, Trawa, WilczeJagody

# Klasa Swiat - kontener organizmów
class Swiat:
    # Stwórz klasę Świat zawierającą dwuwymiarową tablicę wskaźników lub referencji (w zależności od stosowanego
    # języka programowania) na obiekty klasy Organizm.

    def __init__(self, N: int):
        self.organizmy = [[None for _ in range(N)] for _ in range(N)]
        

    def wykonajTure(self):
        organizmy = self.organizmy  # order by inicjatywa (ewentualnie wiek)
        for organizm in organizmy:
            organizm.akcja()  # Zaimplementuj przebieg tury, wywołując metody akcja() dla wszystkich organizmów oraz
            # kolizja() dla organizmów na tym samym polu. Pamiętaj, że kolejność wywoływania metody akcja() zależy od
            # inicjatywy (lub wieku, w przypadku równych wartości inicjatyw) organizmu.

    def rysujSwiat(self):
        pass


# Organizmy mają możliwość wpływania na stan świata. Dlatego istnieje konieczność przekazania metodom akcja() oraz kolizja() parametru określającego obiekt klasy Świat. Postaraj się, aby klasa Świat definiowała jako publiczne składowe tylko takie pola i metody, które są potrzebne pozostałym obiektom aplikacji do działania. Pozostałą funkcjonalność świata staraj się zawrzeć w składowych prywatnych.