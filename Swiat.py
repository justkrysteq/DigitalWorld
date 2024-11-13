from Zwierzeta import Wilk, Owca, Lis, Mysz, Skunks
from Rosliny import Mlecz, Trawa, WilczeJagody

# Klasa Swiat - kontener organizmów
class Swiat:
    # Stwórz klasę Świat zawierającą dwuwymiarową tablicę wskaźników lub referencji (w zależności od stosowanego
    # języka programowania) na obiekty klasy Organizm.

    def __init__(self, N: int):
        self.organizmy = [[None for _ in range(N)] for _ in range(N)]

    def dodajOrganizm(self, organizm: object, x: int, y: int):
        self.organizmy[x][y] = organizm([x, y], self)
        print(organizm, self.organizmy[x][y].position)

    def wykonajTure(self):
        organizmy = self.organizmy.copy()  # To add: order by inicjatywa (ewentualnie wiek)
        # W tym miejscu dodać sortowanie (Trzeba będzie wypisać do tablicy jednowymiarowej wszystkie organizmy i potem tą tablicę posortować po inicjatywie)
        # organizmy[0][0].position[1] += 1
        organizmy[0][1] = organizmy[0][0]
        organizmy[0][0] = None
        for row in organizmy:
            for organizm in row:
                if organizm != None:
                    print(organizm.position)
                    organizm.akcja()  # Zaimplementuj przebieg tury, wywołując metody akcja() dla wszystkich organizmów oraz
                # kolizja() dla organizmów na tym samym polu. Pamiętaj, że kolejność wywoływania metody akcja() zależy od
                # inicjatywy (lub wieku, w przypadku równych wartości inicjatyw) organizmu.

    def rysujSwiat(self):
        pass

    def get_organizmy(self):
        return self.organizmy


# Organizmy mają możliwość wpływania na stan świata. Dlatego istnieje konieczność przekazania metodom akcja() oraz kolizja() parametru określającego obiekt klasy Świat. Postaraj się, aby klasa Świat definiowała jako publiczne składowe tylko takie pola i metody, które są potrzebne pozostałym obiektom aplikacji do działania. Pozostałą funkcjonalność świata staraj się zawrzeć w składowych prywatnych.


# Można dodać customowy error, gdy launchuje się ten plik jako __main__