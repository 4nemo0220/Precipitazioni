from datetime import datetime
import os
import shutil

def StudiaMain(lines, Moduli):
    stampa=False
    i=0
    while i<len(lines):
        if stampa==True: print("Analizzo la linea numero [", i, "]: ", lines[i], sep='', end='')

        if "edizione= " in lines[i]:
            lines.pop(i)
            lines.insert(i, "edizione= " + str(edizione)+"\n")
            if stampa==True: print("--------> La sostituisco con: ", lines[i], sep='', end='')

        if "from " in lines[i]  or "import" in lines[i]   :

            if "from Funzioni" in lines[i]:


                da = lines[i].split(' import ')[0].split(' ')[1]
                ImportaFunzioniEsterne(da)

                lines.pop(i)
                lines.insert(i, "# Importo dal file denominato '"+da+".py ---------------------------------------------------------\n")
                if stampa==True: print("--------> La sostituisco con: ", lines[i], sep='', end='')
                i+=1


                importate=ImportaFunzioniEsterne(da)

                for k in range(len(importate)):
                    lines.insert(i, importate[k])
                    if stampa==True: print("Aggiungo la linea numero [", i, "]: ", lines[i], sep='', end='')
                    i+=1



                lines.insert(i, "# Fine import dal file denominato '"+da+".py ---------------------------------------------------------\n")
                if stampa==True: print("Aggiungo la linea numero [", i, "]: ", lines[i], sep='', end='')

        i+=1
    return lines


def ImportaMain(edizione):
    with open('FunzioniVarie\MAIN.py') as f:
        lines = f.readlines()
    return lines





def ImportaFunzioniEsterne (nomeFile):
    #print("Importo tuttecose da", nomeFile)

    with open("FunzioniVarie\\" + nomeFile + ".py") as ff:
        flines = ff.readlines()

    linesFunzione = []
    imp=False
    for k in range(len(flines)):
        if "####InizioImport" in flines[k]:
            imp = True
            k+=1
        if "####FineImport" in flines[k]: imp = False

        if imp == True:
            linesFunzione.append(flines[k])

    return linesFunzione

def AggiornaFileComando(versione):
    with open('comando.txt') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        # print(lines[i], end='')
        if "Versione:" in lines[i]:
            if (int(lines[i].split()[1])) == versione:
                print("",end='')
            else:
                lines.pop(i)
                lines.insert(i, "Versione: " + str(versione)+'\n')

            print("Numero versione:",versione)

        if "Edizione:" in lines[i]:
            edizione= int(lines[i].split()[1]) +1

            lines.pop(i)
            lines.insert(i, "Edizione: " + str(edizione) + '\n')
            print("Numero edizione:",edizione)

        if "XXXXX" in lines[i]:
            nuovonome="Switcher_"+str(versione)+'_'+str(edizione)+".py"
            punto=lines[i].index("XXXXX")

            stringaComando= lines[i][:punto]+nuovonome+lines[i][(punto+len("XXXXX")):]

    with open('comando.txt', "w") as f:
        for l in lines:
            f.write(l)

    return edizione, stringaComando


def CreabackUp(versione, edizione,my_date, nomeProgramma ):

    # Creo La macro Cartella

    parent_dir = "C:/Users/coand/Google Drive/PC/Documenti/111 Programmazione/000 Python/BackupPyCharm/"

    path = parent_dir+nomeProgramma

    # Check whether the specified path exists or not
    if os.path.exists(path)== False: os.mkdir(path);

    path = parent_dir+ "/" + nomeProgramma+ "/" + nomeProgramma + "_" + str(versione) + '_' + str(edizione)

    print("\nCreao un BackUp nella cartella:\t",path, end='')

    source_dir = r"FunzioniVarie"
    destination_dir= path

    shutil.copytree(source_dir, destination_dir)

    with open('comando.txt', "a") as f:
        f.write("Swticher_"+ str(versione)+ "_"+ str(edizione)+"\t-------->\t"+str(my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')) +'\n')



def CreaExe(stringaComando):
    print("\n\nPer creare l'exe esegui il seguente comando:", ">>> " + stringaComando, sep='\n')





def AggiornaExe ():
    dest_dir = r"C:/Users/coand/Google Drive/PC/Immagini/Switcher/dist/prog001.exe"
    part_dir=os.getcwd()+"\FunzioniVarie\dist\MAIN.EXE"

    shutil.copyfile(part_dir, dest_dir)



def CancellaCartelleInutili():



    dir_path = os.getcwd() + "\\FunzioniVarie\\build"

    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))

    dir_path= os.getcwd() + "\\FunzioniVarie\\__pycache__"

    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))


if __name__ == '__main__':
    CancellaCartelleInutili()
