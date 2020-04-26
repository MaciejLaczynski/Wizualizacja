class Ksztalty:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.opis = "Klasa Kształtów"
    def pole(self):
        return self.x * self.y
    def obwod(self):
        return 2 * self.x + 2 * self.y
    def wpisz_opis(self, text):
        self.opis = text
    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x =x
        self.y=x
    def __add__(self,pom):
        return self.x + pom.x
figura = Kwadrat(69)
print('Pierwsza figura:', figura.x,'x', figura.y)
figura2 = Kwadrat(420)
print('Druga figura:', figura2.x,'x', figura2.y)
figura3 = Kwadrat(figura + figura2)
print('Trzecia figura:', figura3.x,'x', figura3.y)