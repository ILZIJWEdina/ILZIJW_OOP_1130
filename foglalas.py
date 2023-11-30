class Foglalas:
    id_counter = 1

    def __init__(self, szoba, datum, ar):
        self.id = Foglalas.id_counter
        Foglalas.id_counter += 1
        self.szoba = szoba
        self.datum = datum
        self.ar = ar

    def __str__(self):
        return f"Foglalás ID: {self.id}, Szoba: {self.szoba.szam}, Dátum: {self.datum}, Ár: {self.ar} Ft."
