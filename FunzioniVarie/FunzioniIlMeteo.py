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
        stampa[2]: la pemperatura prevista
        stampa[3]: una tupla contenente (Lati, Longi)
    '''

    if luogo=="Roma Centro Borgo":
        URL="https://www.ilmeteo.it/meteo/Roma%20centro%20Borgo"
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
    except:
        if __name__ == '__main__':
            print(
                "C'è stato un errore nell'identificare delle info dal radar del meteo. Procedo con i valori di default.")
        stampa[
            0] = "C'è stato un errore nell'identificare delle info dal radar del meteo. Procedo con i valori di default."
        stampa[1] = "serenissimo"
        stampa[2] = 0
        stampa[3] = (41.9035, 12.48)
        return stampa

    # Inizializzo la list che ritornerà i dati indietro
    stampa = ['', '', '', '']

    # Definizione ora attuale
    try:
        ora = (rigaRadar.text).split()[0]
        if __name__ == '__main__': print("La stringa sull'ora è: --->",ora,"<---", sep='')
    except:
        if __name__ == '__main__': print(
            "C'è stato un errore nell'attribuzione della variabile ora, assegno il valore '???'.")
        ora = "???"

    # Definizione PrevisioniMeteo
    try:
        stampa[1] = course_cards.find('tr', class_='dark')
        stampa[1] = stampa[1].find('td', class_='col3').text
        if __name__ == '__main__':
            print("La stringa sulle previsioni è: --->", stampa[1], "<---", sep='')

    except:
        if __name__ == '__main__': print(
            "C'è stato un errore nell'identificazione delle previsioni meteo assegno la previsione 'serenxissimo'.")
        stampa[1] = "???"


    # Definizione delle precipitazioni
    try:
        precipitazioni = rigaRadar.find('td', class_='col3').text
        if __name__ == '__main__': print("La stringa sulle precipitazioni è: --->", precipitazioni, "<---", sep='')
    except:
        if __name__ == '__main__': print("C'è stato un errore nell'attribuzione della definizione dello stato delle precipitazioni, assegno il valore '???'.")
        precipitazioni = "????"



    # Definizione latitudine e longitudine
    try:
        infoLoc = soup.find('div', class_='infoloc').text.replace('°', '').split("\n")[5].split(" ") #Lati = infoLoc[1] & Longi = infoLoc[3]
        stampa[3] = (infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)
        if luogo=="Roma Centro Borgo": stampa[3] = (41.9035, 12.48)
        else: stampa[3] = (infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)
        if __name__ == '__main__':
            print("La list contenente le info sulla Latitudine e la longitudine è: \n--->",infoLoc, "<---", sep='')
            print("E i valori scelti sono: Lati = ", stampa[3][0],", Longi = ",stampa[3][0],".", sep='' )
    except:
        if __name__ == '__main__': print("C'è stato un errore nell'attribuzione delle variabili latitudine e longitudine. Assegno quelle per roma.")
        stampa[3] = (41.9035, 12.48)
    stampa[0] = "FINENDA"
    return stampa













    # riga = rigaRadar.find_all('td')

    #
    # ora = riga[0].text
    # meteo = riga[2].text
    # prec = riga[5].text
    #
    # rigaPrev = course_cards.find('tr', class_='dark')
    #
    # colonne = rigaPrev.find_all('td')

    #
    #
    # #Ora del Forecast
    # if colonne[0] == None: oraF = "??"
    # else: oraF = colonne[0].text
    #
    # # Previsioni Imminenti (su questo val si basa la scelta delle img)
    # meteoF = AssicuraTesto(colonne[2])
    # if colonne[2] == None:  meteoF = "??"
    # else:  meteoF = colonne[2].text
    #
    # # Pevisione temperatura
    # if colonne[3] == None: tempF = "??"
    # else: tempF = colonne[3].text
    #
    # # Previsione Precipitazioni
    # if len(colonne)>=6:
    #     # print("---->",colonne[6].text,"<------", sep='')
    #
    #     if colonne[6] == None: precipitazioniF = "Prec=?"
    #     else:
    #         if len(colonne[6].text)== None: precipitazioniF="Prec=??"
    #         else:
    #             colonne[6] = colonne[6].text
    #             while colonne[6][0] == ' ': colonne[6] = colonne[6][1:]
    #
    #             # print("---->", colonne[6], "<------", sep='')
    #
    #
    #             precipitazioniF = colonne[6]
    #             if " " in precipitazioniF:
    #                 precipitazioniF = precipitazioniF.split()[1]
    #             else: precipitazioniF="Prec=???"
    # else: precipitazioniF="Prec=????"
    #
    #
    # # Previsione vento
    # if colonne[5] == None: ventoF = "??"
    # else: ventoF = AssicuraTesto(colonne[5].find('abbr'))
    #
    # # Previsioni Umidità relativa
    # if len(colonne) >= 10:
    #     if colonne[10] == None: urF = "??"
    #     else: urF = colonne[10].text[:-1]
    # else:
    #     urF = "???"
    #
    #
    # stampa[
    #     0] = f'{luogo}: {meteoF}\n({ora}): {meteo} di {prec};\n({oraF}): {meteoF}, {tempF}, {precipitazioniF}, {ventoF} km/h, {urF};'#= f'{luogo}: {meteoF}\n({ora}): {meteo} di {prec};\n({oraF}): {meteoF}, {tempF},  {ventoF} km/h, {urF};'
    #
    # stampa[1] = meteoF
    # stampa[2] = tempF

    #
    # # return (stampa)



if __name__ == '__main__':
    InfoMeteo("Roma")
    #
    # print("Roma[0]: ",Roma[0])
    # print("Roma[1]: ", Roma[1])
    # print("Roma[2]: ", Roma[2])
    # print("Roma[3]: ", Roma[3])