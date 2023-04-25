import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.168.1.112", 5000)

my_address = ("192.168.1.119", 5000)
s.bind(my_address)


text_received, address = s.recvfrom(4096)
print(f"Ricevuto: {text_received.decode()} da {address}")

s.sendto(text_received, server_address)
print(f"inviato: {text_received.decode()} a {server_address}")

s.close()