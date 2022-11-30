class Quadrato():
    def __init__(self, x, y, l):
        self.x=x#float
        self.y=y#float
        self.lato=l#float

    def perimetro(self):
        return self.lato*4

    def area(self):
        return self.lato*self.lato
    
    def isDentro(self, x, y):
        if x<self.x+self.lato and x>self.x and y<self.y+self.lato and y>self.y:
            print("dentro")
        else:
            print("fuori")

def main():
    q=Quadrato(10, 20, 5)
    print(q.perimetro())
    print(q.area())
    q.isDentro(12, 23)

if __name__ == "__main__":
    main()