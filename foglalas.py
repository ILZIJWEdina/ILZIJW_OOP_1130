class Foglalás:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás a(z) {self.szoba.szalloda_nev} szállodában:\n" \
               f"Szoba típusa: {self.szoba.szoba_tipus()}\n" \
               f"Szobaszám: {self.szoba.szobaszam}\n" \
               f"Dátum: {self.datum}\n" \
               f"Ár: {self.szoba.ar} Ft\n---------------------------"
