import matplotlib.pyplot as plt
import requests
import time
import io
from FunzioniAPI import ArrTemperatura, ArrPrec
from FunzioniGrafici_VECCHIOMODULO import Grafico, GraficoConPrecipitazioni
from PIL import Image

def SovrapponiMeteo():



    lati = 41.903
    longi = 12.48

    X, Y, T = ArrTemperatura(lati, longi, 5)
    Xprec, Yprec, Xcpr, Ycpr = ArrPrec(lati, longi, 5)
    Dati1= GraficoConPrecipitazioni(X, Y, T, Xprec, Yprec, Xcpr, Ycpr)

    Dati1.StampaGraficoConPrec().savefig('test.png', transparent=True)

    path='C:/Users/coand/Google Drive/PC/Immagini/Switcher/'
    sfondo= Image.open(path+'Live/sfondo1.png')
    gr=Image.open('test.png')

    size=600,300
    gr.thumbnail(size, Image.ANTIALIAS)

    sfondo.paste(gr, (1300, 700), gr)
    sfondo.save('sfondo1.png')






if __name__ == '__main__':
    SovrapponiMeteo()