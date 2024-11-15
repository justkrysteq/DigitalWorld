from Swiat.Exceptions import LanuchedModuleException
from Swiat.Organizmy.Zwierze import Zwierze








#  Przynajmniej 1 klasa bazowa po której dziedziczy bezpośrednio (w tym samym pokoleniu) kilka klas pochodnych (konieczne na >=3pkt)
#  Wielokrotne wykorzystanie kodu (kod w klasie bazowej używany przez obiekty klas pochodnych) (konieczne na >=3pkt)
#  Nadpisywanie metody klasy bazowej wraz z wywołaniem jej w implementacji klasy pochodnej (konieczne na >=4pkt)

if __name__ == "__main__":
    try:
        raise LanuchedModuleException("Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
    except LanuchedModuleException as e:
        print(e)