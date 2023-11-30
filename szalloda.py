from foglalas import Foglalas

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def listaz_szobak(self):
        print(f"{self.nev} szálloda szobái:")
        for szoba in self.szobak:
            print(szoba)

    def foglalas(self, szoba_szam, datum):
        for szoba in self.szobak:
            if szoba.szam == szoba_szam:
                ar = szoba.foglal(datum)
                foglalas = Foglalas(szoba, datum, ar)
                self.foglalasok.append(foglalas)
                return f"Sikeres foglalás a(z) {szoba_szam} számú szobára. Ár: {ar} Ft."

        return f"Nincs ilyen szobaszám: {szoba_szam}."

    def lemondas(self, foglalas_id):
        for foglalas in self.foglalasok:
            if foglalas.id == foglalas_id:
                foglalas.szoba.lemond(foglalas.datum)
                self.foglalasok.remove(foglalas)
                return f"Sikeres lemondás a(z) {foglalas_id} azonosítójú foglalásról."

        return f"Nincs ilyen foglalás: {foglalas_id}."

    def listaz_foglalasok(self):
        print(f"{self.nev} szálloda foglalásai:")
        for foglalas in self.foglalasok:
            print(foglalas)


    def foglalas(self, szoba_szam, datum):
        for szoba in self.szobak:
            if szoba.szam == szoba_szam:
                # Ellenőrizzük, hogy a dátum jövőbeni-e
                jelenlegi_datum = datetime.now().strftime("%Y-%m-%d")
                if datum < jelenlegi_datum:
                    return "Csak jövőbeni dátumra lehet foglalni."

                # Az eredeti kód folytatása
                ar = szoba.foglal(datum)
                foglalas = Foglalas(szoba, datum, ar)
                self.foglalasok.append(foglalas)
                return f"Sikeres foglalás a(z) {szoba_szam} számú szobára. Ár: {ar} Ft."

        return f"Nincs ilyen szobaszám: {szoba_szam}."


    def lemondas(self, foglalas_id):
        for foglalas in self.foglalasok:
            if foglalas.id == foglalas_id:
                # Ellenőrizzük, hogy a foglalás létezik
                if foglalas.szoba not in self.szobak:
                    return "A foglalás már nem létezik."

                foglalas.szoba.lemond(foglalas.datum)
                self.foglalasok.remove(foglalas)
                return f"Sikeres lemondás a(z) {foglalas_id} azonosítójú foglalásról."

        return f"Nincs ilyen foglalás: {foglalas_id}."
