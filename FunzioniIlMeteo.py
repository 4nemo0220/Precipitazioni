from bs4 import BeautifulSoup
from requests import get


def InfoMeteo(URL, luogo):
    gtml_text = get(URL).text

    soup = BeautifulSoup(gtml_text, 'lxml')

    course_cards = soup.find('table', class_='datatable')

    rigaRadar = course_cards.find('tr', class_='situa2 radar-data')

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

    stampa = ['', '', '']
    stampa[
        0] = f'{luogo}: {meteoF.upper()}\n({ora}): {meteo} di {prec};\n({oraF}): {meteoF}, {tempF}, {precipitazioniF.split()[1]}, {ventoF} km/h, {urF};'
    stampa[1] = meteoF
    stampa[2] = tempF
    return (stampa)
