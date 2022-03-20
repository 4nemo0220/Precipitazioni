from bs4 import BeautifulSoup
from requests import get

def AssicuraTesto( valore):
    if valore == None: valore="N.I."
    else: valore.text

def InfoMeteo(luogo="Roma Centro Borgo"):

    if luogo=="Roma Centro Borgo":
        URL="https://www.ilmeteo.it/meteo/Roma%20centro%20Borgo"
    else:

        URL="https://www.ilmeteo.it/meteo/"

        for i in range(len(luogo.split())):
            if i!=0: URL+='+'
            URL +=luogo.split()[i]
        if __name__ == '__main__': print(URL)




    gtml_text = get(URL).text

    soup = BeautifulSoup(gtml_text, 'lxml')
    course_cards = soup.find('table', class_='datatable')
    rigaRadar = course_cards.find('tr', class_='situa2 radar-data')
    infoLoc = soup.find('div', class_='infoloc').text.replace('°', '').split("\n")[5].split(" ") #Lati = infoLoc[1] & Longi = infoLoc[3]


    riga = rigaRadar.find_all('td')


    ora = riga[0].text
    meteo = riga[2].text
    prec = riga[5].text

    rigaPrev = course_cards.find('tr', class_='dark')

    colonne = rigaPrev.find_all('td')

    # if __name__ == '__main__':
    #     for i in range(len(colonne)):
    #         print(i,colonne[i])
    #
    #     s=6
    #     print(type( colonne[s]))
    #
    #     if type( colonne[s]) == "class 'bs4.element.Tag'":
    #         print("Si")
    #     else: print("No")
    #
    #     print("--",colonne[s].text,"--", sep='')

    #Ora del Forecast
    if colonne[0] == None: oraF = "??"
    else: oraF = colonne[0].text

    # Previsioni Imminenti (su questo val si basa la scelta delle img)
    meteoF = AssicuraTesto(colonne[2])
    if colonne[2] == None:  meteoF = "??"
    else:  meteoF = colonne[2].text

    # Pevisione temperatura
    if colonne[3] == None: tempF = "??"
    else: tempF = colonne[3].text

    # Previsione Precipitazioni
    if len(colonne)>=6:
        # print("---->",colonne[6].text,"<------", sep='')

        if colonne[6] == None: precipitazioniF = "Prec=?"
        else:
            if len(colonne[6].text)== None: precipitazioniF="Prec=??"
            else:
                colonne[6] = colonne[6].text
                while colonne[6][0] == ' ': colonne[6] = colonne[6][1:]

                # print("---->", colonne[6], "<------", sep='')


                precipitazioniF = colonne[6]
                if " " in precipitazioniF:
                    precipitazioniF = precipitazioniF.split()[1]
                else: precipitazioniF="Prec=???"
    else: precipitazioniF="Prec=????"


    # Previsione vento
    if colonne[5] == None: ventoF = "??"
    else: ventoF = AssicuraTesto(colonne[5].find('abbr'))

    # Previsioni Umidità relativa
    if len(colonne) >= 10:
        if colonne[10] == None: urF = "??"
        else: urF = colonne[10].text[:-1]
    else:
        urF = "???"

    stampa = ['', '', '', '']
    stampa[
        0] = f'{luogo}: {meteoF}\n({ora}): {meteo} di {prec};\n({oraF}): {meteoF}, {tempF}, {precipitazioniF}, {ventoF} km/h, {urF};'#= f'{luogo}: {meteoF}\n({ora}): {meteo} di {prec};\n({oraF}): {meteoF}, {tempF},  {ventoF} km/h, {urF};'

    stampa[1] = meteoF
    stampa[2] = tempF
    stampa[3] = (infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)

    if luogo=="Roma Centro Borgo":
        stampa[3] = (41.9035, 12.48)


    return (stampa)

# VECCHIA FUNZIONE
# def InfoMeteo(URL, luogo):
#     gtml_text = get(URL).text
#
#     soup = BeautifulSoup(gtml_text, 'lxml')
#
#     course_cards = soup.find('table', class_='datatable')
#
#     rigaRadar = course_cards.find('tr', class_='situa2 radar-data')
#
#     infoLoc = soup.find('div', class_='infoloc').text.replace('°', '').split("\n")[5].split(" ") #Lati = infoLoc[1] & Longi = infoLoc[3]
#
#
#     riga = rigaRadar.find_all('td')
#
#     ora = riga[0].text
#     meteo = riga[2].text
#     prec = riga[5].text
#
#     rigaPrev = course_cards.find('tr', class_='dark')
#
#     colonne = rigaPrev.find_all('td')
#
#     oraF = colonne[0].text
#     meteoF = colonne[2].text
#     tempF = colonne[3].text
#     precipitazioniF = colonne[6].text
#     ventoF = colonne[5].find('abbr').text
#     urF = colonne[10].text[:-1]
#
#     stampa = ['', '', '', '']
#     stampa[
#         0] = f'{luogo}: {meteoF.upper()}\n({ora}): {meteo} di {prec};\n({oraF}): {meteoF}, {tempF}, {precipitazioniF.split()[1]}, {ventoF} km/h, {urF};'
#     stampa[1] = meteoF
#     stampa[2] = tempF
#     stampa[3] = (infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)
#     return (stampa)




if __name__ == '__main__':
    Roma = InfoMeteo("Roma")

    print("Roma[0]: ",Roma[0])
    print("Roma[1]: ", Roma[1])
    print("Roma[2]: ", Roma[2])
    print("Roma[3]: ", Roma[3])