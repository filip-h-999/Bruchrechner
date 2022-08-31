from tkinter import *
from bruchrechner import *


class Bruchrechner_GUI:
    def __init__(self):
        window = Tk()
        window.geometry('210x200+800+300')
        window.title("Bruchrechner")
        window.resizable(False, False)

        self.derRechner = Bruchrechner()

        def createLabel(t: str, posX: int):
            la = Label(window, text=t)
            la.place(x=posX, y=10)

        createLabel("Bruch 1", 10)
        createLabel("Bruch 2", 78)
        createLabel("Ergebnis", 150)

        self.la4_text = StringVar()
        self.la4_text.set("+")
        la4 = Label(window, textvariable=self.la4_text, font='{Arial} 14')
        la4.place(x=54, y=60)

        la5 = Label(window, text='=', font='{Arial} 14')
        la5.place(x=128, y=60)

        def createEntry(textvar: IntVar, posX: int, posY: int):
            entry = Entry(window, width=3, textvariable=textvar)
            entry.place(x=posX, y=posY, width=30)

        self.int1 = IntVar()
        createEntry(self.int1, 18, 50)
        self.int2 = IntVar()
        createEntry(self.int2, 18, 80)
        self.int3 = IntVar()
        createEntry(self.int3, 88, 50)
        self.int4 = IntVar()
        createEntry(self.int4, 88, 80)
        self.int5 = IntVar()
        createEntry(self.int5, 162, 50)
        self.int6 = IntVar()
        createEntry(self.int6, 162, 80)

        def createBtn(symbol: str, posX: int, cmd):
            btn = Button(window, text=symbol, font='{Arial} 13',
                         command=cmd, bg="light green")
            btn.place(x=posX, y=130)

        createBtn("+", 18+6, self.addition)
        createBtn("-", 65+6, self.subtraction)
        createBtn("*", 110+6, self.multiplication)
        createBtn("/", 155+6, self.division)

    def setAndGet(self):
        self.derRechner.setBruch1Zehler(self.int1.get())
        self.derRechner.setBruch1Nenner(self.int2.get())
        self.derRechner.setBruch2Zehler(self.int3.get())
        self.derRechner.setBruch2Nenner(self.int4.get())
        self.int5.set(self.derRechner.getErgebnisZehler())
        self.int6.set(self.derRechner.getErgebnisNenner())

    def addition(self):
        self.la4_text.set("+")
        self.setAndGet()
        self.derRechner.addition()

    def subtraction(self):
        self.la4_text.set("-")
        self.setAndGet()
        self.derRechner.subtraction()

    def multiplication(self):
        self.la4_text.set("*")
        self.setAndGet()
        self.derRechner.multiplication()

    def division(self):
        self.la4_text.set("/")
        self.setAndGet()
        self.derRechner.division()


if __name__ == '__main__':
    Window = Bruchrechner_GUI()
    mainloop()
