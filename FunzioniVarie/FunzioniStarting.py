from FunzioniInfoOra  import InfoOra
import time

####InizioImport

def PrintaByNik(edizione=0):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" )
    print(" *  \\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af|  _____________          _____                          ___     __             *")
    print("  *  \\\\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af  |_____   _____|        | ____| ____    _    _    _    / | |   / /            *")
    print("   *  \\\\_______  __  ____   _  _ | | _____  _   _ ||____ | O  |   ||   \\\\  //   / /| |  / //\u00af//\u00af\u00af\u00af\u00af\u00af/  *")
    print("    *  \\______ \\ \\ \\ |   \\ | || || || ____|| | | || ____||  __|   ||___ \\\\//   / / | | / // // /\u00af\u00af\u00af   * ")
    print("     *    _____\\\\ \\ \\| |\\ \\| || || |||____ |  =  |||____ |   \\    | O | / /   / /  | |/ // // /___   * ")
    print("      *  |_______\\ \\___| \\___||_||_||_____||_| |_||_____||_|\\_\\   |___|/_/   /_/   |___//_//_____/  *")
    print(f"       *                        Edizione {str(edizione)}          Eseguito alle { InfoOra()}                      *" )
    print("        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  " )
    AggiornaStato(0)


def PrintaSwitcher(edizione=0):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" )
    print(" *  \\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af|  _____________             _____          *")
    print("  *  \\\\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af  |_____   _____|           / ____/ ____   *")
    print    ("   *  \\\\_______  __  ____   _  _ | | ______  __  __ //____ / O  /  *")
    print ("    *  \\______ \\ \\ \\ |   \\ | || || || _____// /_/ // ____//  __/  *")
    print("     *    _____\\\\ \\ \\| |\\ \\| || || |||____ / __  ///____ /   |   *")
    print   ("      *  |_______\\ \\___| \\___||_||_||____//_/ /_//_____//_/|_|  *")

    print(f"       *         Edizione {str(edizione)}   Eseguito alle { InfoOra()}         *" )
    print("        * * * * * * * * * * * * * * * * * * * * * * * * * * * *" )
    AggiornaStato(0, "Starting")

def AggiornaStato(x, comando="Boh!"):
    lunghBarra=len("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")-2
    n=int(x*lunghBarra/100)
    stringaEvo="        ["+"\u2593"*n+"\u2591"*(lunghBarra-n)+"]        "
    meta=int(len(stringaEvo)/2)
    perc=str(x)+"%"
    lperc=len(str(perc))
    dlx=int(lperc)

    stringaEvo = "        [" + "\u2593" * n + "\u2591" * (lunghBarra - n) + "]   Step:"

    stringaEvo=stringaEvo[:(meta-dlx)]+perc+stringaEvo[(meta-dlx+lperc):]



    print('',end='\r')
    if x >= 100:
        comando="Done"

    print(stringaEvo, comando, end='')


#TODO
####FineImport

if __name__ == '__main__':
    PrintaByNik()

    for i in range (101):
        AggiornaStato(i)
        time.sleep(0.05)
