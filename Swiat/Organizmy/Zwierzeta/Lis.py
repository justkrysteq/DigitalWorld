from Swiat.Organizmy.Zwierze import Zwierze
from random import randint


class Lis(Zwierze):
    sila = 3
    inicjatywa = 7

    # Zależy jak jest zgodnie z najlepszymi praktykami programowania obiektowego

    # def __init__(self, pozycja, swiat, wiek = 0, alive = True, rozmnozyc = False):
    #     super().__init__(pozycja, swiat, wiek, alive, rozmnozyc)
    #     self.sila = 3
    #     self.inicjatywa = 7

    def akcja(self, all_positions: list[list[int]], *args):
        if not self.omit_akcja:
            available_positions = [] # tu będą pozycje na których nie ma organizmu z większą siłą od lisa (czyli puste lub z mniejszą siłą)
            possible_positions = self.get_available_positions() # tu są wszystkie ruchy jakie mógłby wykonać
            for position in possible_positions:
                if position in all_positions and position is not None:
                    [x, y] = position
                    organizm = self.swiat.organizmy[y][x]
                    # Sprawdzanie czy organizm na tej pozycji na większą siłę niż lis, jeśli tak to się tam nie ruszy
                    if organizm is not None and self.sila >= organizm.sila:
                        available_positions.append(position)
                else:
                    available_positions.append(position)

            if len(available_positions) > 0:
                choose_position = randint(0, len(available_positions)-1)
                print(f"{self.__class__.__name__} na polu {self.position} przeszedł na pole {available_positions[choose_position]}, unikając ewentualnego zagrożenia")
                self.position = available_positions[choose_position]
        
        # jesli pole na ktore chce sie ruszyc zawiera organizm z wieksza sila to tam nie wejdzie
