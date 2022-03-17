from bs4 import BeautifulSoup
from requests import get


####InizioImport

def TitoloRep():
    URL = 'https://www.repubblica.it/'
    gtml_text = get(URL).text

    soup = BeautifulSoup(gtml_text, 'lxml')

    course_cards = soup.find('h2', class_='entry__title')
    titolo = course_cards.text.replace("  ", "").replace("\n", "")
    return (titolo)


def TitoloRepMondo():
    URL = 'https://www.repubblica.it/esteri/?ref=RHHD-MS'
    gtml_text = get(URL).text

    soup = BeautifulSoup(gtml_text, 'lxml')

    course_cards = soup.find('h2', class_='entry__title')
    titolo = course_cards.text.replace("  ", "").replace("\n", "")
    return (titolo)


def TitoloCor():
    URL = 'https://www.corriere.it/'
    gtml_text = get(URL).text

    soup = BeautifulSoup(gtml_text, 'lxml')

    course_cards = soup.find('section', class_='body-hp')
    course_cards = course_cards.find('h4')
    titolo = course_cards.text.replace("  ", "").replace("\n", "")
    return (titolo)


def TitoloAnsa():
    URL = 'https://www.ansa.it/sito/notizie/mondo/mondo.shtml?refresh_ce'
    gtml_text = get(URL).text

    soup = BeautifulSoup(gtml_text, 'lxml')

    course_cards = soup.find('div', class_='pp-inner')
    course_cards = course_cards.find('header')

    titolo = course_cards.text.replace("  ", "").replace("\n", "")
    return (titolo)

####FineImport