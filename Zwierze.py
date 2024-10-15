from abc import ABC, abstractmethod
import Organizm

class Zwierze(ABC, Organizm):

    def akcja(self):
        pass # każde typowe zwierze w swojej turze W interfejsie aplikacji musi być przedstawione: imię, nazwisko oraz numer z dziennika. przesuwa się na wybrane losowo, sąsiednie pole 

    def kolizja(self):
        pass
# rozmnażanie w ramach metody kolizja() (kolizja jest metoda w klasie Organizm) → przy kolizji z organizmem tego samego gatunku
# nie dochodzi do walki, oba zwierzęta pozostają na swoich miejscach, koło nich pojawia się
# trzecie zwierze, tego samego gatunku