edizione= "015"

# IMPORTA E SETTA il LOGGER
import logging
logging.basicConfig(filename="C:/Users/coand/Google Drive/PC/Immagini/Switcher/Log/log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# IMPORTA MODULI ESTERNI
from shutil import copyfile, SameFileError
from sys import exit
from PIL import Image, ImageDraw, ImageFont
import time
from bs4 import BeautifulSoup
from requests import get
import threading

# IMPORTA MODULI PERSONALI
from FunzioniStarting import *
from FunzioniSwitcher import InfoSfondo
from FunzioniImmagini import *
from FunzioniSalvaSuFile import *
from FunzioneInfoOra  import InfoOra
from FunzioniIlMeteo  import InfoMeteo
from FunzioniTitoliGiorali import TitoloRep, TitoloRepMondo, TitoloCor, TitoloAnsa
from FunzioniAPI import APIOpenMeteo
from FunzioniGrafici import CreaGrafico
from FunzioneSovrapponiImmagini import SovrapponiMeteo


def PT1_scrIlMeteo():
    global IinfoSfondo

    IinfoSfondo.InfoMeteoRoma=InfoMeteo(luogo=IinfoSfondo.luogo)
    #(infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)

    AggiornaStato(20)

    T1_secThreads = []

    T1_secThreads.append(threading.Thread(target=PT1_ST0_ApriImg))
    T1_secThreads[0].start()

    T1_secThreads.append(threading.Thread(target=PT1_ST1_ApiOpenMeteo))
    T1_secThreads[1].start()


    T1_secThreads[0].join()

    AggiornaStato(50)

    primaryThreads[2].join()
    d = ImageDraw.Draw(IinfoSfondo.immagine)

    d = StampaCalendario(
        d,
        L=IinfoSfondo.dimSfondo[0],
        H=IinfoSfondo.dimSfondo[1],
        Ximm=(IinfoSfondo.dimSfondo[0] - IinfoSfondo.largColonna),
        Yimm=IinfoSfondo.hCalend,
        giorniCal=IinfoSfondo.giorniCal
    )


    primaryThreads[1].join()


    IinfoSfondo.CreaSTRINGONA()

    fnt = ImageFont.truetype('arial.ttf', 19)
    d.text(((IinfoSfondo.dimSfondo[0] - IinfoSfondo.largColonna), IinfoSfondo.hCalend),
           IinfoSfondo.STRINGONA,
           font=fnt, fill=(255, 255, 255))
    logger.info("  il prog ha creato immagine da salvare;")


    T1_secThreads[1].join()
    AggiornaStato(90)

    IinfoSfondo.immagine=SovrapponiMeteo(IinfoSfondo.immagine)
    # print("\n-----------------T1: ENDDDDDDDDDD")


def PT1_ST0_ApriImg():
    global IinfoSfondo

    IinfoSfondo.immagine = CreaImmagine (IinfoSfondo)

def PT1_ST1_ApiOpenMeteo():

    global IinfoSfondo

    Roma = APIOpenMeteo( Lati=IinfoSfondo.InfoMeteoRoma[3][0], Longi=IinfoSfondo.InfoMeteoRoma[3][1], gF =3, gP=0)
    Roma.AggiungiPrecipitazioni()
    Roma.AggiungiTemperaturaPercepita()

    ogGrfico=CreaGrafico(Roma)

    ogGrfico.CreaXTickers()
    IinfoSfondo.pltGrafico=ogGrfico.StampaGrafico( comando = ["temperatura", "precipitazioni", "Temperatura percepita"], mlw=2 )

    IinfoSfondo.pltGrafico.savefig('grafico.png', transparent=True) #<------------------------------------------------------------------------------------------


def PT2_scrQuotidiani():

    global IinfoSfondo


    secThreads = []

    #IinfoSfondo.CreaStringaTitoloRepubblica()
    secThreads.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloRepubblica))
    secThreads[0].start()


    #IinfoSfondo.CreaStringaTitoloRepubblicaMondo()
    secThreads.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloRepubblicaMondo))
    secThreads[1].start()


    #IinfoSfondo.CreaStringaTitoloCorriere()
    secThreads.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloCorriere))
    secThreads[2].start()

    #IinfoSfondo.CreaStringaTitoloAnsa()
    secThreads.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloAnsa))
    secThreads[3].start()

    for i in range(len(secThreads)):
        secThreads[i].join()
        # print("PT2_ST",i,": End", sep='')



def PT3_Calendario():
    global IinfoSfondo
    IinfoSfondo.strOra=InfoOra()
    IinfoSfondo.giorniCal = CreaArrayCalendario()



if __name__ == '__main__':
    PrintaSwitcher(edizione)

    start=time.time()

    IinfoSfondo = InfoSfondo( dimSfondo= (1920, 1080), luogo= "Roma centro Borgo", largColonna=550, hCalend=250)
    IinfoSfondo.path = 'C:/Users/coand/Google Drive/PC/Immagini/Switcher/'

    primaryThreads= []
    primaryThreads.append(threading.Thread(target = PT1_scrIlMeteo))
    primaryThreads[0].start()
    primaryThreads.append(threading.Thread(target = PT2_scrQuotidiani))
    primaryThreads[1].start()
    primaryThreads.append(threading.Thread(target = PT3_Calendario))
    primaryThreads[2].start()



    primaryThreads[0].join()

    SalvaECopia(IinfoSfondo.immagine, IinfoSfondo.path)
    AggiornaStato(100)




    tempo=time.time()-start
    print("\nTempo:", tempo)

    exit(0)