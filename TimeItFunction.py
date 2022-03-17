import time
import timeit
from requests import get
import statistics as st
from FunzioniIlMeteo import *

def FunzioneDaRipetere():
    URL="https://www.ilmeteo.it/meteo/Roma+centro+Campo+Marzio?refresh_ce"
    gtml_text = get(URL).text


if __name__ == '__main__':

    numb=1

    start= time.time()

    time_costs = timeit.repeat(
        stmt    = "InfoMeteo()",
        repeat  = 50,  # numero di cicli che deve eseguire
        number  =numb,  # numero di volte in cui va ripetuta la funzione in ogni ciclo
        setup   = "from FunzioniIlMeteo import InfoMeteo"  # varie ed eventuali funzioni da importare

    )

    print(f"In totale ci ha messo {time.time()-start} secondi.")

    # print(f"La funzione ritorna una list contenente i tempi impiegati per ogni ciclo di controllo:\n {time_costs}")
    print(f"Tempo medio impiegato per un'esecuzione: {st.mean(time_costs)/numb}")
