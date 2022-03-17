import matplotlib.pyplot as plt
import requests
import time

class APIOpenMeteo:
    '''
    Recap sulla classe:

    - Variabili principali
        self.th:            array dei tempi (in ore)
        self.td:            array dei tempi (in giorni)     [funzione per aggiungere questo dato: AggiungiPrecipitazioni()]
        self.txt:           array dei labels (in ore)
        self.tnow:          momento attuale in timeStamp
        self.T:             Temperatura  (ogni ora)
        self.prec:          precipitazioni                  [funzione per aggiungere questo dato: AggiungiPrecipitazioni()       ]
        self.precCum:       somma precipitazioni            [funzione per aggiungere questo dato: AggiungiPrecipitazioni()       ]
        self.Tperc:         Temperatura percepita           [funzione per aggiungere questo dato: AggiungiTemperaturaPercepita() ]
        self.relHum:        umidità relativa                [funzione per aggiungere questo dato: AggiungiTemperaturaRelHum()    ]
        self.wind10:        vento a 10m dal suolo           [funzione per aggiungere questo dato: AggiungiVento()                ]
        self.radSole:       radiazione solare diretta       [funzione per aggiungere questo dato: AggiungiRadSol()               ]
        self.tempSuolo:     temperatura del suolo           [funzione per aggiungere questo dato: AggiungiTempSuolo()            ]
        self.humSuolo:      umidità del suolo               [funzione per aggiungere questo dato: AggiungiUmidSuolo()            ]


    - Variabili secondarie
        self.latitude:      latitudine da analizzare
        self.longitude:     longitudine da analizzare
        self.gFuturi:       numero di giorni di forcast da importare
        self.gioPassati:    numero di giorni di dati passati da importare

    '''



    def __init__(self, (Lati,Longi), gF =7, gP=2):
        self.latitude   = Lati
        self.longitude  = Longi
        self.gFuturi    = gF
        self.gioPassati = gP
        self.tnow = time.time()

        # Ottiene il tempo nel formato ISO 8601
        urlIso = (
            f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly=temperature_2m&timezone=Europe%2FBerlin&past_days={str(self.gioPassati)}")

        # Ottiene il tempo in timestamp (secondi dall'epoca 0)
        urlTime = (
            f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly=temperature_2m&timeformat=unixtime&timezone=Europe%2FBerlin&past_days={str(self.gioPassati)}")

        data = requests.get(urlTime).json()
        text = requests.get(urlIso).json()

        self.th  = data['hourly']['time'][:(24*self.gioPassati+24*self.gFuturi)]
        self.txt = text['hourly']['time'][:(24*self.gioPassati+24*self.gFuturi)]
        self.T  = data['hourly']['temperature_2m'][:(24*self.gioPassati+24*self.gFuturi)]


    def AggiungiPrecipitazioni (self):
        # Ottiene le pecipitazioni in timestamp (secondi dall'epoca 0)
        urlTime = (
            f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly=precipitation&daily=precipitation_sum&timeformat=unixtime&timezone=Europe%2FBerlin&past_days={str(self.gioPassati)}")
        data = requests.get(urlTime).json()
        self.prec = data['hourly']['precipitation']
        self.td = data['daily']['time']
        self.precCum = data['daily']['precipitation_sum']


    def AggiungiTemperaturaPercepita(self):
        comando = "apparent_temperature"
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly={str(comando)}&past_days={str(self.gioPassati)}")
        data = requests.get(url).json()
        self.Tperc = data['hourly']['apparent_temperature']


    def AggiungiTemperaturaRelHum(self):
        comando = "relativehumidity_2m"
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly={str(comando)}&past_days={str(self.gioPassati)}")
        data = requests.get(url).json()
        self.relHum = data['hourly']['relativehumidity_2m']


    def AggiungiVento(self):
        comando = "windspeed_10m"
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly={str(comando)}&past_days={str(self.gioPassati)}")
        data = requests.get(url).json()
        self.wind10 = data['hourly']['windspeed_10m']


    def AggiungiRadSol(self):
        comando = "direct_radiation"
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly={str(comando)}&past_days={str(self.gioPassati)}")
        data = requests.get(url).json()
        self.radSole = data['hourly']['direct_radiation']


    def AggiungiTempSuolo(self):
        comando = "soil_temperature_0cm"
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly={str(comando)}&past_days={str(self.gioPassati)}")
        data = requests.get(url).json()
        self.tempSuolo = data['hourly']['soil_temperature_0cm']


    def AggiungiUmidSuolo(self):
        comando = "soil_moisture_0_1cm"
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={str(self.latitude)}&longitude={str(self.longitude)}&hourly={str(comando)}&past_days={str(self.gioPassati)}")
        data = requests.get(url).json()
        self.humSuolo = data['hourly']['soil_moisture_0_1cm']


if __name__ == '__main__':
    # lati = 41.903
    # longi = 12.48

    Roma = APIOpenMeteo ()
    Roma.AggiungiPrecipitazioni ()
    Roma.AggiungiTemperaturaRelHum ()
    Roma.AggiungiTemperaturaPercepita ()
    Roma.AggiungiVento ()
    Roma.AggiungiRadSol ()
    Roma.AggiungiTempSuolo ()
    Roma.AggiungiUmidSuolo ()


    plot = 0

    if plot == 1:

        plt.figure(figsize=(12, 6))
        plt.plot(Roma.x, Roma.humSuolo, lw=1, c='red')
        # plt.plot(Xprec, Yprec, lw=1, c='blue')
        # plt.plot(Xcpr, Ycpr, lw=1, c='black')

        plt.axvline(Roma.tnow, c='red', lw=2)

        i = 0
        xt = []
        tt = []
        while i < len(Roma.x):
            xt.append(Roma.x[i])
            tt.append(Roma.txt[i][:10])
            i += 24

        xt.append(Roma.x[-1])
        tt.append(Roma.txt[-1])
        for xxt in xt:
            plt.axvline(xxt, c='blue', lw=1, ls='--')

        plt.xticks(xt, tt)
        plt.xlim(Roma.x[0], Roma.x[-1])
        # plt.savefig('test.png', transparent=True)
        plt.show()



    printAll=0


    if printAll == True:

        stringaCSV = 'time, timeISO, temperature, Tperc, HumRel, wind10, radSole, tempSuolo, humSuolo\n'
        for i in range(len(Roma.x)):
            stringaCSV += str(Roma.x[i]) + ', ' + str(Roma.txt[i]) + ', ' + str(Roma.T[i]) + ', ' + str(Roma.Tperc[i]) + ', ' + str(Roma.relHum[i]) + ', ' + str(Roma.wind10[i]) + ', ' + str(Roma.radSole[i]) + ', ' + str(Roma.tempSuolo[i]) + ', ' + str(Roma.humSuolo[i]) + '\n'

        print(stringaCSV)
