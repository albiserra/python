import socket

SERVER_ADDRESS = ('127.0.0.1', 5000)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("client acceso")

while True:
    word = input('Inserisci la parola: ')
    client.sendto(word.encode(), SERVER_ADDRESS)
    msg, address = client.recvfrom(4096)
    msg = msg.decode()
    print(msg)

    if msg == 'Hai vinto!':
        break

client.close()