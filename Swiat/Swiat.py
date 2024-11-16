# try:
#     from Exceptions import LanuchedModuleException
#     from Swiat.Organizmy.Zwierzeta.Zwierzeta import Wilk, Owca, Lis, Mysz, Skunks
#     from Swiat.Organizmy.Rosliny.Mlecz import Mlecz
#     from Swiat.Organizmy.Rosliny.Trawa import Trawa
#     from Swiat.Organizmy.Rosliny.WilczeJagody import WilczeJagody
# except ModuleNotFoundError as module:
#     if __name__ == "__main__":
#         try:
#             raise LanuchedModuleException(f"Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
#         except LanuchedModuleException as e:
#             print(e)

# Klasa Swiat - kontener organizmów
class Swiat:
    # Stwórz klasę Świat zawierającą dwuwymiarową tablicę wskaźników lub referencji (w zależności od stosowanego
    # języka programowania) na obiekty klasy Organizm.

    def __init__(self, N: int):
        self.N = N
        self.organizmy = [[None for _ in range(N)] for _ in range(N)]

    def dodajOrganizm(self, organizm: object, position: list[int]):
        [x, y] = position
        self.organizmy[y][x] = organizm([x, y], self)
        print(organizm, self.organizmy[y][x].position)

    def wykonajTure(self) -> None:
        # Przypisanie każdej wartości z self.organizmy do organizmy (zrobienie kopii)
        # organizmy = [] # To add: order by inicjatywa (ewentualnie wiek)     nwm czy ta kopia self.organizmy mi jest aktualnie potrzebna wsm
        # for y in range(len(self.organizmy)):
        #     organizmy.append([])
        #     for x in range(len(self.organizmy[y])):
        #         organizmy[y].append(self.organizmy[y][x])

        organizmy_by_inicjatywa = []

        # Dodanie wsyztskich organizmów do listy organizmy_by_inicjatywa i zapisanie ich pozycji
        for y in range(len(self.organizmy)):
            # print(self.organizmy[y])
            for x in range(len(self.organizmy[y])):
                if self.organizmy[y][x] is not None:
                    self.organizmy[y][x].set_position([x, y])
                    organizmy_by_inicjatywa.append(self.organizmy[y][x])

        # Sortowanie po inicjatywie (bąbelkowe)
        for i in range(len(organizmy_by_inicjatywa)):
            for j in range(len(organizmy_by_inicjatywa) - i - 1):
                if (
                    organizmy_by_inicjatywa[j].get_inicjatywa()
                    < organizmy_by_inicjatywa[j + 1].get_inicjatywa()
                ):
                    organizmy_by_inicjatywa[j], organizmy_by_inicjatywa[j + 1] = (
                        organizmy_by_inicjatywa[j + 1],
                        organizmy_by_inicjatywa[j],
                    )

        print(organizmy_by_inicjatywa)
        # Trzeba też będzie zapisywać pozycję każdego organizmu (Done above) i potem zmieniać ją poszczególnie dla każdego obiektu organizmu w metodzie akcja (TODO), a po wykonaniu wszystkiego przypisać do self.organizmy wszystko na pusto i wczytać pozycje z każdego organizmu w tej posortowanej tabeli i dodać organizmy do poszczególnych miejsc w tabeli na podstawie tej pozycji (Done below)
        # W tym miejscu dodać sortowanie (Trzeba będzie wypisać do tablicy jednowymiarowej wszystkie organizmy i potem tą tablicę posortować po inicjatywie) (TAK ZROBIŁEM TO, NO WAY)
        # organizmy[0][0].position[1] += 1
        # organizmy[0][1] = organizmy[0][0]
        # organizmy[0][0] = None
        
        self.organizmy = [[None for _ in range(self.N)] for _ in range(self.N)]

        # for row in self.organizmy: # HALO CZEMU TO NIE DZIAŁA?
        #     for organizm in row:
        #         organizm = None
        #         print(organizm)

        for organizm in organizmy_by_inicjatywa:
            organizm.akcja()
            [x, y] = organizm.get_position()
            print(organizm, [x, y])
            self.organizmy[y][x] = organizm
        
        
        # for row in organizmy:
        #     for organizm in row:
        #         if organizm != None:
        #             print(organizm.position)
        #             organizm.akcja()  # Zaimplementuj przebieg tury, wywołując metody akcja() dla wszystkich organizmów oraz
        #         # kolizja() dla organizmów na tym samym polu. Pamiętaj, że kolejność wywoływania metody akcja() zależy od
        #         # inicjatywy (lub wieku, w przypadku równych wartości inicjatyw) organizmu.

        # Nadpisanie self.organizmy tablicą organizmy (dalej nwm czy mi to potrzebne)
        # for y in range(len(organizmy)):
        #     for x in range(len(organizmy[y])):
        #         self.organizmy[y][x] = organizmy[y][x]

        # print(self.organizmy)

    def rysujSwiat(self):
        pass

    def get_organizmy(self) -> list[list]:
        return self.organizmy
    
    def get_N(self) -> int:
        return self.N


# Organizmy mają możliwość wpływania na stan świata. Dlatego istnieje konieczność przekazania metodom akcja() oraz kolizja() parametru określającego obiekt klasy Świat. Postaraj się, aby klasa Świat definiowała jako publiczne składowe tylko takie pola i metody, które są potrzebne pozostałym obiektom aplikacji do działania. Pozostałą funkcjonalność świata staraj się zawrzeć w składowych prywatnych.
# Można dodać customowy error, gdy ten plik launchuje się jako __main__
