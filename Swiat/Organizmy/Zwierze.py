# Importowanie potrzebnych modułów
from abc import ABC
from random import randint
from Swiat.Organizm import Organizm


# Klasa Zwierze - kontener wszystkich Zwierząt
class Zwierze(Organizm, ABC):
    """Klasa odpowiedzialna za przechowywanie wszystkich Zwierząt"""

    # Wykonanie akcji zwierzęcia
    def akcja(self, *args) -> None:
        """Metoda wykonująca akcję dla zwierzęcia"""

        if not self._omit_akcja:
            new_position = self.get_new_position()
            self._swiat._game.narratorLog(f"{self.__class__.__name__} z pola {self._position} przeszedł na pole {new_position}")
            self._position = new_position

    # Kolizja zwierzęcia
    def kolizja(self, organizm: object, previous_position: list[int], all_positions: list[list[int]]) -> None:
        """
        Metoda rozstrzygająca kolizję organizmów

        :param organizm: Organizm, z którym zachodzi kolizja.
        :type organizm: object
        :param previous_position: Pozycja self przed akcją.
        :type previous_position: list[int]
        """

        # Rozmnażanie zwierzęcia
        if self.__class__ == organizm.__class__:
            organizm._omit_akcja = True
            self._position = previous_position
            all_available_positions = []
            all_available_positions.append(self.get_available_positions())
            all_available_positions.append(organizm.get_available_positions())
            
            # Ruchy możliwe dla dziecka
            possible_for_child = []
            for list in all_available_positions:
                for position in list:
                    possible_for_child.append(position)

            # Ruchy dostępne dla dziecka
            available_for_child = []
            for position in possible_for_child:
                if position not in all_positions and position != previous_position and position != organizm._position:
                    available_for_child.append(position)

            # Małe zwierze pojawia się tylko, gdy jest na nie miejsce na świecie
            if len(available_for_child) > 0:
                choose_position = randint(0, len(available_for_child)-1)
                child = self.__class__(available_for_child[choose_position], self._swiat, omit_akcja=True)

                self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {previous_position} i {organizm.__class__.__name__} na polu {organizm._position} rozmnożyli się, tworząc {child.__class__.__name__} na polu {available_for_child[choose_position]}")
                return child
        
        # Logika kolizji z innym organizmem
        else:
            # Import potrzebnych modułów
            from Swiat.Organizmy.Rosliny.WilczeJagody import WilczeJagody
            from Swiat.Organizmy.Zwierzeta.Mysz import Mysz

            # Kolizja dla Myszy
            if organizm.__class__ == Mysz:
                # nie ma zdefiniowanej żmiji, więc nie mam jak zrobić aktualnie tej drugiej części jej kolizji
                available_positions = []
                possible_positions = organizm.get_available_positions()
                for position in possible_positions:
                    if position not in all_positions:
                        available_positions.append(position)

                # Ucieczka zwierzęcia od napastnika, jeśli jest dostępne miejsce
                if len(available_positions) > 0:
                    choose_position = randint(0, len(available_positions)-1)
                    self._swiat._game.narratorLog(f"{organizm.__class__.__name__} na polu {organizm._position} uciekła na pole {available_positions[choose_position]} od napastnika {self.__class__.__name__} nadchodzącego z pola {previous_position}")
                    organizm._position = available_positions[choose_position]
                else:
                    # Brak możliwej ucieczki od napastnika
                    self._swiat._game.narratorLog(f"{organizm.__class__.__name__} na polu {organizm._position} nie miała gdzie uciec od {self.__class__.__name__} na polu {previous_position}")
            else:
                # Zaatakowanie słabszego organizmu
                if self._sila >= organizm.get_sila():
                    # print(f"{organizm.__class__.__name__} nie powinien istnieć")
                    self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {previous_position} zjadł {organizm.__class__.__name__} na polu {organizm._position} i przeszedł na jego pole")
                    organizm._alive = False
                    # Kolizja dla Wilczych Jagód
                    if organizm.__class__ == WilczeJagody:
                        self._alive = False
                        self._swiat._game.narratorLog(f"Trucizna z {organizm.__class__.__name__} zabiła {self.__class__.__name__} na polu {self._position}")
                # Pokonanie przez mocniejszego napastnika
                elif self._sila < organizm.get_sila():
                    self._swiat._game.narratorLog(f"{self.__class__.__name__} na polu {previous_position} wszedł na pole {organizm._position}, na którym znajdował się {organizm.__class__.__name__} i zginął")
                    self._alive = False