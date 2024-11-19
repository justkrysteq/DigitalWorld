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

# Klasa Swiat - kontener wszystkich organizmów
class Swiat:
    """Główny kontener wszystkich organizmów"""
    # Stwórz klasę Świat zawierającą dwuwymiarową tablicę wskaźników lub referencji (w zależności od stosowanego
    # języka programowania) na obiekty klasy Organizm.

    def __init__(self, N: int, game: object):
        self.__N: int = N # Rozmiar planszy
        self._game: object = game # Objekt gry
        self._organizmy: list[list] = [[None for _ in range(N)] for _ in range(N)] # Lista wszystkich organizmów na planszy
        self.__numer_tury: int = 0 # Numer aktualnej tury
        self._current_organism_index: int = 0 # Index dla aktualnie używanego organizmu

    # Tworzenie organizmów
    def dodajOrganizm(self, organizm: object, position: list[int]):
        """Metoda odpowiedzialna za stworzenie organizmu na polu [x, y]"""
        [x, y] = position
        self._organizmy[y][x] = organizm([x, y], self)
        # print(organizm, self._organizmy[y][x].position)

    def wykonajTure(self) -> None:
        """Metoda wykonująca turę"""
        # Dodanie wszytskich organizmów do listy organizmy_by_inicjatywa i zapisanie ich pozycji
        from Swiat.Organizmy.Zwierzeta.Mysz import Mysz # Tu można dać ten customowy error
        organizmy_by_inicjatywa = self.get_organizmy_by_inicjatywa(self._organizmy)

        # Clearowanie planszy
        self._organizmy = [[None for _ in range(self.__N)] for _ in range(self.__N)]

        # Wykonanie akcji i przypisanie organizmom nowych pól na planszy
        for organizm in organizmy_by_inicjatywa:
            if organizm._alive:
                all_positions = []
                all_organizmy = []
                for organizm3 in organizmy_by_inicjatywa:
                    if organizm3 is not None:
                        all_positions.append(organizm3.get_position())
                        all_organizmy.append(organizm3)
                # print(all_positions)
                
                previous_position = organizm.get_position()
                organizm._wiek += 1
                if not organizm._omit_akcja:
                    organizm.akcja(all_positions, all_organizmy)
                new_organizmy = []

                # Kolizja
                for organizm2 in organizmy_by_inicjatywa:
                    if organizm.get_position() == organizm2.get_position() and organizm != organizm2:
                        if organizm.__class__ == organizm2.__class__:
                            new_organizmy.append(organizm.kolizja(organizm2, previous_position, all_positions))
                        elif organizm2.__class__ == Mysz:
                            new_organizmy.append(organizm.kolizja(organizm2, previous_position, all_positions))
                        else:
                            organizm.kolizja(organizm2, previous_position, all_positions)

                # Dla każdego żywego nowego organizmu stworzonego w danej turze, dodajemy go na planszę
                for new_organizm in new_organizmy:
                    if new_organizm is not None and new_organizm._alive:
                        [x, y] = new_organizm.get_position()
                        self._organizmy[y][x] = new_organizm

                # Dodanie do tabeli i aktulizacji pozycji organizmu pozycji na planszy
                [x, y] = organizm.get_position()
                self._organizmy[y][x] = organizm

            for organizm in organizmy_by_inicjatywa:
                if organizm._omit_akcja:
                    organizm._omit_akcja = False

        # Koniec tury
        self.zakonczTure()

    def następnyOrganizm(self) -> None:
        """Metoda wykonująca ruch pojedynczego organizmu"""
        # Pobierz listę organizmów posortowaną wg inicjatywy
        from Swiat.Organizmy.Zwierzeta.Mysz import Mysz
        organizmy_by_inicjatywa = self.get_organizmy_by_inicjatywa(self._organizmy)

        # Clearowanie planszy
        self._organizmy = [[None for _ in range(self.__N)] for _ in range(self.__N)]

        if not organizmy_by_inicjatywa:
            print("Brak organizmów do wykonania ruchu.")
            return

        # Akcja
        organizm = organizmy_by_inicjatywa[self._current_organism_index]
        if organizm._alive:
            all_positions = []
            all_organizmy = []
            for organizm3 in organizmy_by_inicjatywa:
                if organizm3 is not None:
                    all_positions.append(organizm3.get_position())
                    all_organizmy.append(organizm3)

            previous_position = organizm.get_position()
            organizm._wiek += 1
            if not organizm._omit_akcja:
                organizm.akcja(all_positions, all_organizmy)

            # Kolizja
            new_organizmy = []
            for organizm2 in organizmy_by_inicjatywa:
                    if organizm.get_position() == organizm2.get_position() and organizm != organizm2:
                        if organizm.__class__ == organizm2.__class__:
                            new_organizmy.append(organizm.kolizja(organizm2, previous_position, all_positions))
                        elif organizm2.__class__ == Mysz:
                            new_organizmy.append(organizm.kolizja(organizm2, previous_position, all_positions))
                        else:
                            organizm.kolizja(organizm2, previous_position, all_positions)

            # Dodanie nowych organizmów na planszę
            for new_organizm in new_organizmy:
                if new_organizm and new_organizm._alive:
                    [x, y] = new_organizm.get_position()
                    self._organizmy[y][x] = new_organizm

            # Aktualizacja pozycji organizmu na planszy
            [x, y] = organizm.get_position()
            self._organizmy[y][x] = organizm

        # Przejdź do następnego organizmu
        self._current_organism_index += 1

        for organizm in organizmy_by_inicjatywa:
            [x, y] = organizm.get_position()
            self._organizmy[y][x] = organizm

        # Jeśli osiągnięto koniec listy, zakończ turę i zresetuj indeks
        if self._current_organism_index >= len(organizmy_by_inicjatywa):
            self._current_organism_index = 0
            self.zakonczTure()

    # Sortowanie organizmów przez inicjatywę
    def get_organizmy_by_inicjatywa(self, organizmy) -> list[object]:
        """Metoda zwracająca listę posortowanych organizmów po inicjatywie, a jeśli jest równa to po sile"""
        organizmy_by_inicjatywa = []
        for y in range(len(organizmy)):
            for x in range(len(organizmy[y])):
                if organizmy[y][x] is not None:
                    organizmy[y][x].set_position([x, y])
                    organizmy_by_inicjatywa.append(organizmy[y][x])

        # Sortowanie po inicjatywie, a nastepnie po wieku jeśli inicjatywa jest równa (bąbelkowe)
        for i in range(len(organizmy_by_inicjatywa)):
            for j in range(len(organizmy_by_inicjatywa) - i - 1):
                if organizmy_by_inicjatywa[j].get_inicjatywa() < organizmy_by_inicjatywa[j+1].get_inicjatywa():
                    organizmy_by_inicjatywa[j], organizmy_by_inicjatywa[j+1] = organizmy_by_inicjatywa[j+1], organizmy_by_inicjatywa[j]
                elif organizmy_by_inicjatywa[j].get_inicjatywa() == organizmy_by_inicjatywa[j+1].get_inicjatywa():
                    if organizmy_by_inicjatywa[j].get_wiek() < organizmy_by_inicjatywa[j+1].get_wiek():
                        organizmy_by_inicjatywa[j], organizmy_by_inicjatywa[j+1] = organizmy_by_inicjatywa[j+1], organizmy_by_inicjatywa[j]

        return organizmy_by_inicjatywa

    # Koniec tury
    def zakonczTure(self):
        """Metoda wykonująca zakończenie tury"""
        
            # if organizmy_by_inicjatywa[-1].current:
            #     if organizm._alive:
            #         organizm.current = True
            #         organizmy_by_inicjatywa[-1].current = False
        self.__numer_tury += 1
        self._current_organism_index = 0

    # Pobieranie organizmów
    def get_organizmy(self) -> list[list]:
        """Metoda zwracająca logiczną reprezentację planszy"""
        return self._organizmy
    
    def set_organizmy(self, new_organizmy: list[list]) -> None:
        """
        Metoda zmieniająca logiczną reprezentację planszy

        :param new_organizmy: Nowa tabela organizmy
        :type new_organizmy: list[list]
        """
        self._organizmy = new_organizmy

    # Pobieranie organizmów
    def set_organizmy_xy(self, position: list[int], value: any) -> None:
        """
        Metoda zmieniająca logiczną reprezentację planszy na konkretnej pozycji na podaną wartość

        :param position: Pozycja na planszy
        :type position: list[int]
        :param value: Wartość na, którą zamieniamy wartość planszy
        :type value: any
        """
        [x, y] = position
        self._organizmy[y][x] = value

    # Zwracanie rozmiaru pola
    def get_N(self) -> int:
        """Metoda zwracająca rozmiar pola"""
        return self.__N


    # Pobieranie numeru tury
    def get_numer_tury(self) -> int:
        """Metoda zwracająca aktualny numer tury"""
        return self.__numer_tury

    # Wpisywanie numeru tury
    def set_numer_tury(self, new_numer_tury: int) -> None:
        """Metoda ustawiająca aktualny numer tury"""
        self.__numer_tury = new_numer_tury

# Organizmy mają możliwość wpływania na stan świata. Dlatego istnieje konieczność przekazania metodom akcja() oraz kolizja() parametru określającego obiekt klasy Świat. Postaraj się, aby klasa Świat definiowała jako publiczne składowe tylko takie pola i metody, które są potrzebne pozostałym obiektom aplikacji do działania. Pozostałą funkcjonalność świata staraj się zawrzeć w składowych prywatnych.
# Można dodać customowy error, gdy ten plik launchuje się jako __main__
