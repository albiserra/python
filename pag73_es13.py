class robot():
    def __init__(self, nome, massa, tipo):
        self.nome = nome#stringa
        self.massa = massa#float
        self.tipo = tipo#stringa

    def getNome(self):
        print(self.nome) 

    def isPericoloso(self):
        if self.tipo == "umanoide" and self.massa >=100:
            return True
        else:
            return False

def main():
    rob=robot("NAO", 110, "umanoide")
    rob.getNome()
    if rob.isPericoloso() == True:
        print("Il robot è pericoloso")
    else:
        print("Il robot non è pericoloso")

if __name__ == "__main__":
    main()