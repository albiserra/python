import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 5000))

str_invio = ""
while(str_invio != "exit"):
    str_invio = input(f"inserire il messaggio da inviare: ")
    print(f"invio: {str_invio}")
    s.sendall(str_invio.encode())
    str = s.recv(4096)
    print(f"ricevuto: {str.decode()}")

s.close()