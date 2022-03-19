import matplotlib.pyplot as plt
import time
import numpy as np
from matplotlib import cm
from FunzioniAPI import APIOpenMeteo


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


    def StampaGrafico(self, comando = ["temperatura"], figsize=(12,6), colorTheme="white",mlw=1):
        fig, ax = plt.subplots(figsize=(12,6))


        #cancello il lato DX e Up del riquadro del grafico
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines['bottom'].set_color(colorTheme)
        ax.spines['left'].set_color(colorTheme)
        #ax.set_facecolor("gray")#<............................................................................


        ax.tick_params(axis='x', colors=colorTheme)

        [t.set_color(colorTheme) for t in ax.yaxis.get_ticklines()]
        [t.set_color(colorTheme) for t in ax.yaxis.get_ticklabels()]

        ax.xaxis.label.set_color(colorTheme)  # setting up X-axis label color to yellow
        ax.yaxis.label.set_color(colorTheme)

        Y = self.DatiDalComando (comando[0])

        plt.plot(self.graficoData.th, Y, lw=1*mlw, c=colorTheme)
        plt.axvline(self.Xatt, c=colorTheme, lw=2*mlw)
        for xxt in self.graficoData.xt:
            plt.axvline(xxt, c=colorTheme, lw=1*mlw, ls='--')

        plt.xticks(self.graficoData.xt, self.graficoData.tt, c=colorTheme)
        plt.xlim(self.graficoData.th[0], self.graficoData.th[-1])

        #plt.savefig('test.png', transparent=True) < SALVA SENZA SFONDO


        if len(comando)!= 1:
            if "precipitazioni" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.prec, lw=1*mlw,ls=':', c=colorTheme)
            if "Temperatura percepita" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.Tperc, lw=1*mlw, ls=':', c=colorTheme)
            if "umidità relativa" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.relHum, lw=1*mlw, ls=':', c=colorTheme)
            if "vento a 10m dal suolo" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.wind10, lw=1*mlw,ls=':', c=colorTheme)
            if "radiazione solare diretta" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.radSole, lw=1*mlw, ls=':', c=colorTheme)
            if "temperatura del suolo" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.tempSuolo, lw=1*mlw,ls=':', c=colorTheme)
            if "umidità del suolo" in comando[1:]:
                plt.plot(self.graficoData.th, self.graficoData.humSuolo, lw=1*mlw,ls=':', c=colorTheme)

        self.plot = plt
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
    Roma=APIOpenMeteo()
    Roma.AggiungiPrecipitazioni()
    Roma.AggiungiTemperaturaPercepita()

    Roma.grafico=CreaGrafico( GraficoDafa =Roma)
    Roma.grafico.CreaXTickers()
    plt=Roma.grafico.StampaGrafico(colorTheme='black', comando = ["temperatura", "precipitazioni", "Temperatura percepita"], mlw=2)
    plt.show()






