# try:
from abc import ABC
from random import randint
# from Exceptions import LanuchedModuleException
from Swiat.Organizm import Organizm
from Swiat.Organizmy.Rosliny.WilczeJagody import WilczeJagody
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
    def akcja(self):
        if not self.omit_akcja:
            self.position = self.get_new_position()

    def kolizja(self, organizm: object, previous_position: list[int]) -> None:
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
            all_available_positions = []
            all_available_positions.append(self.get_available_positions())
            all_available_positions.append(organizm.get_available_positions())
            possible_for_child = []
            for list in all_available_positions:
                for position in list:
                    possible_for_child.append(position)
            
            available_for_child = []
            all_positions = self.swiat.get_all_positions()
            for position in possible_for_child:
                if position not in all_positions:
                    available_for_child.append(position)

            # Małe zwierze pojawia się tylko, gdy jest na nie miejsce na świecie
            if len(available_for_child) > 0:
                choose_position = randint(0, len(available_for_child)-1)
                # self.swiat.dodajOrganizm(self.__class__, available_for_child[choose_position])
                child = self.__class__(available_for_child[choose_position], self.swiat)

                print(f"{self.__class__.__name__} na polu {previous_position} i {organizm.__class__.__name__} na polu {organizm.position} rozmnożyli się, tworząc {child.__class__.__name__} na polu {available_for_child[choose_position]}")
                return child
        # Kolizja
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