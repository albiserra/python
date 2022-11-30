def tavolaPitagorica():
    
    return[[numero * indice for numero in range(10)] for indice in range(10)]

def stampaFile(nome_file, tabella):
    file=open(nome_file, "w")
    for riga in tabella:
        file.write(f"{riga}\n")


def main():

    tav=tavolaPitagorica()
    stampaFile("tavola.txt", tav)

if __name__ == "__main__":
    main()
