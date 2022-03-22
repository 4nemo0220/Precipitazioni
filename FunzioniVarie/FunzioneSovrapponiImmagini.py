import time

from PIL import Image

def SovrapponiMeteo(sfondo):



    # lati = 41.903
    # longi = 12.48
    #
    # X, Y, T = ArrTemperatura(lati, longi, 5)
    # Xprec, Yprec, Xcpr, Ycpr = ArrPrec(lati, longi, 5)
    # Dati1= GraficoConPrecipitazioni(X, Y, T, Xprec, Yprec, Xcpr, Ycpr)
    #
    # Dati1.StampaGraficoConPrec().savefig('test.png', transparent=True)
    #
    # path='C:/Users/coand/Google Drive/PC/Immagini/Switcher/'
    # sfondo= Image.open(path+'Live/sfondo1.png')

    try:
        gr=Image.open('grafico.png')
        size = 600, 300
        gr.thumbnail(size, Image.ANTIALIAS)

        sfondo.paste(gr, (1300, 700), gr)
        sfondo

    except:
        time.sleep(1)

        try:
            gr=Image.open('grafico.png')
            size = 600, 300
            gr.thumbnail(size, Image.ANTIALIAS)

            sfondo.paste(gr, (1300, 700), gr)
            sfondo

        except:
            print("Non ha proprio funzionato: FunzioneSovrapponiImmagini/SovrapponiMeteo.")



    return sfondo






if __name__ == '__main__':
    SovrapponiMeteo()