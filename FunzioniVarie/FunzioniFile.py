def OttieniLuogoDaFile():
    path="C:/Users/coand/Google Drive/PC/Immagini/Switcher/Luogo.txt"
    with open(path) as f:
        lines = f.readlines()
        # print(lines[0])

    return lines [0][0:-1]

if __name__ == '__main__':
    print( OttieniLuogoDaFile(), '-', sep='')