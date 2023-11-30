from datetime import date
from szoba import EgyagyasSzoba, KetagyasSzoba
from szalloda import Szalloda

# Példa használatra
egyagyas = EgyagyasSzoba("101", 5000)
ketagyas = KetagyasSzoba("201", 8000)

szalloda = Szalloda("Luxury Hotel")
szalloda.uj_szoba(egyagyas)
szalloda.uj_szoba(ketagyas)

datum = date.today()
arfoglalas = szalloda.foglalas("101", datum)
szalloda.lemondas("101", datum)
szalloda.osszes_foglalas()

