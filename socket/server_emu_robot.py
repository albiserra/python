import socket
import turtle
import config

my_address = config.my_address

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(my_address)

t = turtle.Turtle()
t.speed(100)
t.pendown()

def main():
    diz = {'B':t.back, 'F':t.forward, "R":t.right, 'L':t.left}

    s.listen()
    conn, address = s.accept()
    turtle.Screen()
    while(True):

        string = conn.recv(20000)
        string = string.decode()

        if string == "exit":
            break
        elif len(string) > 1 and string[1] != ';' or len(string) <= 1:
            print("errore")
        else:
            command, offset = string.split(';')
            if command in diz:
                try:
                    diz[command](float(offset))
                except: 
                    print("errore dizionario")
    
    conn.close()
    s.close()
        
if __name__ =="__main__":
    main()