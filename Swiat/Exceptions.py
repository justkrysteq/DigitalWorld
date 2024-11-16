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
