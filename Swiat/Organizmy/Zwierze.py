# try:
from abc import ABC
from random import randint
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
        available_positions = self.get_available_positions()
        choose_position = randint(0, len(available_positions)-1)
        self.position = available_positions[choose_position]

    def kolizja(self):
        pass

# rozmnażanie w ramach metody kolizja() (kolizja jest metoda w klasie Organizm) → przy kolizji z organizmem tego
# samego gatunku nie dochodzi do walki, oba zwierzęta pozostają na swoich miejscach, koło nich pojawia się trzecie
# zwierze, tego samego gatunku