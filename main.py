class Calculator:

    def __init__(self,cislo,cislo2):
        self.cislo = cislo
        self.cislo2 = cislo2


    def plus(self):
        vypocet = self.cislo + self.cislo2
        return vypocet

    def minus(self):
        vypocet = self.cislo-self.cislo2
        return vypocet

    def krat(self):
        vypocet = self.cislo*self.cislo2
        return vypocet

    def delenie(self):
        vypocet = self.cislo/self.cislo2
        return vypocet
