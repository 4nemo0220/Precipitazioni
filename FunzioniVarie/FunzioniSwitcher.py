from FunzioniInfoOra  import InfoOra
from FunzioniIlMeteo  import InfoMeteo
from FunzioniTitoliGiorali import TitoloRep, TitoloRepMondo, TitoloCor, TitoloAnsa
from FunzioniStarting import PrintaByNik, AggiornaStato

# importo e setto tutto il necessario per i file di logging
import logging
# Create and configure logger
logging.basicConfig(filename="C:/Users/coand/Google Drive/PC/Immagini/Switcher/Log/log.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()    # Creating an object
logger.setLevel(logging.DEBUG)  # Setto la soglia del logger a schermo su DEBUG



####InizioImport

class InfoSfondo:
    def __init__(self, dimSfondo= (1920, 1080), luogo= "Caltanissetta", largColonna=250, hCalend=500):
        self.dimSfondo=dimSfondo
        self.luogo=luogo
        self.largColonna=largColonna
        self.hCalend=hCalend
        self.linea=int((largColonna/450)*40)

    def VecchiaDef (self):
        
        self.strOra = "Ultimo aggiornato alle " + InfoOra()
        logger.debug(f"  il prog ha creato la stringa 'strOra' [{self.strOra}];")
        logger.info("  il prog ha creato la stringa 'strOra';")

        AggiornaStato(10)

        self.InfoMeteoRoma = InfoMeteo("Roma")
        logger.debug(f"  il prog ha creato la stringa 'Roma' \n[--------------\n{self.InfoMeteoRoma}\n--------------];")
        logger.info("  il prog ha creato la stringa 'Roma';")

        self.CreaStringaTitoloRepubblica()
        self.CreaStringaTitoloRepubblicaMondo()

        self.CreaStringaTitoloCorriere()
        self.CreaStringaTitoloAnsa()

        self.CreaSTRINGONA()


    def SpezzaInrighe(self, stringhetta):

        for i in [4, 3, 2]:   stringhetta = stringhetta.replace((" " * i), " - ")
        stringhetta = stringhetta.split(' ')
        newstr = '''|"'''
        count = 0
        for i in range(len(stringhetta)):
            if count + len(stringhetta[i]) <= self.linea:
                if count != 0:
                    newstr += (' ' + stringhetta[i])
                else:
                    newstr += stringhetta[i]

                count += len(stringhetta[i])
            else:
                newstr += chr(172) + '\n|' + chr(173) + chr(62)
                count = len(stringhetta[i] + ' ') + 2
                newstr += stringhetta[i]

        return newstr + '''."'''

    def CreaStringaTitoloRepubblica(self):
        self.repubblica = self.SpezzaInrighe(TitoloRep())


    def CreaStringaTitoloRepubblica(self):
        self.repubblica = self.SpezzaInrighe(TitoloRep())

    def CreaStringaTitoloRepubblicaMondo(self):
        self.repubblicaM = self.SpezzaInrighe(TitoloRepMondo())

    def CreaStringaTitoloCorriere(self):
        self.corriere = self.SpezzaInrighe(TitoloCor())

    def CreaStringaTitoloAnsa(self):
        self.ansa = self.SpezzaInrighe(TitoloAnsa())





    def CreaSTRINGONA(self):
        self.STRINGONA = self.InfoMeteoRoma[0] + '\n' \
                         + '\nilCorriere:\n' + self.corriere \
                         + '\n\nla Repubblica:\n' + self.repubblica \
                         + '\nla Repubblica Mondo:\n' + self.repubblicaM \
                         + '\n\nAnsa:\n' + self.ansa

        # Vecchia versione
        # self.STRINGONA= self.strOra + "\n" + self.InfoMeteoRoma[0] + '\n' \
        #                 +'\nilCorriere:\n'          + self.corriere \
        #                 +'\n\nla Repubblica:\n'       + self.repubblica \
        #                 +'\nla Repubblica Mondo:\n' + self.repubblicaM \
        #                 +'\n\nAnsa:\n'                + self.ansa


####FineImport






if __name__ == '__main__':
    IinfoSfondo = InfoSfondo()

    print(IinfoSfondo)