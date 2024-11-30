# Uruchom grę, jeśli wszystkie moduły są zainstalowane
try:
    # Importowanie modułów
    import pygame as pg # Sterowanie logiką gry
    import pygame_gui as gui # Sterowanie GUI gry
    from random import randint
    
    # Importowanie Świata i Organizmów
    from Swiat.Swiat import Swiat
    from Swiat.Organizmy.Zwierzeta.Wilk import Wilk
    from Swiat.Organizmy.Zwierzeta.Owca import Owca
    from Swiat.Organizmy.Zwierzeta.Lis import Lis
    from Swiat.Organizmy.Zwierzeta.Skunks import Skunks
    from Swiat.Organizmy.Zwierzeta.Mysz import Mysz
    from Swiat.Organizmy.Rosliny.Trawa import Trawa
    from Swiat.Organizmy.Rosliny.Mlecz import Mlecz
    from Swiat.Organizmy.Rosliny.WilczeJagody import WilczeJagody
    from Swiat.Exceptions import TooSmallBoardException

    # Klasa Game
    class Game:
        """Główny kontener gry"""

        def __init__(self):
            # Inicjalizacja okna Pygame
            pg.init()
            pg.display.set_caption("Wirtualny Świat - NA, KS, SW")

            # Tablica narratora
            self.__messages = []

            # Ustawienia okna
            self._screen = pg.display.set_mode((1300, 680), pg.RESIZABLE)
            self.__manager = gui.UIManager((1920, 1080))
            self.__clicked_button_position: list[int] = [0, 0]

            # Wczytanie styli
            try:
                self.__manager.get_theme().load_theme("organizmy.json")
            except Exception as e:
                print(f"Error loading theme: {e}")

            # Rysowanie siatki 20x20
            self.__N = 20
            self.__table = [[None for _ in range(self.__N)] for _ in range(self.__N)]

            # Przypisanie klasy Swiat
            self._swiat = Swiat(self.__N, self)

            # Tworzenie guzików
            bt_rectrel = pg.Rect(0, 0, 150, 60)
            bt_rectrel.topleft = (30, 30)
            self.__save_button = gui.elements.UIButton(relative_rect=bt_rectrel, text="Zapisz Świat", manager=self.__manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            bt_rectrel.topleft = (210, 30)
            self.__load_button = gui.elements.UIButton(relative_rect=bt_rectrel, text="Wczytaj Świat", manager=self.__manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            bt_rectrel.topleft = (30, 500)
            self.__next_round_button = gui.elements.UIButton(relative_rect=bt_rectrel, text="Wykonaj Turę", manager=self.__manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            bt_rectrel.topleft = (210, 500)
            self.__next_organizm_button = gui.elements.UIButton(relative_rect=bt_rectrel, text="Następny Organizm", manager=self.__manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))

        def create_panel(self) -> None:
            """Metoda tworząca panel zawierający planszę"""

            hgt = 580
            if self.__N*28+20 > 580:
                hgt = self.__N*28+20
            self._screen = pg.display.set_mode((self.__N*28+900, hgt))
            panel_plansza_relrect = pg.Rect(0, 0, self.__N*27, self.__N*27)
            panel_plansza_relrect.center = (self._screen.get_width()/2, self._screen.get_height()/2)
            self.__panel_plansza = gui.elements.UIPanel(panel_plansza_relrect, 1, self.__manager, object_id=gui.core.ObjectID(class_id="@background_panel"))
            narrator_relrect = pg.Rect(0, 0, 400, 500)
            narrator_relrect.topright = (self._screen.get_width()-30, 30)
            self.__narrator_box = gui.elements.UITextBox(relative_rect=narrator_relrect, html_text="", manager=self.__manager, object_id=gui.core.ObjectID(class_id="@narrator_box"))

            # Tworzenie panelu do dodawania organizmów
            panel_relrect = pg.Rect(0, 0, 480, 250)
            panel_relrect.center = (self._screen.get_width()/2, self._screen.get_height()/2-100)
            self.__panel = gui.elements.UIPanel(relative_rect=panel_relrect,starting_height=3, manager=self.__manager,visible=False)
            self.__panel_title = gui.elements.UILabel(relative_rect=pg.Rect(180, 0, 120, 100), text="Dodaj organizm", manager=self.__manager, container=self.__panel)
            self.__button_lis = gui.elements.UIButton(relative_rect=pg.Rect(100, 80, 50, 50), text=" ", manager=self.__manager,container=self.__panel,object_id=gui.core.ObjectID(class_id="@lis"))
            self.__button_mysz = gui.elements.UIButton(relative_rect=pg.Rect(150, 80, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@mysz"))
            self.__button_wilk = gui.elements.UIButton(relative_rect=pg.Rect(200, 80, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@wilk"))
            self.__button_owca = gui.elements.UIButton(relative_rect=pg.Rect(250, 80, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@owca"))
            self.__button_skunks = gui.elements.UIButton(relative_rect=pg.Rect(300, 80, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@skunks"))
            self.__button_trawa = gui.elements.UIButton(relative_rect=pg.Rect(100, 130, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@trawa"))
            self.__button_mlecz = gui.elements.UIButton(relative_rect=pg.Rect(150, 130, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@mlecz"))
            self.__button_wilczejagody = gui.elements.UIButton(relative_rect=pg.Rect(200, 130, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@wilcze_jagody"))
            self.__button_empty = gui.elements.UIButton(relative_rect=pg.Rect(300, 130, 50, 50), text=" ", manager=self.__manager,container=self.__panel, object_id=gui.core.ObjectID(class_id="@puste_pole"))
            self.__panel_elements = [self.__panel_title, self.__button_lis, self.__button_mysz, self.__button_wilk, self.__button_owca, self.__button_skunks, self.__button_trawa, self.__button_mlecz, self.__button_wilczejagody, self.__button_empty]

        def update_display(self) -> None:
            """Metoda odpowiedzialna za aktulizację świata na podstawie tabeli organizmy w klasie Swiat"""

            # Dictionary do przypisania odpowiednich nazw klasy stylów do klas organizmów
            class_to_name = {
                Wilk: "wilk",
                Owca: "owca",
                Lis: "lis",
                Mysz: "mysz",
                Skunks: "skunks",
                Trawa: "trawa",
                Mlecz: "mlecz",
                WilczeJagody: "wilcze_jagody",
            }

            # Wyświetlanie organizmów na podstawie tabeli dwuwymiarowej organizmów z obiektu klasy Swiat
            organizmy = self._swiat.get_organizmy()
            for y in range(len(organizmy)):
                for x in range(len(organizmy[y])):
                    if x >= self.__N or y >= self.__N:
                        try:
                            raise TooSmallBoardException("Zapis świata mógł się wczytać niepoprawnie, ponieważ wczytujesz plik z większą ilością pól niż jest na planszy, skorzystaj z ustawień i zmień jej rozmiar")
                        except TooSmallBoardException as e:
                            print(e)
                    else:
                        # Przypisanie do zmiennej class_name nazwy klasy stylu z class_to_name jeśli organizm jest instancją zawartej tam klasy
                        class_name = class_to_name.get(type(organizmy[y][x]))
                        if class_name is not None:
                            self.remove_button(x, y)
                            self.add_button(x, y, class_name)
                        else:
                            self.remove_button(x, y)
                            self.add_button(x, y, "puste_pole")
        
        # Wyświetlenie tekstu narratora
        def narratorLog(self, message: str) -> None:
            """Wypisywanie akcji organizmów w grze"""

            self.__messages.append(message)
            self.__narrator_box.set_text("\n".join(self.__messages))

        # Nowa runda
        def next_round(self) -> None:
            """Metoda wykonanie nowej rundy"""

            self._swiat.wykonajTure()
            self.update_display()

        # Zapisanie świata
        def save_world(self) -> None:
            """Metoda wykonująca zapis świata"""

            f = open("save.txt", "w")
            f.write(f"{str(self._swiat.get_N())};{str(self._swiat.get_numer_tury())};{self._swiat._current_organism_index}\n")
            for y in range(len(self._swiat.get_organizmy())):
                for x in range(len(self._swiat.get_organizmy()[y])):
                    if self._swiat.get_organizmy()[y][x] is not None:
                        f.write(f"{self._swiat.get_organizmy()[y][x].__class__.__name__};{self._swiat.get_organizmy()[y][x].get_position()};{self._swiat.get_organizmy()[y][x].get_wiek()};{self._swiat.get_organizmy()[y][x].get_alive()};{self._swiat.get_organizmy()[y][x].get_omit_akcja()}\n")
            f.close()

        # Wczytanie świata
        def load_world(self) -> None:
            """Metoda wykonująca wczytanie świata"""

            str_to_classname = {
                'Wilk': Wilk,
                'Owca': Owca,
                'Lis': Lis,
                'Mysz': Mysz,
                'Skunks': Skunks,
                'Trawa': Trawa,
                'Mlecz': Mlecz,
                'WilczeJagody': WilczeJagody,
            }

            with open("save.txt", "r") as f:
                lines = f.readlines()
                lines[0] = lines[0].split(";")
                N = int(lines[0][0])
                numer_tury = int(lines[0][1])
                current_organism_index = int(lines[0][2])
                new_organizmy = [[None for _ in range(N)] for _ in range(N)]
                for line in lines[1:]:  # Pomijamy pierwszą linię (N)
                    line = line.rstrip()
                    line = line.split(";")
                    class_name = str_to_classname.get(line[0])
                    [x, y] = eval(line[1])
                    new_organizmy[y][x] = class_name([x, y], self._swiat, int(line[2]), bool(line[3]), bool(line[4]))
            
                self._swiat.set_organizmy(new_organizmy)
                self._swiat.set_numer_tury(numer_tury)
                self._swiat._current_organism_index = current_organism_index
            f.close()
            self.update_display()

        # Wyświetlenie organizmu na planszy
        def add_button(self, x: int, y: int, classname: str, text: str = " ") -> None:
            """Metoda wykonująca wyświetlenie organizmu na polu [x, y]"""

            button_relrect = pg.Rect(0, 0, 25, 25)
            button_relrect.topleft = (self.__N/2+x*26, self.__N/2+y*26)
            self.__table[y][x] = gui.elements.UIButton(relative_rect=button_relrect, text=text, manager=self.__manager, object_id=gui.core.ObjectID(class_id=f"@{classname}"), container=self.__panel_plansza, tool_tip_text=f"Pole: [{x}, {y}]\nKliknij, aby dodać organizm.")

        # Usuwanie z planszy
        def remove_button(self, x: int, y: int) -> None:
            """Metoda wykonująca usunięcie organizmu z pola [x, y]"""
            if self.__table[y][x] is not None:
                self.__table[y][x].kill()

        # Stworzenie wszystkich organizmów
        def spawn_all(self) -> None:
            """Metoda wykonująca stworzenie wszystkich organizmów"""
            
            each_spawned_times = 2
            all_organisms = [Owca, Wilk, Lis, Mysz, Skunks, Trawa, Mlecz, WilczeJagody]
            used_positions = []
            
            for _ in range(each_spawned_times):
                for organizm in all_organisms:
                    # Wybierz losowe wolne pole, obok już aktualnie zajętego
                    position = [randint(0, self.__N-1), randint(0, self.__N-1)]
                    while position in used_positions:
                        position = [randint(0, self.__N-1), randint(0, self.__N-1)]
                    used_positions.append(position)
                    self._swiat.dodajOrganizm(organizm, position)
                    # Przykładowa zmiana ilości tworzonych organizmów
                    # if organizm == Skunks:
                    #     for _ in range(10):
                    #         position = [randint(0, self.N-1), randint(0, self.N-1)]
                            
                    #         while position in used_positions:
                    #             position = [randint(0, self.N-1), randint(0, self.N-1)]
                            
                    #         used_positions.append(position)
                    #         self._swiat.dodajOrganizm(organizm, position)

        # Nowa runda dla danego organizmu (TODO)
        def next_organizm(self) -> None:
            """Metoda wykonująca nową rundę dla danego organizmu"""

            self._swiat.następnyOrganizm()
            self.update_display()

        # Menu gry loop
        def menu(self) -> str:
            """Metoda uruchamiająca menu gry"""

            running = True
            game_state = "menu"
            clock = pg.time.Clock()

            # Tworzenie guzików do menu
            manager_menu = gui.UIManager((1920, 1080))
            
            # Guzik Graj
            button_relrect = pg.Rect(160, 350, 180, 50)
            button_relrect.centerx = self._screen.get_width()/2
            play_button = gui.elements.UIButton(relative_rect=button_relrect, text="Graj", manager=manager_menu, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            
            # Guzik Ustawienia
            button_relrect.center = (self._screen.get_width()/2, 430)
            settings_button = gui.elements.UIButton(relative_rect=button_relrect, text="Ustawienia", manager=manager_menu, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            
            # Guzik Wyjście
            button_relrect.center = (self._screen.get_width()/2, 485)
            exit_button = gui.elements.UIButton(relative_rect=button_relrect,text="Wyjście", manager=manager_menu, object_id=gui.core.ObjectID(class_id="@menu_control_button"))   
           
            # Guzik Powrót
            button_relrect.center = (self._screen.get_width()/2, 550)
            back_to_menu_button = gui.elements.UIButton(relative_rect=button_relrect,text="Powrót", manager=manager_menu, object_id=gui.core.ObjectID(class_id="@menu_control_button"),visible=False)
            
            # Pole wpisania wielkości planszy
            number_input = gui.elements.UITextEntryLine(relative_rect=pg.Rect(300, 130, 150, 50), manager=manager_menu, object_id=gui.core.ObjectID(class_id="@menu_control_button"),visible=False,initial_text="20") 

            # Menu loop
            while running:
                time_delta = clock.tick(60) / 1000.0
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                        return "quit"
                    
                    # Logika guzików w menu
                    if event.type == gui.UI_BUTTON_PRESSED:
                        # Menu
                        if game_state == "menu":
                            # Okno gry
                            if event.ui_element == play_button:
                                # print("graned")
                                running = False 
                            # Okno ustawień
                            elif event.ui_element == settings_button:
                                # print("setting settings")
                                game_state = "settings"
                                play_button.hide()
                                settings_button.hide()
                                exit_button.hide()
                                back_to_menu_button.show()
                                number_input.show()
                            # Wyjście z ustawień
                            elif event.ui_element == exit_button:
                                return "quit"
                        
                        # Powrót z ustawień
                        elif game_state == "settings":
                            if event.ui_element == back_to_menu_button:
                                game_state = "menu"
                                play_button.show()
                                settings_button.show()
                                exit_button.show()
                                back_to_menu_button.hide()
                                number_input.hide()

                    # Logika pola wpisania tekstu
                    if event.type == gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == number_input:
                        user_n_input = number_input.get_text()
                        print(user_n_input, "test")
                        if user_n_input.isdigit():
                            N_value = int(user_n_input)
                            if N_value > 5 and N_value < 30:
                                self.__N = N_value
                                self.__table = [[None for _ in range(self.__N)] for _ in range(self.__N)]
                                self._swiat = Swiat(self.__N, self)
                                print(f"Wprowadzona liczba: {user_n_input}")
                            else:
                                print("Niepoprawna liczba")
                        else:
                            number_input.set_text("")
                            print("Niepoprawna liczba")
                    manager_menu.process_events(event)

                # Wyświetlenie menu
                self._screen.fill((100, 100, 100))

                # Okno menu
                if game_state == "menu":
                    # Konfiguracja interfejsu menu
                    font = pg.font.Font(None, 54)
                    font_version = pg.font.Font(None, 36)
                    title_text = font.render("Wirtualny Świat", True, (255, 255, 255))
                    version_text = font_version.render("Version: 1.0", True, (255, 255, 255))
                    self._screen.blit(title_text, (self._screen.get_width()/2-150, 50))
                    self._screen.blit(version_text, (self._screen.get_width()/2-80, 100))

                # Okno ustawień
                elif game_state == "settings":
                    # Konfiguracja interfejsu ustawień
                    font = pg.font.Font(None, 54)
                    settings_title = font.render("Opcje", True, (255, 255 ,255))
                    settings_title_relrect = pg.Rect(self._screen.get_width()/2, 50, 200, 200)
                    settings_title_relrect.centerx = self._screen.get_width()/2 + 50
                    self._screen.blit(settings_title, settings_title_relrect)
                    font_option_n = pg.font.Font(None, 24)
                    setting_n = font_option_n.render("Podaj wielkość planszy NxN (6-29):", True, (255, 255, 255))
                    self._screen.blit(setting_n,(20, 150))

                # Rysowanie menu gry
                manager_menu.update(time_delta)
                manager_menu.draw_ui(self._screen)
                pg.display.flip()
            self.create_panel()

            return "play"

        # Wyświetlanie menu do wyboru organizmów
        def displayDodajMenu(self, x, y) -> None:
            """Metoda odpowiedzialna za wyświetlenie menu do wyboru organizmów"""

            self.__clicked_button_position = [x, y]
            if self.__panel.visible:
                self.__panel.visible = False
                for element in self.__panel_elements:
                    element.visible = False
            else:
                self.__panel.visible = True
                for element in self.__panel_elements:
                    element.visible = True
        
        def displayHideMenu(self) -> None:
            """Metoda odpowiedzialna za chowanie menu do wyboru organizmów"""

            self.__panel.visible = False
            for element in self.__panel_elements:
                element.visible = False

        # Main loop gry
        def run(self) -> None:
            """Metoda odpowiedzialna za uruchamienie gry"""

            clock = pg.time.Clock()
            running = True

            # Stwórz wszystkie organizmy
            self.spawn_all()

            # Wyświetlenie początkowego tury świata
            self.update_display()

            # Tworzenie panelu zawierającego planszę
            panel_plansza_relrect = pg.Rect(0, 0, self.__N*27, self.__N*27)
            panel_plansza_relrect.center = (self._screen.get_width()/2, self._screen.get_height()/2)
            self.__panel_plansza = gui.elements.UIPanel(panel_plansza_relrect, 1, self.__manager)

            # Pętla gry
            while running:
                time_delta = clock.tick(60) / 1000.0
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.__next_round_button:
                            self.__messages = []
                            self.narratorLog(f"Tura {self._swiat.get_numer_tury()}")
                            self.next_round()
                        elif event.ui_element == self.__save_button:
                            self.save_world()
                            self.narratorLog("Zapisano świat")
                        elif event.ui_element == self.__load_button:
                            self.load_world()
                            self.__messages = []
                            self.narratorLog("Wczytano świat")
                        elif event.ui_element == self.__next_organizm_button:
                            if self._swiat._current_organism_index == 0:
                                self.__messages = []
                                self.narratorLog(f"Tura {self._swiat.get_numer_tury()}")
                            tura_przed = self._swiat.get_numer_tury()
                            self.next_organizm()
                            if self._swiat.get_numer_tury() > tura_przed:
                                self.__messages = []
                                self.narratorLog(f"Tura {self._swiat.get_numer_tury()}")

                        # Dodawanie organizmów na plaszą poprzez panel
                        elif event.ui_element in self.__panel_elements:
                            if event.ui_element == self.__button_lis:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, Lis(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_mysz:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, Mysz(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_wilk:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, Wilk(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_owca:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, Owca(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_skunks:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, Skunks(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_trawa:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, Trawa(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_mlecz:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, Mlecz(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_wilczejagody:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, WilczeJagody(self.__clicked_button_position, self._swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.__button_empty:
                                self._swiat.set_organizmy_xy(self.__clicked_button_position, None)
                                self.update_display()
                                self.displayHideMenu()
                        else:
                            for y in range(len(self.__table)):
                                for x in range(len(self.__table[y])):
                                    if event.ui_element == self.__table[y][x]:
                                        self.displayDodajMenu(x, y)
                    self.__manager.process_events(event)
                
                # Rysowanie tła
                self.__manager.update(time_delta)
                self._screen.fill((0, 0, 0))
                self.__manager.draw_ui(self._screen)

                # Update klatki gry
                pg.display.update()

    # Uruchamianie gry
    if __name__ == "__main__":
        app = Game()
        if app.menu() == "play":
            app.run()
        pg.quit()

# Przechwytywanie wyjątku, jeśli wymagany moduł nie jest znaleziony
except ModuleNotFoundError as module:
    print(f"Upewnij się, że masz wszystkie zależności oraz pliki, dlatego że: {module}")