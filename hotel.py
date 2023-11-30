from datetime import date
from szoba import EgyagyasSzoba, KetagyasSzoba
from szalloda import Szalloda

def main():
    nev = input("Kérem, adja meg a szálloda nevét: ")
    szalloda = Szalloda(nev)

    while True:
        print("\n1 - Szoba hozzáadása")
        print("2 - Kilistázás")
        print("3 - Foglalás rögzítése")
        print("4 - Kilépés")

        valasztas = input("Válasszon műveletet: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a szoba számát: ")
            ar = int(input("Adja meg a szoba árát: "))
            szoba_tipus = input("Adja meg a szoba típusát (egyagyas/ketagyas): ").lower()

            if szoba_tipus == "egyagyas":
                szoba = EgyagyasSzoba(szobaszam, ar)
            elif szoba_tipus == "ketagyas":
                szoba = KetagyasSzoba(szobaszam, ar)
            else:
                print("Hibás szoba típus!")

            szalloda.uj_szoba(szoba)

        elif valasztas == "2":
            szalloda.listaz_szobak()
            foglalasokat_listazza(szalloda)

        elif valasztas == "3":
            foglalas_szobaszam = input("Adja meg a foglalandó szoba számát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")

            if is_valid_date(datum):
                foglalas_osszeg = szalloda.foglalas(foglalas_szobaszam, datum)
                if foglalas_osszeg > 0:
                    print(f"A foglalás összege: {foglalas_osszeg} Ft")
            else:
                print("Hibás dátum formátum vagy már múltbeli dátumot adott meg.")

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen választás! Kérem, válasszon újra.")

def is_valid_date(date_str):
    try:
        datum = date.fromisoformat(date_str)
        return datum >= date.today()
    except ValueError:
        return False

def foglalasokat_listazza(szalloda):
    print("\nSzálloda foglalások:")
    szalloda.osszes_foglalas()

if __name__ == "__main__":
    main()
