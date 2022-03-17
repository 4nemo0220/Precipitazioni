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

# IMPORTA MODULI PERSONALI
from FunzioniStarting import *
from FunzioniSwitcher import InfoSfondo
from FunzioniImmagini import *
from FunzioniSalvaSuFile import *
from FunzioneInfoOra  import InfoOra
from FunzioniIlMeteo  import InfoMeteo
from FunzioniTitoliGiorali import TitoloRep, TitoloRepMondo, TitoloCor, TitoloAnsa
import threading

def PT1_scrIlMeteo():
    global IinfoSfondo

    IinfoSfondo.InfoMeteoRoma=InfoMeteo(luogo=IinfoSfondo.luogo)

    T1_secThreads = []

    T1_secThreads.append(threading.Thread(target=PT1_ST1_ApriImg))
    T1_secThreads[0].start()

    T1_secThreads.append(threading.Thread(target=PT1_ST2_ApriImg))
    T1_secThreads[1].start()

    for st in T1_secThreads:
        st.join()

    print("\n-----------------T1: ENDDDDDDDDDD")

def PT1_ST1_ApriImg():
    immagine = CreaImmagineFinale (IinfoSfondo)
    print("PT1_ST1: End")

def PT1_ST2_ApriImg():
    print("PT1_ST2: End")


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

    for st in secThreads:
        st.join()




    print("\n-----------------T2: ENDDDDDDDDDD")

def PT3_Calendario():
    global IinfoSfondo
    IinfoSfondo.giorniCal = CreaArrayCalendario()

    print("\n-----------------T3: ENDDDDDDDDDD")

if __name__ == '__main__':
    PrintaSwitcher(edizione)

    start=time.time()

    IinfoSfondo = InfoSfondo( dimSfondo= (1920, 1080), luogo= "Roma", largColonna=450, hCalend=250)
    IinfoSfondo.path = 'C:/Users/coand/Google Drive/PC/Immagini/Switcher/'

    primaryThreads= []
    primaryThreads.append(threading.Thread(target = PT1_scrIlMeteo))
    primaryThreads[0].start()
    primaryThreads.append(threading.Thread(target = PT2_scrQuotidiani))
    primaryThreads[1].start()
    primaryThreads.append(threading.Thread(target = PT3_Calendario))
    primaryThreads[2].start()

    for pt in primaryThreads:
        pt.join()

    tempo=time.time()-start


    # print(IinfoSfondo.InfoMeteoRoma[0])
    # print(IinfoSfondo.repubblicaM)
    # print("tempo:", tempo)



     #
    # InfMet = InfoMeteo("Belmonte in sabina")
    # LatiLongi=InfMet[3] #latilongi
    #
    # #Printa su schermo le info per l'avvio del programma
    # AggiornaStato(0)
    #
    # #Crea l'oggetto "IinfoSfondo" contenente tutte le info necessarie
    # IinfoSfondo = InfoSfondo()
    #
    # AggiornaStato(50)
    #
    # #Crea l'immagine da salvare - con la funzione CreaImmagineFinale()
    # #Salva l'immagine creata in duplice copia - con la funzione SalvaECopia()
    # IinfoSfondo.path='C:/Users/coand/Google Drive/PC/Immagini/Switcher/'
    # SalvaECopia(  CreaImmagineFinale(IinfoSfondo, dimSfondo)  , IinfoSfondo.path)
    #
    # AggiornaStato(100)

    exit(0)