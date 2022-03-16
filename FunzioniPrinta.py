# -*- coding: utf-8 -*-
"""
FUNZIONI DI STAMPA
@author: Nicolò Nardi
14/12/2021
"""


# DEFINIZIONE FUNZIONI E VARIABILI PER LA STAMPA SU SCHERMO ----------------------------------------------
#
#   1) Funzione "Avvia()"    : avvia  il programma stampando su schermo un quadraatoo con la scritta START
#   2) Funzione "Concludi()" : chiude il programma stampando su schermo un quadraatoo con la scritta END
#   3) Funzione "Printa()"   : facilita la stampa di stringhe su schermo (per più info vedi descrizione)
#
#---------------------------------------------------------------------------------------------------------

# Definizione variabili globali per la stampa su schermo

livello = 1     # necessaria a capire "quanto profondo" stia operando il programma
pr=True         # necessaria a sapere se si vuole o meno un feedback su sckermo

# 1) Funzione "Avvia()" 
def Avvia():    
    print ("\n\n*********\n* START * \n*********\n|", end="")
    if pr== True: print("\n|\n|", end="")
    
#2) Funzione "Concludi()"
def Concludi():
    if pr== True: 
        print("\n|\n|", end="")    
    print ("\n|\n*********\n*  END  *\n*********\n");
    

#3) Funzione "Printa()"    
def Printa ( compito, stringa):
    """
    Funzione pensata per migliorare gli output su schermo.
    
    Parameters
    ----------
    compito : tipo intero 
         2 ---> annuncia l'inizio di una funzione esterna printandone il nome (var. stringa)
         1 ---> printa la strina in funzione del livello del programa
         0 ---> conclude il livello attuale con esito positivo
        -1 ---> conclude il livello attuale con esito negativo
    
    stringa : tipo stringa
        Stringa da printare, serve solo se compito == 1!

    Returns
    -------
    None.

    """    
    global livello, pr;  
    
    if pr== True: print("") 
    
    if compito == 2:
        for i in range(livello):  
            if pr== True: print("|\t", end='')   
        if pr== True: print("")
        livello +=1
        for i in range(livello-1):  
            if pr== True: print("|\t", end='')    
        if pr== True: print("|----- AVVIO DELLA FUNZIONE:",stringa, end='')
        
    if compito == 1:
            for i in range(livello):  
                if pr== True: print("|\t", end='')    
            if pr== True: print(stringa, end='')
        
    if compito == 0 or compito == -1:
        for i in range(livello-1):  
            if pr== True: print("|\t", end='')    
        if pr== True: print("|----- FUNZIONE CONCLUSA, ESITO:", end='')
        if compito == 0 and pr== True: print("\t[OK]", end='')
        if compito == -1 and pr== True: print("\t[ERR]", end='')
        livello-=1;
        if pr== True: print("")
        for i in range(livello):  
            if pr== True: print("|\t", end='')   

# FINE DEFINIZIONE FUNZIONI E VARIABILI PER LA STAMPA SU SCHERMO ----------------------------------------------



if __name__ == '__main__':

    # Esempio
    Avvia()
    Printa(1, "tutto molto bello")
    Printa(2,"Testina")
    Printa(1, "tutto molto bello")
    Printa(1, "tutto molto molto bello")
    Printa(2,"Nuova")
    Printa(1, "tutto molto molto bello")
    Printa(0,"Nuova")

    Printa(1, "tutto molto bello")
    Printa(1, "tutto molto molto bello")

    Printa(-1,"Nuova")

    Printa(1, "tutto molto bello")
    Printa(1, "tutto molto molto bello")
    Concludi()
