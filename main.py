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

    # Klasa Game
    class Game:
        """Główny kontener gry"""
        def __init__(self):
            # Inicjalizacja okna Pygame
            pg.init()
            pg.display.set_caption("Wirtualny Świat - NA, KS, SW")
            # Tablica narratora
            self.messages = [] 
            # Ustawienia okna
            self.screen = pg.display.set_mode((825, 680))
            self.manager = gui.UIManager((825, 680))
            self.narrator_box = gui.elements.UITextBox(relative_rect=pg.Rect(540,20,260,500),html_text="" ,manager=self.manager,object_id=gui.core.ObjectID(class_id="@narrator_box"))
            self.clicked_button_position: list[int] = [0, 0]

            # Wczytanie styli
            try:
                self.manager.get_theme().load_theme("organizmy.json")
            except Exception as e:
                print(f"Error loading theme: {e}")

            # Rysowanie siatki 20x20
            self.N = 20
            self.table = [[None for _ in range(self.N)] for _ in range(self.N)]

            # Przypisanie klasy Swiat
            self.swiat = Swiat(self.N, self)

            # Tworzenie guzików
            self.next_round_button = gui.elements.UIButton(relative_rect=pg.Rect(10, 530, 150, 60), text="Wykonaj Turę", manager=self.manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            self.next_organizm_button = gui.elements.UIButton(relative_rect=pg.Rect(10, 600, 150, 60), text="Następny Organizm", manager=self.manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            self.save_button = gui.elements.UIButton(relative_rect=pg.Rect(185, 530, 150, 60), text="Zapisz Świat", manager=self.manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            self.load_button = gui.elements.UIButton(relative_rect=pg.Rect(355, 530, 150, 60), text="Wczytaj Świat", manager=self.manager, object_id=gui.core.ObjectID(class_id="@menu_control_button"))

            # Tworzenie panelu
            self.panel = gui.elements.UIPanel(relative_rect=pg.Rect(20, 20, 480, 250),starting_height=3, manager=self.manager,visible=False)
            self.panel_title = gui.elements.UILabel(relative_rect=pg.Rect(10, 10, 100, 100), text="Dodaj organizm", manager=self.manager, container=self.panel)
            self.button_lis = gui.elements.UIButton(relative_rect=pg.Rect(50, 50, 50, 50), text=" ", manager=self.manager,container=self.panel,object_id=gui.core.ObjectID(class_id="@lis"))
            self.button_mysz = gui.elements.UIButton(relative_rect=pg.Rect(100, 50, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@mysz"))
            self.button_wilk = gui.elements.UIButton(relative_rect=pg.Rect(150, 50, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@wilk"))
            self.button_owca = gui.elements.UIButton(relative_rect=pg.Rect(200, 50, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@owca"))
            self.button_skunks = gui.elements.UIButton(relative_rect=pg.Rect(250, 50, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@skunks"))
            self.button_trawa = gui.elements.UIButton(relative_rect=pg.Rect(50, 100, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@trawa"))
            self.button_mlecz = gui.elements.UIButton(relative_rect=pg.Rect(100, 100, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@mlecz"))
            self.button_wilczejagody = gui.elements.UIButton(relative_rect=pg.Rect(150, 100, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@wilcze_jagody"))
            self.button_empty = gui.elements.UIButton(relative_rect=pg.Rect(200, 100, 50, 50), text=" ", manager=self.manager,container=self.panel, object_id=gui.core.ObjectID(class_id="@puste_pole"))
            # self.button_dodaj = gui.elements.UIButton(relative_rect=pg.Rect(300, 100, 50, 50), text="Dodaj", manager=self.manager,container=self.panel)
            # self.button_anuluj = gui.elements.UIButton(relative_rect=pg.Rect(350, 100, 50, 50), text="Anuluj", manager=self.manager,container=self.panel)
            self.panel_elements = [self.panel_title, self.button_lis, self.button_mysz, self.button_wilk, self.button_owca, self.button_skunks, self.button_trawa, self.button_mlecz, self.button_wilczejagody, self.button_empty] #, self.button_dodaj, self.button_anuluj

        def update_display(self):
            """Metoda odpowiedzialna za aktulizację świata z każdą turą """
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
            organizmy = self.swiat.get_organizmy()
            for y in range(len(organizmy)):
                for x in range(len(organizmy[y])):
                    # print("X:", organizmX, "Y:", organizmY)
                    # Przypisanie do zmiennej class_name nazwy klasy stylu z class_to_name jeśli organizm jest instancją zawartej tam klasy
                    class_name = class_to_name.get(type(organizmy[y][x]))
                    if class_name is not None:
                        # print(class_name)
                        self.remove_button(x, y)
                        self.add_button(x, y, class_name)
                    else:
                        self.remove_button(x, y) # FIXME
                        self.add_button(x, y, "puste_pole")
        
        # Wyświetlenie tekstu narratora
        def narratorLog(self, message: str):
            """Wypisywanie akcji organizmów w grze"""
            self.messages.append(message)
            self.narrator_box.set_text("\n".join(self.messages))

        # Nowa runda
        def next_round(self):
            """Metoda wykonanie nowej rundy"""
            self.swiat.wykonajTure()
            self.update_display()

        # Zapisanie świata (TODO!!!)
        def save_world(self):
            """Metoda wykonująca zapis świata"""
            pass

        # Wczytanie świata (TODO!!!)
        def load_world(self):
            """Metoda wykonująca wczytanie świata"""
            pass

        # Wyświetlenie organizmu na planszy
        def add_button(self, x: int, y: int, classname: str, text: str = " "):
            """Metoda wykonująca wyświetlenie organizmu na polu [x, y]"""
            self.table[y][x] = gui.elements.UIButton(relative_rect=pg.Rect(x * 26, y * 26, 25, 25), text=text, manager=self.manager, object_id=gui.core.ObjectID(class_id=f"@{classname}"))

        # Usuwanie z planszy
        def remove_button(self, x: int, y: int):
            """Metoda wykonująca usunięcie organizmu z pola [x, y]"""
            if self.table[y][x] is not None:
                self.table[y][x].kill()
            # self.table[y][x] = gui.elements.UIButton(relative_rect=pg.Rect(x * 26, y * 26, 25, 25), text=" ", manager=self.manager, object_id=gui.core.ObjectID(class_id="@puste_pole"))

        # Stworzenie wszystkich organizmów
        def spawn_all(self) -> None:
            """Metoda wykonująca stworzenie wszystkich organizmów"""
            each_spawned_times = 2
            all_organisms = [Owca, Wilk, Lis, Mysz, Skunks, Trawa, Mlecz, WilczeJagody]
            used_positions = []
            
            for _ in range(each_spawned_times):
                for organizm in all_organisms:
                    # Wybierz losowe wolne pole, obok już aktualnie zajętego
                    position = [randint(0, self.N-1), randint(0, self.N-1)]
                    while position in used_positions:
                        position = [randint(0, self.N-1), randint(0, self.N-1)]
                    used_positions.append(position)
                    self.swiat.dodajOrganizm(organizm, position)
                    # if organizm == Skunks:
                    #     for _ in range(10):
                    #         position = [randint(0, self.N-1), randint(0, self.N-1)]
                            
                    #         while position in used_positions:
                    #             position = [randint(0, self.N-1), randint(0, self.N-1)]
                            
                    #         used_positions.append(position)
                    #         self.swiat.dodajOrganizm(organizm, position)

        # Nowa runda dla danego organizmu (TODO)
        def next_organizm(self):
            """Metoda wykonująca nową rundę dla danego organizmu"""
            self.swiat.następnyOrganizm()
            self.update_display()

        # Menu gry loop
        def menu(self) -> None:
            """Metoda uruchamiająca menu gry"""
            running = True
            game_state = "menu"
            clock = pg.time.Clock()

            # Tworzenie guzików do menu
            manager_menu = gui.UIManager((525, 630))
            
            # Guzik Graj
            play_button = gui.elements.UIButton(relative_rect=pg.Rect(160, 350, 180, 50),text="Graj",manager=manager_menu,object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            
            # Guzik Ustawienia
            settings_button = gui.elements.UIButton(relative_rect=pg.Rect(160, 420, 180, 50),text="Ustawienia",manager=manager_menu,object_id=gui.core.ObjectID(class_id="@menu_control_button"))
            
            # Guzik Wyjście
            exit_button = gui.elements.UIButton(relative_rect=pg.Rect(160, 490, 180, 50),text="Wyjście",manager=manager_menu,object_id=gui.core.ObjectID(class_id="@menu_control_button"))   
           
            # Guzik Powrót
            back_to_menu_button = gui.elements.UIButton(relative_rect=pg.Rect(160, 550, 180, 50),text="Powrót",manager=manager_menu,object_id=gui.core.ObjectID(class_id="@menu_control_button"),visible=False)
            
            # Pole wpisania wielkości planszy
            number_input = gui.elements.UITextEntryLine(relative_rect=pg.Rect(300, 130, 150, 50),manager=manager_menu,object_id=gui.core.ObjectID(class_id="@menu_control_button"),visible=False,initial_text="20") 

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
                                print("graned")
                                running = False 
                            # Okno ustawień
                            elif event.ui_element == settings_button:
                                print("setting settings")
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
                                self.N = N_value
                                self.table = [[None for _ in range(self.N)] for _ in range(self.N)]
                                self.swiat = Swiat(self.N, self)
                                print(f"Wprowadzona liczba: {user_n_input}")
                            else:
                                print("Niepoprawna liczba")
                        else:
                            number_input.set_text("")
                            print("Niepoprawna liczba")
                    manager_menu.process_events(event)

                # Wyświetlenie menu
                self.screen.fill((100, 100, 100))

                # Okno menu
                if game_state == "menu":
                    # Konfiguracja interfejsu menu
                    font = pg.font.Font(None,54)
                    font_version = pg.font.Font(None,36)
                    font_credits = pg.font.Font(None, 16)
                    title_text = font.render("Wirtualny Świat", True, (255, 255, 255))
                    version_text = font_version.render("Version: 0.5", True, (255, 255, 255))
                    credits_title = font_credits.render("Wykonali:", True, (255, 255, 255))
                    credits_1 = font_credits.render("Norbert Andrzejczuk nr 2", True, (255, 255, 255))
                    credits_2 = font_credits.render("Krystian Słupski nr 23", True, (255, 255, 255))
                    credits_3 = font_credits.render("Szymon Wirkus nr 27", True, (255, 255, 255))
                    self.screen.blit(title_text, (145, 50))
                    self.screen.blit(version_text, (200, 100))
                    self.screen.blit(credits_title, (380, 540))
                    self.screen.blit(credits_1, (380, 560))
                    self.screen.blit(credits_2, (380, 580))
                    self.screen.blit(credits_3, (380, 600))

                # Okno ustawień
                elif game_state == "settings":
                    # Konfiguracja interfejsu ustawień
                    font = pg.font.Font(None, 54)
                    settings_title = font.render("Opcje", True, (255, 255 ,255))
                    self.screen.blit(settings_title,(200, 50))
                    font_option_n = pg.font.Font(None, 24)
                    setting_n = font_option_n.render("Podaj wielkość planszy NxN (6-29):", True, (255, 255, 255))
                    self.screen.blit(setting_n,(20, 150))

                # Rysowanie menu gry
                manager_menu.update(time_delta)
                manager_menu.draw_ui(self.screen)
                pg.display.flip()

            return "play"

        # Wyświetlanie menu do wyboru organizmów
        def displayDodajMenu(self, x, y) -> None:
            """Metoda odpowiedzialna za wyświetlenie menu do wyboru organizmów"""
            self.clicked_button_position = [x, y]
            if self.panel.visible:
                self.panel.visible = False
                for element in self.panel_elements:
                    element.visible = False
            else:
                self.panel.visible = True
                for element in self.panel_elements:
                    element.visible = True
        
        def displayHideMenu(self) -> None:
            """Metoda odpowiedzialna za chowanie menu do wyboru organizmów"""
            # if self.panel.visible:
            self.panel.visible = False
            for element in self.panel_elements:
                element.visible = False
            # else:
            #     self.panel.visible = True
            #     for element in self.panel_elements:
            #         element.visible = True

        # Main loop gry
        def run(self) -> None:
            """Metoda odpowiedzialna za uruchamienie gry"""
            clock = pg.time.Clock()
            running = True

            # Stwórz wszystkie organizmy
            self.spawn_all()
            # Miejsce na testy
            # self.swiat.dodajOrganizm(Owca, 0, 0)
            # self.swiat.dodajOrganizm(Owca, 6, 0)
            # self.swiat.dodajOrganizm(Owca, 0, 7)
            # self.swiat.dodajOrganizm(Owca, 8, 9)
            # self.swiat.dodajOrganizm(Owca, 0, 4)
            # self.swiat.dodajOrganizm(Owca, 14, 2)
            # self.swiat.dodajOrganizm(Owca, 0, 17)
            # self.swiat.dodajOrganizm(Owca, 6, 6)
            # self.swiat.dodajOrganizm(Trawa, 2, 0)
            # self.swiat.dodajOrganizm(Wilk, 4, 5)

            # Wyświetlenie początkowego tury świata
            self.update_display()

            # Pętla gry
            while running:
                time_delta = clock.tick(60) / 1000.0
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.next_round_button:
                            self.messages = []
                            self.narratorLog(f"Tura {self.swiat.numer_tury}")
                            self.next_round()
                            print("next tura")
                        elif event.ui_element == self.save_button:
                            self.save_world()
                            print("zapisaned")
                            self.narratorLog("Zapisano świat")
                        elif event.ui_element == self.load_button:
                            self.load_world()
                            print("wczytaned")
                            self.narratorLog("Wczytano świat")
                        elif event.ui_element == self.next_organizm_button:
                            if self.swiat.current_organism_index == 0:
                                self.messages = []
                                self.narratorLog(f"Tura {self.swiat.numer_tury}")
                            tura_przed = self.swiat.numer_tury
                            self.next_organizm()
                            if self.swiat.numer_tury > tura_przed:
                                self.messages = []
                                self.narratorLog(f"Tura {self.swiat.numer_tury}")
                            print("Następny organizm")
                        elif event.ui_element in self.panel_elements:
                            if event.ui_element == self.button_lis:
                                self.swiat.set_organizmy(self.clicked_button_position, Lis(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_mysz:
                                self.swiat.set_organizmy(self.clicked_button_position, Mysz(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_wilk:
                                self.swiat.set_organizmy(self.clicked_button_position, Wilk(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_owca:
                                self.swiat.set_organizmy(self.clicked_button_position, Owca(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_skunks:
                                self.swiat.set_organizmy(self.clicked_button_position, Skunks(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_trawa:
                                self.swiat.set_organizmy(self.clicked_button_position, Trawa(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_mlecz:
                                self.swiat.set_organizmy(self.clicked_button_position, Mlecz(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_wilczejagody:
                                self.swiat.set_organizmy(self.clicked_button_position, WilczeJagody(self.clicked_button_position, self.swiat))
                                self.update_display()
                                self.displayHideMenu()
                            elif event.ui_element == self.button_empty:
                                self.swiat.set_organizmy(self.clicked_button_position, None)
                                self.update_display()
                                self.displayHideMenu()
                        else:
                            for y in range(len(self.table)):
                                for x in range(len(self.table[y])):
                                    if event.ui_element == self.table[y][x]:
                                        self.displayDodajMenu(x, y)
                    self.manager.process_events(event)
                
                # Rysowanie tła
                self.manager.update(time_delta)
                self.screen.fill((0, 0, 0))
                self.manager.draw_ui(self.screen)

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
