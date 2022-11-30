"""
file = open("./file.csv", "r")

lista_righe = file.readlines()

file.close()

print(lista_righe)

for riga in lista_righe:
    print(riga[:-1])#stampo tutto tranne il carattere \n

for riga in lista_righe[1:]:#parto dalla seconda riga
    print(riga[:-1])#stampo tutto tranne il carattere \n

diz_matematici= {"id": [], "nomi": []}

for riga in lista_righe[1:]:#parto dalla seconda riga
    riga_senza_linefeed= riga[:-1]#creo le stringa senza \n
    lista_campi = riga_senza_linefeed.split(",")#inserirsco in una lista i campi desiderati
    print(lista_campi)
    id=int(lista_campi[0])
    nome=lista_campi[1]
    diz_matematici["id"].append(id)
    diz_matematici["nomi"].append(nome)

print(diz_matematici)
"""

def leggi_file(nome_file):
    file = open(nome_file, "r")
    lista_righe = file.readlines()
    file.close()

    diz_matematici= {"id": [], "nomi": []}

    for riga in lista_righe[1:]:#parto dalla seconda riga
        riga_senza_linefeed= riga[:-1]#creo le stringa senza \n
        lista_campi = riga_senza_linefeed.split(",")#inserirsco in una lista i campi desiderati
        print(lista_campi)
        id=int(lista_campi[0])
        nome=lista_campi[1]
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome)
    
    return diz_matematici

def ricerca(i, diz):
    listaId=diz["id"]
    listaNomi=diz["nomi"]
    print(listaNomi)
    for i, n in zip(listaId, listaNomi):
        if(i==id):
            return n

def stampa_id(dizionario, n):
    print(dizionario)

def main():
    dizionario=leggi_file("./file.csv")
    print(dizionario)

    n=int(4)

    while n>3 or n<0:
        n=int(input("Inserire l'id"))
    print(ricerca(2, dizionario))


if __name__ == "__main__":
    main()