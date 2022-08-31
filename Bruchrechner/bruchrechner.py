class Bruchrechner:
    def __init__(self):
        self.bruch1_zehler = 0
        self.bruch1_nenner = 0
        self.bruch2_zehler = 0
        self.bruch2_nenner = 0
        self.ergebnis_zehler = 0
        self.ergebnis_nenner = 0

    def setBruch1Zehler(self, z):
        self.bruch1_zehler = z

    def setBruch2Zehler(self, z):
        self.bruch2_zehler = z

    def setBruch1Nenner(self, n):
        self.bruch1_nenner = n

    def setBruch2Nenner(self, n):
        self.bruch2_nenner = n

    def getErgebnisZehler(self):
        return self.ergebnis_zehler

    def getErgebnisNenner(self):
        return self.ergebnis_nenner

    def addition(self):
        self.ergebnis_zehler = (self.bruch1_zehler * self.bruch2_nenner) + \
                               (self.bruch2_zehler * self.bruch1_nenner)
        self.ergebnis_nenner = self.bruch1_nenner * self.bruch2_nenner

    def subtraction(self):
        self.ergebnis_zehler = (self.bruch1_zehler * self.bruch2_nenner) - \
                               (self.bruch2_zehler * self.bruch1_nenner)
        self.ergebnis_nenner = self.bruch1_nenner * self.bruch2_nenner

    def multiplication(self):
        self.ergebnis_zehler = self.bruch1_zehler * self.bruch2_zehler
        self.ergebnis_nenner = self.bruch1_nenner * self.bruch2_nenner

    def division(self):
        self.ergebnis_zehler = self.bruch1_zehler * self.bruch2_nenner
        self.ergebnis_nenner = self.bruch1_nenner * self.bruch2_zehler
