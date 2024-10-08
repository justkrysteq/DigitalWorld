from abc import ABC, abstractmethod
import Organizm

class Zwierze(ABC, Organizm):

    def akacja(self):
        pass

# rozmnażanie w ramach metody kolizja() (kolizja jest metoda w klasie Organizm) → przy kolizji z organizmem tego samego gatunku
# nie dochodzi do walki, oba zwierzęta pozostają na swoich miejscach, koło nich pojawia się
# trzecie zwierze, tego samego gatunku