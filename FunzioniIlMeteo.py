from bs4 import BeautifulSoup
from requests import get


def InfoMeteo(luogo="Roma"):

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

    oraF = colonne[0].text
    meteoF = colonne[2].text
    tempF = colonne[3].text
    precipitazioniF = colonne[6].text
    ventoF = colonne[5].find('abbr').text
    urF = colonne[10].text[:-1]

    stampa = ['', '', '', '']
    stampa[
        0] = f'{luogo}: {meteoF.upper()}\n({ora}): {meteo} di {prec};\n({oraF}): {meteoF}, {tempF}, {precipitazioniF.split()[1]}, {ventoF} km/h, {urF};'
    stampa[1] = meteoF
    stampa[2] = tempF
    stampa[3] = (infoLoc[1], infoLoc[3]) # ------> (Lati, Longi)
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
    Roma = InfoMeteo("Belmonte in sabina")

    print("Roma[0]: ",Roma[0])
    print("Roma[1]: ", Roma[1])
    print("Roma[2]: ", Roma[2])
    print("Roma[3]: ", Roma[3])