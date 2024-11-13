from abc import ABC
from Organizm import Organizm

class Zwierze(Organizm, ABC):
    def akcja(self):
        organizmy = self.swiat.get_organizmy().copy()
        # print(organizmy)
        # organizm = organizmy[self.position[0]][self.position[1]]
        # organizmy[self.position[0]][self.position[1]+1] = organizm
        # organizmy[self.position[0]][self.position[1]] = None
        # self.position[1]+=1

        # każde typowe zwierze w swojej turze W interfejsie aplikacji musi być przedstawione: imię,
        # nazwisko oraz numer z dziennika. przesuwa się na wybrane losowo, sąsiednie pole

    def kolizja(self):
        pass

# rozmnażanie w ramach metody kolizja() (kolizja jest metoda w klasie Organizm) → przy kolizji z organizmem tego
# samego gatunku nie dochodzi do walki, oba zwierzęta pozostają na swoich miejscach, koło nich pojawia się trzecie
# zwierze, tego samego gatunku
