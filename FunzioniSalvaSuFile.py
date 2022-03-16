


def SaveAsCSV(stringa, nomefile = "nome.txt"):
    # open the file in the write mode
    with open(nomefile, "w") as f:
        f.write(stringa)

