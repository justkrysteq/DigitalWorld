# try:
from abc import ABC

# from random import randint
# from Exceptions import LanuchedModuleException
from Swiat.Organizm import Organizm
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
        self.position = self.get_new_position()

    def kolizja(self, organizm: object, previous_position: list[int]) -> None:
        """
        Metoda rozstrzygająca kolizję organizmów

        :param organizm: Organizm, z którym zachodzi kolizja.
        :type organizm: object
        :param previous_position: Pozycja self przed akcją.
        :type previous_position: list[int]
        """
        print(
            f"Zaszła kolizja {self.__class__.__name__} z {organizm.__class__.__name__}"
        )
        if self.__class__ == organizm.__class__:
            pass  # TU BĘDZIE ROZMNAŻANIE
        else:
            if self.sila > organizm.get_sila():
                self.swiat.organizmy[organizm.get_position()[1]][
                    organizm.get_position()[0]
                ] = None


# rozmnażanie w ramach metody kolizja() (kolizja jest metoda w klasie Organizm) → przy kolizji z organizmem tego
# samego gatunku nie dochodzi do walki, oba zwierzęta pozostają na swoich miejscach, koło nich pojawia się trzecie
# zwierze, tego samego gatunku
