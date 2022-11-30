def contaIncasso(nome_file):
    file = open(nome_file, "r")
    lista_righe = file.readlines()
    file.close()

    tot=0

    for riga in lista_righe[:]:
        riga_senza_linefeed= riga[:-1]#creo le stringa senza \n
        lista_campi = riga_senza_linefeed.split(";")#inserirsco in una lista i campi desiderati
        #print(lista_campi)
        tot=tot+int(lista_campi[2])
    
    return tot

def verificaQuota(nome_file):
    file = open(nome_file, "r")
    lista_righe = file.readlines()
    file.close()

    tot=0

    for riga in lista_righe[:]:
        riga_senza_linefeed= riga[:-1]#creo le stringa senza \n
        lista_campi = riga_senza_linefeed.split(";")#inserirsco in una lista i campi desiderati
        if(lista_campi[1]=="Serra"):
            tot=tot+int(lista_campi[2])
    
    return tot

def main():
    tot=contaIncasso("4AROB_GITA.CSV")
    if(tot<2200):
        print(f"mancano :", (2200-tot))
    if(tot==2200):
        print("quota pagata regolarmente")
    if(tot>2200):
        print("eccesso :", (tot-2200))

    quota=verificaQuota("4AROB_GITA.CSV")
    if(quota<100):
        print(f"mancano :", (100-tot))
    if(quota==100):
        print("quota pagata regolarmente")
    if(quota>100):
        print("eccesso :", (tot-100))


