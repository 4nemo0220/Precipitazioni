import matplotlib.pyplot as plt
import requests
import time

class TimeOptimizzationClass:
    def __init__(self,):
        self.start=time.time()
        self.tempi=[]
        self.nomi = []

    def Tic (self, nome="xx"):
        self.tempi.append(time.time()-self.start)
        if nome=="xx":
            nome=str(len(self.tempi))
        self.nomi.append(nome)





    def PrintaResoconto(self):
        print("\n\nRESOCONTO TEMPI\nStartingTime: ",self.start)
        diff=[]

        # Riga TITOLI
        print("Tic\t\tStart", end="\t")
        for t in self.nomi:
            print(self.Normalizza(t), end="\t")

        # Riga TEMPO
        print("\nTempo TOT\t0\t", end='')
        for t in self.tempi:
            print(self.Arrotonda(t), end="\t")


        # Riga PERCENTUALE d'avanzamento
        print("\n% risp. il TOT\t", end='')
        print(self.Normalizza("0%"), end="\t")
        for c in range(len(self.tempi) - 1):
            print(str((round(self.tempi[c + 1] * 100 / self.tempi[-1], 1))) + "%", end="\t")


        # Riga DIFFERENZE TEMPO
        print("\nTEMPO tra tic\t", end='')
        print(self.Arrotonda(self.tempi[0]), end="\t")
        for c in range(len(self.tempi)-1):
            diff.append(self.tempi[c+1]-self.tempi[c])
            print(self.Arrotonda(diff[c]), end="\t")


        # Riga percentuale rispetto al totale
        print("\n% risp. al TOT\t", end='')
        print(self.Normalizza("0%"), end="\t")
        for c in diff:
            print(
                self.Normalizza(str( int( c*100/self.tempi[-1])) + "%")
            , end="\t"
            )


        # Riga percentuale rispetto il massimo
        print("\n% risp. il MAX\t", end='')
        print(self.Normalizza("0%"), end="\t")
        for c in diff:
            print(
                self.Normalizza(str( int( c*100/max(diff))) + "%")
            , end="\t"
            )

        print("\n")

    def Normalizza(self, valore):
        if len(valore) > 8:
            valore =valore[:6]+'.'
        else:
            while len(valore) <= 7:
                valore += ' '
        return valore[:7]


    def Arrotonda(self, valore):
        valore= str(round(valore, 4))
        while len(valore)<6:
            valore+=' '
        return valore

if __name__ == '__main__':
    print("Start")
    Tempi=TimeOptimizzationClass()
    time.sleep(0.1)
    Tempi.Tic("sandroloooooooooooooo")
    time.sleep(0.21)
    Tempi.Tic()
    time.sleep(0.11)
    Tempi.Tic()
    time.sleep(0.05)
    Tempi.Tic()
    time.sleep(0.03)
    Tempi.Tic()
    Tempi.PrintaResoconto()

    print("Done")