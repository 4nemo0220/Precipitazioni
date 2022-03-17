####InizioImport

def InfoOra():
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return(current_time)

####FineImport

if __name__ == '__main__':
    print(InfoOra())