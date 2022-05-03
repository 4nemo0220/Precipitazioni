from bs4 import BeautifulSoup
from requests import get

def AssicuraTesto( valore):
    if valore == None: valore="N.I."
    else: valore.text

def InfoMeteo(luogo="Roma Centro Borgo"):
    '''
    Questa funziona ritorna una list contenente i dati relativi al meteo.
    :param luogo: la stringa che definisce il luogo da analizzare
            NB: se la def è "Roma Centro Borgo" userà l'url pre-impostato;
    :return:
        stampa[0]: la stringona da stampare sull'img finale contenente tutte le info
        stampa[1]: il meteo previsto
        stampa[2]: la temperatura prevista
        stampa[3]: una tupla contenente (Lati, Longi)
    '''

    if luogo=="Roma Centro Borgo":
        URL="https://www.ilmeteo.it/meteo/Roma%20centro%20Borgo"
    elif luogo=="Belmonte":
        URL="https://www.ilmeteo.it/meteo/Belmonte+in+Sabina"
    else:

        URL="https://www.ilmeteo.it/meteo/"

        for i in range(len(luogo.split())):
            if i!=0: URL+='+'
            URL +=luogo.split()[i]
        if __name__ == '__main__': print("L'URL da cui andrò a prendere le info sul meteo è:", URL)



    # Importo la pag
    try:
        gtml_text = get(URL).text
        soup = BeautifulSoup(gtml_text, 'lxml')
    except:
        if __name__ == '__main__':
            print("C'è stato un errore nel ottenere dal sito le info. Procedo con i valori di default.")
        stampa[0]="C'è stato un errore nel ottenere dal sito le info. Procedo con i valori di default."
        stampa[1]= "serenissimo"
        stampa[2]= 0
        stampa[3] = (41.9035, 12.48)
        return stampa

    # Seleziono la tabella del meteo
    try:
        course_cards = soup.find('table', class_='datatable')
    except:
        if __name__ == '__main__':
            print(
                "C'è stato un errore nell'identificare la tabella dei dati dal meteo. Procedo con i valori di default.")
        stampa[
            0] = "C'è stato un errore nell'identificare la tabella dei dati dal meteo. Procedo con i valori di default."
        stampa[1] = "serenissimo"
        stampa[2] = 0
        stampa[3] = (41.9035, 12.48)
        return stampa


    # Seleziono la riga del radar meteo
    try:
        rigaRadar = course_cards.find('tr', class_='situa2 radar-data riga-situazione-realtime')
        if (rigaRadar)==None:
            if __name__ == '__main__': print(
                "ERR: nell'acquisizione della riga radar meteo. Passo all'acquisizione della riga metar.")

            rigaRadar = course_cards.find('tr', class_='situa2 metar-dati riga-situazione-realtime')
            if (rigaRadar) == None:
                if __name__ == '__main__': print(
                    "ERR: nell'acquisizione della riga metar. NON SO CHE FARE!.")

    except:
        if __name__ == '__main__':
            print(
                "ERR: nell'identificare delle info dal radar del meteo. Procedo con i valori di default.")
        stampa[
            0] = "C'è stato un errore nell'identificare delle info dal radar del meteo. Procedo con i valori di default."
        stampa[1] = "serenissimo"
        stampa[2] = 0
        stampa[3] = (41.9035, 12.48)
        return stampa

    # Inizializzo la list che ritornerà i dati indietro
    stampa = ['', '', '', '']



    # METEO FORECASTED
    # Definizione PrevisioniMeteo
    try:
        stampa[1] = course_cards.find('tr', class_='dark')
        stampa[1] = stampa[1].find('td', class_='col3').text
        if __name__ == '__main__':
            print("stampa[1] ---> La stringa  sulle previsioni è: -", stampa[1], "-", sep='')

    except:
        if __name__ == '__main__': print(
            "ERR: nell'identificazione delle previsioni meteo assegno la previsione 'serenxissimo'.")
        stampa[1] = "???"

    # TEMPERATURA FORECASTED
    # Definizione Temperatura prevista
    try:
        stampa[2] = course_cards.find('tr', class_='dark')
        stampa[2] = stampa[2].find('td', class_='col4').text
        if __name__ == '__main__':
            print("stampa[2] ---> La stringa sulla temperatura prevista è: -", stampa[2], "-", sep='')

    except:
        if __name__ == '__main__': print(
            "ERR: nell'identificazione della temperatura prevista, assegno la temperatura '???°'.")
        stampa[2] = "???°"


    # ORA FORECASTED
    # Definizione ora per le previsioni prevista
    try:
        oraF = course_cards.find('tr', class_='dark')
        oraF = oraF.find('td', class_='f').text
        if __name__ == '__main__':
            print("oraF      ---> La stringa sull'ora delle previsioni è: -", oraF, "-", sep='')

    except:
        if __name__ == '__main__': print(
            "ERR: sull'ora delle previsioni, assegno il valore '???°'.")
        oraF = "???°"


    # VENTO FORECASTED
    # Definizione vento previst
    try:
        ventoF = course_cards.find('tr', class_='dark')
        ventoF = ventoF.find('td', class_='col6')
        ventoF = ventoF.find('abbr', style='cursor:help').text
        if __name__ == '__main__':
            print("ventoF    ---> La stringa sul vento previsto è: -", ventoF, "-", sep='')

    except:
        if __name__ == '__main__': print(
            "ERR: nell'identificazione del vento previsto, assegno li valore '???'.")
        ventoF = "???"


    # PRECIPITAZIONI FORECASTED
    # Definizione precipitazioni previste
    try:
        precF = course_cards.find('tr', class_='dark')
        precF = (precF.find('td', class_='col7').text).split()[1]
        if __name__ == '__main__':
            print("precF     ---> La stringa sulle precipitazioni previste (forecasted) è: -", precF, "-", sep='')

    except:
        if __name__ == '__main__': print(
            "ERR: nell'identificazione delle precipitazioni, assegno il valore '???'.")
        precF = "???"

    # UMIDITA' FORECASTED
    # Definizione umidità prevista
    try:
        urF = course_cards.find('tr', class_='dark')
        urF = (urF.find('td', class_='col11').text).split('%')[0]+'%'
        if __name__ == '__main__':
            print("urF       ---> La stringa sul'umidità relativa prevista è: -", urF, "-", sep='')

    except:
        if __name__ == '__main__': print(
            "ERR: nell'identificazione dell'umità relavtiva, assegno l'umidità '???'.")
        urF = "???"





    # ORA RADAR
    # Definizione ora attuale
    try:
        oraR = (rigaRadar.text).split()[0]
        if __name__ == '__main__': print("oraR      ---> la stringa sull'ora del radar è: -", oraR, "-", sep='')
    except:
        if __name__ == '__main__': print(
            "ERR: nell'attribuzione della variabile ora, assegno il valore '???'.")
        oraR = "???x"


    # Meteo RADAR
    # Definizione delle pprevisioni (attuali)
    try:
        MeteoR = rigaRadar.find('td', class_='col3').text
        if __name__ == '__main__': print("MeteoR    ---> La stringa sul meteo attuale è: -", MeteoR, "-", sep='')
    except:
        if __name__ == '__main__': print("ERR: nell'attribuzione del stringa sul meteo attuale, assegno il valore '???'.")
        MeteoR = "????"




    # LATI LONGII
    # Definizione latitudine e longitudine
    try:
        infoLoc = soup.find('div', class_='infoloc').text.replace('°', '').split("\n")[5].split(" ") #Lati = infoLoc[1] & Longi = infoLoc[3]
        stampa[3] = (infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)
        if luogo=="Gambero" or luogo == "Coronari": stampa[3] = (41.9035, 12.48)
        elif luogo == "Belmonte" or "Convento": stampa[3] = (42.321, 12.8845)
        else: stampa[3] = (infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)
        if __name__ == '__main__':
            print("stampa[3] ---> il touple con le info sulla pos è: -",stampa[3], "-", sep='')
    except:
        if __name__ == '__main__': print("ERR: nell'attribuzione delle variabili latitudine e longitudine. Assegno quelle per roma.")
        stampa[3] = (41.9035, 12.48)


    # PRECIPITAZIONI RADAR
    # Definizione delle precipitazioni (attuali)
    try:
        precR = rigaRadar.find('td', class_='col6').text
        if __name__ == '__main__': print("precR     ---> La stringa sulle precipitazioni attuali è: -", precR, "-", sep='')
    except:
        if __name__ == '__main__': print("ERR: nell'attribuzione della definizione dello stato delle precipitazioni, assegno il valore '???'.")
        precR = "????"

    stampa[0] =f'{luogo}: {stampa[1].upper()}\n'
    if oraR != "???x": stampa[0] += f'({oraR}): {MeteoR} di {precR};\n({oraF}): {stampa[1]}, {stampa[2]}, {precF}, {ventoF} km/h, {urF};\n'
    elif oraF != "???":  stampa[0] += f'({oraF}): {stampa[1]}, {stampa[2]}, {precF}, {ventoF} km/h, {urF};'

    #                       meteoF
    return stampa







if __name__ == '__main__':
    InfoMeteo("Roma")