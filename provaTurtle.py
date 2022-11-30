import turtle

finestra=turtle.Screen()

alice = turtle.Turtle()
alice.color("red")
alice.pensize(100)
bob = turtle.Turtle()

alice.penup()
alice.forward(100)
bob.right(180)
bob.forward(100)

alice.pendown()
alice.right(60)
bob.left(60)
alice.forward(100)
bob.forward(100)

turtle.done()