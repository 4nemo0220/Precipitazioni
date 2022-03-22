from datetime import datetime
import os
import shutil

from FunzioniAggiornamentoEBackUp import *



if __name__ == '__main__':

    nomeProgramma = "Switcher"
    versione = 1

    print("Nome  programma:", nomeProgramma)
    my_date = datetime.now()

    edizione, stringaComando = AggiornaFileComando(versione)

    CancellaCartelleInutili()

    CreabackUp(versione, edizione, my_date, nomeProgramma)

    AggiornaExe ()






