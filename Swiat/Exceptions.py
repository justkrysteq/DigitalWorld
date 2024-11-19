# Klasa odpowiedzialna za tworzenie wyjątków
class LanuchedModuleException(Exception):
    """
    Exception, który służy do informowaniu użytkownika o tym, że uruchomił moduł

    :Przykład użycia:
    >>> if __name__ == "__main__":
        try:
            raise LanuchedModuleException("Uruchomiono moduł, skorzystaj z pliku main.py, aby uruchomić grę")
        except LanuchedModuleException as e:
            print(e)
    """

    pass

class TooSmallBoardException(Exception):
    """
    Exception, który służy do informowaniu użytkownika o tym, że wczytuje zapis na za małej planszy

    :Przykład użycia:
    >>> if __name__ == "__main__":
        try:
            raise TooSmallBoardException("Wczytujesz plik z większą ilością pół niż jest na planszy, skorzystaj z ustawień i zmień jej rozmiar")
        except LanuchedModuleException as e:
            print(e)
    """

    pass
