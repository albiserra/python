import turtle
import random
import time

ANGOLO = 90

def robot(r):
    
    for i in range(0, 7200):
        d=random.randint(0, 3)
        d=d*ANGOLO
        
        r.speed(2000)
        r.pendown()
        r.color("blue")
        r.right(d)
        r.forward(10)

def main():
    f=turtle.Screen()
    r=turtle.Turtle()
    robot(r)

if __name__ == "__main__":
    main()
