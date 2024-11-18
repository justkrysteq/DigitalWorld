# try:
from abc import ABC
from random import randint
from Swiat.Organizm import Organizm
# from Exceptions import LanuchedModuleException
# except ModuleNotFoundError as module:
#     if module.name != "Exceptions":
#         if __name__ == "__main__":
#             try:
#                 raise LanuchedModuleException(f"Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
#             except LanuchedModuleException as e:
#                 print(e)
#     else:
#         print("Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")


class Zwierze(Organizm, ABC):
    def akcja(self, *args):
        if not self.omit_akcja:
            new_position = self.get_new_position()
            print(f"{self.__class__.__name__} z pola {self.position} przeszedł na pole {new_position}")
            self.position = new_position

    def kolizja(self, organizm: object, previous_position: list[int], all_positions: list[list[int]]) -> None:
        """
        Metoda rozstrzygająca kolizję organizmów

        :param organizm: Organizm, z którym zachodzi kolizja.
        :type organizm: object
        :param previous_position: Pozycja self przed akcją.
        :type previous_position: list[int]
        """
        # print(f"Zaszła kolizja {self.__class__.__name__} z {organizm.__class__.__name__}")

        # Rozmnażanie
        if self.__class__ == organizm.__class__:
            organizm.omit_akcja = True
            self.position = previous_position
            all_available_positions = []
            all_available_positions.append(self.get_available_positions())
            all_available_positions.append(organizm.get_available_positions())
            possible_for_child = []
            for list in all_available_positions:
                for position in list:
                    possible_for_child.append(position)

            available_for_child = []
            for position in possible_for_child:
                if position not in all_positions and position != previous_position and position != organizm.position:
                    available_for_child.append(position)

            # Małe zwierze pojawia się tylko, gdy jest na nie miejsce na świecie
            if len(available_for_child) > 0:
                choose_position = randint(0, len(available_for_child)-1)
                # self.swiat.dodajOrganizm(self.__class__, available_for_child[choose_position])
                child = self.__class__(available_for_child[choose_position], self.swiat, omit_akcja=True)

                print(f"{self.__class__.__name__} na polu {previous_position} i {organizm.__class__.__name__} na polu {organizm.position} rozmnożyli się, tworząc {child.__class__.__name__} na polu {available_for_child[choose_position]}")
                return child
        # Kolizja
        else:
            from Swiat.Organizmy.Rosliny.WilczeJagody import WilczeJagody
            from Swiat.Organizmy.Zwierzeta.Mysz import Mysz

            if organizm.__class__ == Mysz:
                # nie ma zdefiniowanej żmiji, więc nie mam jak zrobić aktualnie tej drugiej części jej kolizji
                available_positions = []
                possible_positions = organizm.get_available_positions()
                print(all_positions)
                for position in possible_positions:
                    if position not in all_positions:
                        available_positions.append(position)
                
                print(available_positions)

                if len(available_positions) > 0:
                    choose_position = randint(0, len(available_positions)-1)
                    print(f"{organizm.__class__.__name__} na polu {organizm.position} uciekła na pole {available_positions[choose_position]} od napastnika {self.__class__.__name__} nadchodzącego z pola {previous_position}")
                    organizm.position = available_positions[choose_position]
                    print(organizm, organizm.position)
                    print(self, self.position)
                else:
                    print(f"{organizm.__class__.__name__} na polu {organizm.position} nie miała gdzie uciec od {self.__class__.__name__} na polu {previous_position}")
            else:
                if self.sila >= organizm.get_sila():
                    # print(f"{organizm.__class__.__name__} nie powinien istnieć")
                    print(f"{self.__class__.__name__} na polu {previous_position} zjadł {organizm.__class__.__name__} na polu {organizm.position} i przeszedł na jego pole")
                    organizm.alive = False
                    if organizm.__class__ == WilczeJagody:
                        self.alive = False
                        print(f"Trucizna z {organizm.__class__.__name__} zabiła {self.__class__.__name__} na polu {self.position}")
                elif self.sila < organizm.get_sila():
                    print(f"{self.__class__.__name__} na polu {previous_position} wszedł na pole {organizm.position}, na którym znajdował się {organizm.__class__.__name__} i zginął")
                    self.alive = False


# rozmnażanie w ramach metody kolizja() (kolizja jest metoda w klasie Organizm) → przy kolizji z organizmem tego
# samego gatunku nie dochodzi do walki, oba zwierzęta pozostają na swoich miejscach, koło nich pojawia się trzecie
# zwierze, tego samego gatunku


# Przynajmniej 1 klasa bazowa po której dziedziczy bezpośrednio (w tym samym pokoleniu) kilka klas pochodnych (konieczne na >=3pkt)
# Wielokrotne wykorzystanie kodu (kod w klasie bazowej używany przez obiekty klas pochodnych) (konieczne na >=3pkt)
# Nadpisywanie metody klasy bazowej wraz z wywołaniem jej w implementacji klasy pochodnej (konieczne na >=4pkt)