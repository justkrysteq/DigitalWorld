from Swiat.Organizmy.Zwierze import Zwierze


class Skunks(Zwierze):
    sila = 5
    inicjatywa = 5

    def akcja(self, all_positions: list[list[int]], all_organizmy: list[object]):
        super().akcja(all_positions)
        available_positions = self.get_available_positions()
        for position in available_positions:
            if position is not None and position in all_positions:
                [x, y] = position
                for organizm in all_organizmy:
                    org_position = organizm.get_position()
                    if position == org_position:
                        if organizm.get_inicjatywa() > 0:
                            organizm.set_inicjatywa(organizm.get_inicjatywa()-1)
                            print(f"{self.__class__.__name__} na polu {self.get_position()} obniżył inicjatywę {organizm.__class__.__name__} na polu {organizm.get_position()} o 1, teraz jego inicjatywa wynosi {organizm.get_inicjatywa()}")
                        else:
                            print(f"{self.__class__.__name__} na polu {self.position} nie mógł obniżyć inicjatywy {organizm.__class__.__name__}, ponieważ ta wynosi {organizm.get_inicjatywa()}")