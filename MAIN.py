from FunzioniAPI         import APIOpenMeteo
from FunzioniSalvaSuFile import SaveAsCSV
from FunzioniGrafici import Grafico, GraficoConPrecipitazioni
from FunzioniTest import VediamoUnpo


if __name__ == '__main__':

    Roma = APIOpenMeteo( )
    Roma.AggiungiPrecipitazioni()
    Roma.AggiungiTemperaturaRelHum()
    Roma.AggiungiTemperaturaPercepita()
    Roma.AggiungiVento()
    Roma.AggiungiRadSol()
    Roma.AggiungiTempSuolo()
    Roma.AggiungiUmidSuolo()

    VediamoUnpo(Roma)



    plot = 0

    if plot == 1:
        graficoDati1 = GraficoConPrecipitazioni(Roma.th, Roma.T, Roma.txt, Roma.prec, Roma.th, Roma.precCum, Roma.td)

        graficoDati1.StampaGraficoConPrec().show()



    printAll= 0


    if printAll == True:

        stringaCSV = 'time, timeISO, temperature, Tperc, HumRel, wind10, radSole, tempSuolo, humSuolo\n'
        for i in range(len(Roma.x)):
            stringaCSV += str(Roma.x[i]) + ', ' + str(Roma.txt[i]) + ', ' + str(Roma.T[i]) + ', ' + str(Roma.Tperc[i]) + ', ' + str(Roma.relHum[i]) + ', ' + str(Roma.wind10[i]) + ', ' + str(Roma.radSole[i]) + ', ' + str(Roma.tempSuolo[i]) + ', ' + str(Roma.humSuolo[i]) + '\n'

        SaveAsCSV(stringaCSV, nomefile = "dati.csv")

