import turtle
finestra = turtle.Screen()

def leggiFile(tur):
    file=open("indicazioni.csv", "r")
    lista_righe=file.readlines()
    file.close()
    lista_comandi=[]
    lista_num=[]
    for riga in lista_righe[:]:
        lista_c0= riga[:-1].split(',')
        lista_comandi.append(lista_c0[0])
        lista_num.append((int)(lista_c0[1]))
    
    for c, n in zip(lista_comandi, lista_num):
        if(c=="forward"):
            tur.forward(n)
        else: 
            if(c=="right"):
                tur.right(n)
            else:
                if(c=="left"):
                    tur.left(n)
    turtle.done()
    

def main():
    pol=turtle.Turtle()
    leggiFile(pol)

"""
def main():
    cursore = turtle.Turtle()
    finestra = turtle.Screen()

    diz = {
        "forward": cursore.forward,
        "backward": cursore.backward,
        "right": cursore.right,
        "left": cursore.left
    }

    """

if __name__ =="__main__": #"_" = Dunder
    main()