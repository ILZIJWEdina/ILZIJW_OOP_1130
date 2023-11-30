# szalloda.py

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def listaz_szobak(self):
        print(f"Szobák a(z) {self.nev} szállodában:")
        for szoba in self.szobak:
            print(f"Szoba száma: {szoba.szobaszam}, Típus: {szoba.szoba_tipus()}, Ár: {szoba.ar} Ft")

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                print(f"Foglalás a(z) {self.nev} szállodában:")
                print(f"Szoba típusa: {szoba.szoba_tipus()}")
                print(f"Szobaszám: {szobaszam}")
                print(f"Dátum: {datum}")
                print(f"Ár: {szoba.ar} Ft")
                print("---------------------------")
                return szoba.ar
        print(f"Nincs ilyen szoba: {szobaszam}")
        return 0

    def lemondas(self, szobaszam, datum):
        print(f"Foglalás lemondása a(z) {self.nev} szállodában:")
        print(f"Szobaszám: {szobaszam}")
        print(f"Dátum: {datum}")
        print("---------------------------")

    def osszes_foglalas(self):
        print(f"A(z) {self.nev} szálloda összes foglalása:")
        for foglalas in self.foglalasok:
            print(f"Szoba típusa: {foglalas.szoba.szoba_tipus()}, Szobaszám: {foglalas.szoba.szobaszam}")
        print("---------------------------")

    def is_szoba_szabad(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                return False
        return True
