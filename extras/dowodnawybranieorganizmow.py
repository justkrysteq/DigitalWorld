# Funkcja wybierania Zwierząt
def wyborZwierząt(x, y):
    id1 = x % 5 + 3
    id2 = y % 5 + 8
    if id1 == id2:
        id2 = ((y + 1) % 5) + 8
    return id1, id2

# id1 – id (wg tabeli 1) pierwszego ze zwierząt
# id2 – id (wg tabeli 1) drugiego ze zwierząt
# X – przedostatnia cyfra numeru w dzienniku (jeśli jednocyfrowa => wpisz 0)
# Y – ostatnia cyfra numeru z dziennika

# ZWIERZĘTA
# Wilk
# Owca
# Lew/Leniwiec albo wymyslone (Żaba rusza się dwa pola/Skunks - obniza inicjatywe wszystkim wokol, ewentualnie na akcji cofaja sie inni (tak uciekaja od smrodu))
print("ID Zwierząt na podstawie numeru z dziennika 02")
print(wyborZwierząt(0, 2)) # lis, mysz

# ROSLINY
# trawa
# mlecz - A
# wilcze jagody - N

# 😎
