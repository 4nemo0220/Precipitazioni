from FunzioneInfoOra  import InfoOra
import time

####InizioImport

def PrintaByNik(edizione):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" )
    print(" *  \\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af|  _____________          _____                          ___     __             *")
    print("  *  \\\\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af  |_____   _____|        | ____| ____    _    _    _    / | |   / /            *")
    print("   *  \\\\_______  __  ____   _  _ | | _____  _   _ ||____ | O  |   ||   \\\\  //   / /| |  / //\u00af//\u00af\u00af\u00af\u00af\u00af/  *")
    print("    *  \\______ \\ \\ \\ |   \\ | || || || ____|| | | || ____||  __|   ||___ \\\\//   / / | | / // // /\u00af\u00af\u00af   * ")
    print("     *    _____\\\\ \\ \\| |\\ \\| || || |||____ |  =  |||____ |   \\    | O | / /   / /  | |/ // // /___   * ")
    print("      *  |_______\\ \\___| \\___||_||_||_____||_| |_||_____||_|\\_\\   |___|/_/   /_/   |___//_//_____/  *")
    print(f"       *                        Edizione {str(edizione)}          Eseguito alle { InfoOra()}                      *" )
    print("        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  " )
    print("        [","\u2591"*87,"]  ", sep='', end='')


def PrintaSwitcher(edizione):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" )
    print(" *  \\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af|  _____________             _____          *")
    print("  *  \\\\\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af\u00af  |_____   _____|           / ____/ ____   *")
    print    ("   *  \\\\_______  __  ____   _  _ | | ______  __  __ //____ / O  /  *")
    print ("    *  \\______ \\ \\ \\ |   \\ | || || || _____// /_/ // ____//  __/  *")
    print("     *    _____\\\\ \\ \\| |\\ \\| || || |||____ / __  ///____ /   |   *")
    print   ("      *  |_______\\ \\___| \\___||_||_||____//_/ /_//_____//_/|_|  *")

    print(f"       *         Edizione {str(edizione)}   Eseguito alle { InfoOra()}           *" )
    print("        * * * * * * * * * * * * * * * * * * * * * * * * * * * *" )
    print("        [","\u2591"*87,"]  ", sep='', end='')

def AggiornaStato(x):
    n=int(x*87/100)
    print('',end='\r')
    print("        ["+"\u2593"*n+"\u2591"*(87-n)+"]  ", end='')

####FineImport

if __name__ == '__main__':
    PrintaSwitcher(0)

    # for i in range (100):
    #     AggiornaStato(i)
    #     time.sleep(1)
