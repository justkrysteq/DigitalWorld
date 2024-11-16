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
        # print(organizm, self.organizmy[y][x].position)

    def wykonajTure(self) -> None:
        """Metoda wykonująca turę"""
        # Dodanie wszytskich organizmów do listy organizmy_by_inicjatywa i zapisanie ich pozycji
        organizmy_by_inicjatywa = []
        for y in range(len(self.organizmy)):
            for x in range(len(self.organizmy[y])):
                if self.organizmy[y][x] is not None:
                    self.organizmy[y][x].set_position([x, y])
                    organizmy_by_inicjatywa.append(self.organizmy[y][x])

        # Sortowanie po inicjatywie, a nastepnie po wieku jeśli inicjatywa jest równa (bąbelkowe)
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
                elif (
                    organizmy_by_inicjatywa[j].get_inicjatywa()
                    == organizmy_by_inicjatywa[j + 1].get_inicjatywa()
                ):
                    if (
                        organizmy_by_inicjatywa[j].get_wiek()
                        < organizmy_by_inicjatywa[j + 1].get_wiek()
                    ):
                        organizmy_by_inicjatywa[j], organizmy_by_inicjatywa[j + 1] = (
                            organizmy_by_inicjatywa[j + 1],
                            organizmy_by_inicjatywa[j],
                        )

        # Zclearowanie planszy
        self.organizmy = [[None for _ in range(self.N)] for _ in range(self.N)]

        # Wykonanie akcji i przypisanie organizmom nowych pól na planszy
        for organizm in organizmy_by_inicjatywa:
            previous_position = organizm.get_position()
            organizm.wiek += 1
            organizm.akcja()

            # Kolizja
            for organizm2 in organizmy_by_inicjatywa:
                if (
                    organizm.get_position() == organizm2.get_position()
                    and organizm != organizm2
                ):
                    organizm.kolizja(organizm2, previous_position)

            # Wyświeltanie wsm, w sensie dodanie do tabeli, z której to się wyświetla czy tam aktualzacja pozycji na planszy jakoś tak
            if organizm.alive:
                [x, y] = organizm.get_position()
                self.organizmy[y][x] = organizm

    def rysujSwiat(self):
        pass

    def get_organizmy(self) -> list[list]:
        return self.organizmy

    def get_N(self) -> int:
        return self.N


# Organizmy mają możliwość wpływania na stan świata. Dlatego istnieje konieczność przekazania metodom akcja() oraz kolizja() parametru określającego obiekt klasy Świat. Postaraj się, aby klasa Świat definiowała jako publiczne składowe tylko takie pola i metody, które są potrzebne pozostałym obiektom aplikacji do działania. Pozostałą funkcjonalność świata staraj się zawrzeć w składowych prywatnych.
# Można dodać customowy error, gdy ten plik launchuje się jako __main__
