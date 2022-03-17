from FunzioniStarting import PrintaByNik, AggiornaStato

# importing module for playing with files
from shutil import copyfile, SameFileError

# importing module for logging
import logging
# Create and configure logger
logging.basicConfig(filename="C:/Users/coand/Google Drive/PC/Immagini/Switcher/Log/log.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)



def SaveAsCSV(stringa, nomefile = "nome.txt"):
    # open the file in the write mode
    with open(nomefile, "w") as f:
        f.write(stringa)


def SalvaECopia(immagine, path):
    immagine.save(path + 'Live/sfondo1.png')

    AggiornaStato(80)

    logger.info("  il prog ha salvato l'immagine nel file nominato 'sfondo1.png';")

    original = r'C:/Users/coand/Google Drive/PC/Immagini/Switcher/Live/sfondo1.png'
    target = r'C:/Users/coand/Google Drive/PC/Immagini/Switcher/Live/sfondo2.png'
    try:

        AggiornaStato(90)
        copyfile(original, target)
        logger.info("  il prog ha creato la copia del file 'sfondo1.png' denominandola 'sfondo1.png';")
    # If source and destination are same
    except SameFileError:
        print("Source and destination represents the same file.")
    # If destination is a directory.
    except IsADirectoryError:
        print("Destination is a directory.")
    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
    # For other errors
    except:
        logger.warning("  il prog ha NON creato il file nominato 'TEST1.png';")



