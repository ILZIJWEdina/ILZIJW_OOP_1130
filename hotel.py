from datetime import date
from szoba import EgyagyasSzoba, KetagyasSzoba
from szalloda import Szalloda

# Felhasználótól kérjük be a szálloda nevét
szalloda_nev = input("Kérem, adja meg a szálloda nevét: ")

# Hozzuk létre a szállodát a megadott névvel
szalloda = Szalloda(szalloda_nev)

# Kérjük be a felhasználótól szobák adatait
while True:
    szobaszam = input("Adja meg a szoba számát (üres mező kilépéshez): ")
    if not szobaszam:
        break

    szoba_tipus = input("Adja meg a szoba típusát (egyagyas/ketagyas): ").lower()
    ar = int(input("Adja meg a szoba árát: "))

    # Az egy- vagy kétágyas szoba típusától függően hozzuk létre a szobát
    if szoba_tipus == "egyagyas":
        szoba = EgyagyasSzoba(szobaszam, ar)
    elif szoba_tipus == "ketagyas":
        szoba = KetagyasSzoba(szobaszam, ar)
    else:
        print("Ismeretlen szoba típus. Egy vagy ketagyas lehet.")

    # Adjuk hozzá a szobát a szállodához
    szalloda.add_szoba(szoba)

# Kiírjuk a szobák adatait
szalloda.listaz_szobak()


# Kérjük be a felhasználótól a foglalások adatait
while True:
    datum = input("Adja meg a foglalás dátumát (üres mező kilépéshez): ")
    if not datum:
        break

    szobaszam = input("Adja meg a szobaszámot a foglaláshoz: ")

    # Foglaljuk le a megadott szobát a megadott dátumra
    foglalas = szalloda.foglalas(szobaszam, datum)

    # Ha a foglalás sikeres volt, írjuk ki a foglalás adatait
    if foglalas:
        print("Foglalás sikeres:\n", foglalas)
    else:
        print("Nem sikerült foglalni a szobát. Szoba foglalt vagy nem létezik.")

# Kiírjuk a foglalásokat
szalloda.listaz_foglalasok()


