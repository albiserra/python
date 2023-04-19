import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.168.1.112", 5000)

while True:
    text = input("Inserire un messaggio: ")
    if text == "exit":
        break
    text_b = text.encode()
    #text_b = b"{text}"

    s.sendto(text_b, server_address)

    text_received, server_address = s.recvfrom(4096)
    print(f"Ricevuto: {text_received.decode()} da {server_address}")

s.close()