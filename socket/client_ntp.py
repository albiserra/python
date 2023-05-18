import socket

SERVER_ADDRESS = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("client acceso")

while True:
    message = input('Inserisci il messaggio: ')
    s.sendto(message.encode(), SERVER_ADDRESS)
    msg, address = s.recvfrom(4096)
    msg = msg.decode()
    print(msg)