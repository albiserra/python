import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_address = ("127.0.0.1", 5000)
s.bind(my_address)

file = "./prova_ricevuto.txt"

text_received = s.recvfrom(20000)
print(text_received.decode())

with open(file, "wb") as f:
    f.write(text_received)
s.close()
