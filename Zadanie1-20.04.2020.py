class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc

    def wyświetl_nazwę(self):
        print("Rodzaj materiału: "+str(self.rodzaj))
        print("Długość materiału: "+str(self.dlugosc))
        print("Szerokość materiału: "+str(self.szerokosc))

class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla=dla

    def wyświetl_dane(self):
        print("Rozmiar ubrania: "+str(self.rozmiar))
        print("Kolor ubrania: "+str(self.kolor))
        print("Ubranie Dla: "+str(self.dla))

class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra

    def wyświetl_dane(self):
        print("Rodzaj swetra : "+str(self.rodzaj_swetra))

bawelna = Material('bawełna', 1, 1)
welna = Material('wełna', 3, 3)
polyester = Material('polyester', 0.7, 0.7)


bawelna.wyświetl_nazwę()
print("\n")
welna.wyświetl_nazwę()
print("\n")
polyester.wyświetl_nazwę()
print("\n")
ubranie = Ubrania('3XL', 'żółty', 'Marcin Nizioł')
ubranie.wyświetl_dane()

print("\n")
sweter = Sweter('Rozsuwany, z kapturem')
sweter.wyświetl_dane()