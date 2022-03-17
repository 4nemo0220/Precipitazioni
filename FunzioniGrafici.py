import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib import cm


class CreaGrafico:
    def __init__(self, GraficoDafa, comando = ["temperatura"]):
        self.graficoData = GraficoDafa
        self.Xatt = time.time()

        self.CreaXTickers()


    def CreaXTickers(self):
        i = 0
        self.graficoData.xt = []
        self.graficoData.tt = []
        while i < len(self.graficoData.th):
            self.graficoData.xt.append(self.graficoData.th[i])
            self.graficoData.tt.append(self.graficoData.txt[i][:10])
            i += 24

        self.graficoData.xt.append(self.graficoData.xt[-1])
        self.graficoData.tt.append(self.graficoData.txt[-1][:10])


    def StampaGrafico(self, comando = ["temperatura"], figsize=(12,6), colorTheme="white"):
        fig, ax = plt.subplots(figsize=(12,6))


        #cancello il lato DX e Up del riquadro del grafico
        right_side = ax.spines["right"]
        right_side.set_visible(False)
        top_side = ax.spines["top"]
        top_side.set_visible(False)

        Y = self.DatiDalComando (comando[0])

        plt.plot(self.graficoData.th, Y, lw=1, c=colorTheme)
        plt.axvline(self.Xatt, c=colorTheme, lw=2)
        for xxt in self.graficoData.xt:
            plt.axvline(xxt, c=colorTheme, lw=1, ls='--')

        plt.xticks(self.graficoData.xt, self.graficoData.tt)
        plt.xlim(self.graficoData.th[0], self.graficoData.th[-1])



        #plt.savefig('test.png', transparent=True) < SALVA SENZA SFONDO


        if len(comando)!= 1:
            if "precipitazioni" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.prec, lw=1,ls=':', c=colorTheme)
            if "Temperatura percepita" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.Tperc, lw=1, ls=':', c=colorTheme)
            if "umidità relativa" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.relHum, lw=1, ls=':', c=colorTheme)
            if "vento a 10m dal suolo" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.wind10, lw=1,ls=':', c=colorTheme)
            if "radiazione solare diretta" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.radSole, lw=1, ls=':', c=colorTheme)
            if "temperatura del suolo" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.tempSuolo, lw=1,ls=':', c=colorTheme)
            if "umidità del suolo" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.humSuolo, lw=1,ls=':', c=colorTheme)

        return plt


    def DatiDalComando (self, stringa):
        if stringa == "temperatura":
            return self.graficoData.T
        elif stringa == "precipitazioni":
            return self.graficoData.prec
        elif stringa == "Temperatura percepita":
            return self.graficoData.Tperc
        elif stringa == "umidità relativa":
            return self.graficoData.relHum
        elif stringa == "vento a 10m dal suolo":
            return self.graficoData.wind10
        elif stringa == "radiazione solare diretta":
            return self.graficoData.radSole
        elif stringa == "temperatura del suolo":
            return self.graficoData.tempSuolo
        elif stringa == "umidità del suolo":
            return self.graficoData.humSuolo




if __name__ == '__main__':

    lati = 41.903
    longi = 12.48






