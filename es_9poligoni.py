import turtle
import math

def triangolo():
    t=turtle.Turtle()
    t.penup()
    t.goto(-300, 150)
    t.pendown()

    t.color("blue")
    for i in range(0, 3):
        t.forward(100)
        t.left(120)

def quadrato():
    q=turtle.Turtle()
    q.penup()
    q.goto(-50, 150)
    q.pendown()
    q.color("blue")
    for i in range(0, 4):
        q.forward(100)
        q.left(90)

def pentagono():
    p=turtle.Turtle()
    p.penup()
    p.goto(200, 150)
    p.pendown()
    p.color("blue")
    for i in range(0, 5):
        p.forward(100)
        p.left(72)

def esagono():
    e=turtle.Turtle()
    e.penup()
    e.goto(-300, 0)
    e.pendown()
    e.color("blue")
    for i in range(0, 6):
        e.forward(50)
        e.left(60)

def ettagono():
    et=turtle.Turtle()
    et.penup()
    et.goto(-50, 0)
    et.pendown()
    et.color("blue")
    for i in range(0, 7):
        et.forward(50)
        et.left(51.43)

def ottagono():
    o=turtle.Turtle()
    o.penup()
    o.goto(200, 0)
    o.pendown()
    o.color("blue")
    for i in range(0, 8):
        o.forward(50)
        o.left(45)

def ennagono():
    en=turtle.Turtle()
    en.penup()
    en.goto(-300, -200)
    en.pendown()
    en.color("blue")
    for i in range(0, 9):
        en.forward(50)
        en.left(40)

def decagono():
    d=turtle.Turtle()
    d.penup()
    d.goto(-50, -200)
    d.pendown()
    d.color("blue")
    for i in range(0, 10):
        d.forward(50)
        d.left(36)

def endecagono():
    end=turtle.Turtle()
    end.penup()
    end.goto(200, -200)
    end.pendown()
    end.color("blue")
    for i in range(0, 11):
        end.forward(50)
        end.left(32.73)

def poligono(posx, posy, nLati, cursore, colore):
    cursore.penup()
    cursore.color(colore)
    cursore.goto(posx, posy)
    cursore.pendown()
    angolo=360/nLati
    lato=2*80*math.sin(angolo/2*3.1415/180)
    for _ in range(0, nLati):
        cursore.right(angolo)
        cursore.forward(lato)

def main(): 
    diz_pos={3:(-300, 150, "red"), 4:(-50, 150, "blue"), 5:(200, 150, "lime"), 6:(-300, 0, "red"), 
    7:(-50, 0, "blue"), 8:(200, 0, "lime"), 9:(-300, -200, "red"), 10:(-50, -200, "blue"), 11:(200, -200, "lime")}
    finestra=turtle.Screen()
    curs=turtle.Turtle()
    triangolo()
    quadrato()
    pentagono()
    esagono()
    ettagono()
    ottagono()
    ennagono()
    decagono()
    endecagono()
    turtle.done()
    """for nLati, dati in diz_pos.items():
        poligono(dati[0], dati[1], nLati, curs, dati[2])"""

if __name__ == "__main__":
    main()