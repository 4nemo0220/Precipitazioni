import time

from PIL import Image

def SovrapponiMeteo(sfondo):
    from PIL import Image, ImageDraw, ImageFont



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


    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        errore=str(e.__class__)
        d = ImageDraw.Draw(sfondo)
        fnt = ImageFont.truetype('arial.ttf', 19)
        d.text((1400, 800), "Non ha funzionato. ERR: "+errore, font=fnt, fill=(255, 255, 255))



    return sfondo






if __name__ == '__main__':
    SovrapponiMeteo()