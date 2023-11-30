from datetime import date
from szoba import EgyagyasSzoba, KetagyasSzoba
from szalloda import Szalloda

# Felhasználótól kérjen be adatokat
hotel_nev = input("Adja meg a szálloda nevét: ")
szobak = []

while True:
    szobaszam = input("Adja meg a szobaszámot: ")
    szoba_tipus = input("Adja meg a szoba típusát (egyagyas/ketagyas): ").lower()
    ar = int(input("Adja meg a szoba árát: "))

    if szoba_tipus == "egyagyas":
        szobak.append(EgyagyasSzoba(szobaszam, ar))
    elif szoba_tipus == "ketagyas":
        szobak.append(KetagyasSzoba(szobaszam, ar))
    else:
        print("Hibás szoba típus. Csak 'egyagyas' vagy 'ketagyas' elfogadott.")

    ujabb = input("Szeretne még hozzáadni szobát? (igen/nem): ").lower()
    if ujabb != "igen":
        break

# Szálloda létrehozása
szalloda = Szalloda(hotel_nev)

# Szobák hozzáadása a szállodához
for szoba in szobak:
    szalloda.uj_szoba(szoba)

# Szobák listázása
szalloda.osszes_foglalas()
