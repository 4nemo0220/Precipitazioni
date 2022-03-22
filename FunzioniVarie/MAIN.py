import os

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

#PT0
def PT0_scrIlMeteo():
    global IinfoSfondo

    IinfoSfondo.InfoMeteoRoma=InfoMeteo(luogo=IinfoSfondo.luogo)
    #(infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)

    AggiornaStato(20)

    PT0_ST = []
    PT0_ST.append(threading.Thread(target=PT0_ST0_ApriImg))
    PT0_ST[0].start() #PT0_ST0
    PT0_ST.append(threading.Thread(target=PT0_ST1_ApiOpenMeteo))
    PT0_ST[1].start() #PT0_ST1

    # JOIN PT0_ST0
    PT0_ST[0].join()

    # JOIN PT3
    PT[2].join()

    d = ImageDraw.Draw(IinfoSfondo.immagine)
    d = StampaCalendario(
        d,
        L=IinfoSfondo.dimSfondo[0],
        H=IinfoSfondo.dimSfondo[1],
        Ximm=(IinfoSfondo.dimSfondo[0] - IinfoSfondo.largColonna),
        Yimm=IinfoSfondo.hCalend,
        giorniCal=IinfoSfondo.giorniCal
    )

    # JOIN PT2
    PT[1].join()

    IinfoSfondo.CreaSTRINGONA()

    fnt = ImageFont.truetype('arial.ttf', 19)
    d.text(((IinfoSfondo.dimSfondo[0] - IinfoSfondo.largColonna), IinfoSfondo.hCalend),
           IinfoSfondo.STRINGONA,
           font=fnt, fill=(255, 255, 255))
    logger.info("  il prog ha creato immagine da salvare;")

    # JOIN PT0_ST1
    PT0_ST[1].join()

    # print("\n-----------------T1: ENDDDDDDDDDD")

#PT0_ST0
def PT0_ST0_ApriImg():
    global IinfoSfondo

    IinfoSfondo.immagine = CreaImmagine (IinfoSfondo)

#PT0_ST1
def PT0_ST1_ApiOpenMeteo():

    global IinfoSfondo

    Roma = APIOpenMeteo( Lati=IinfoSfondo.InfoMeteoRoma[3][0], Longi=IinfoSfondo.InfoMeteoRoma[3][1], gF =3, gP=1)
    Roma.AggiungiPrecipitazioni()
    Roma.AggiungiTemperaturaPercepita()

    ogGrfico=CreaGrafico(Roma)

    ogGrfico.CreaXTickers()
    IinfoSfondo.pltGrafico=ogGrfico.StampaGrafico( comando = ["temperatura", "precipitazioni", "Temperatura percepita"], mlw=2 )

    IinfoSfondo.pltGrafico.savefig('grafico.png', transparent=True) #<------------------------------------------------------------------------------------------
    time.sleep(0.1)

#PT1
def PT1_scrQuotidiani():

    global IinfoSfondo


    PT1_ST = []

    #IinfoSfondo.CreaStringaTitoloRepubblica()
    PT1_ST.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloRepubblica))
    PT1_ST[0].start()


    #IinfoSfondo.CreaStringaTitoloRepubblicaMondo()
    PT1_ST.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloRepubblicaMondo))
    PT1_ST[1].start()


    #IinfoSfondo.CreaStringaTitoloCorriere()
    PT1_ST.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloCorriere))
    PT1_ST[2].start()

    #IinfoSfondo.CreaStringaTitoloAnsa()
    PT1_ST.append(threading.Thread(target=IinfoSfondo.CreaStringaTitoloAnsa))
    PT1_ST[3].start()

    for i in range(len(PT1_ST)):
        PT1_ST[i].join()
        # print("PT2_ST",i,": End", sep='')


#PT2
def PT2_Calendario():
    global IinfoSfondo
    IinfoSfondo.strOra=InfoOra()
    IinfoSfondo.giorniCal = CreaArrayCalendario()



if __name__ == '__main__':


    PrintaSwitcher(edizione)
    start=time.time()

    IinfoSfondo = InfoSfondo( dimSfondo= (1920, 1080),
                              luogo= "Roma Centro Borgo",
                              largColonna=550,
                              hCalend=250)

    IinfoSfondo.path = 'C:/Users/coand/Google Drive/PC/Immagini/Switcher/' #os.getcwd().split("FunzioniVarie")[0].replace("\\", "/")

    PT= []
    PT.append(threading.Thread(target = PT0_scrIlMeteo))
    PT[0].start()
    PT.append(threading.Thread(target = PT1_scrQuotidiani))
    PT[1].start()
    PT.append(threading.Thread(target = PT2_Calendario))
    PT[2].start()

    # all the work ...

    # JOIN PT0
    PT[0].join()




    AggiornaStato(90)

    IinfoSfondo.immagine = SovrapponiMeteo(IinfoSfondo.immagine)

    SalvaECopia(IinfoSfondo.immagine, IinfoSfondo.path)
    time.sleep(0.1)
    AggiornaStato(99)

    try:
        os.remove('grafico.png')
        time.sleep(0.1)

    except:
        print( "Rimozione non riuscita!")
    AggiornaStato(100)




    tempo=time.time()-start
    print("\nTempo:", tempo)

    exit(0)