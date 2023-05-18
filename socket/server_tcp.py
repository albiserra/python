import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 5000))

s.listen()

conn, address = s.accept()

str_invio = ""

while(str_invio != "exit"):
    str = conn.recv(4096)
    str.decode()
    print(f"ricevuto: {str} da {address}")

    str_invio = input(f"inserire il messaggio da inviare: ")
    print(f"invio: {str_invio} a {address}")
    conn.sendall(str_invio.encode())

s.close()