from datetime import datetime
import socket

ora = "ORA"
data = "DATA"
data_ora = "DATA/ORA"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_address = ('127.0.0.1', 5000)

s.bind(my_address)

text_received = ""
text = ""

while text_received != "EXIT":
    text_received, address = s.recvfrom(4096)
    text_received = text_received.decode()
    if text_received == ora:
        text = datetime.now().strftime("%H:%M:%S").encode()
        s.sendto(text, address)
    elif text_received == data:
        text = datetime.now().strftime("%d-%m-%Y").encode()
        s.sendto(text, address)
    elif text_received == data_ora:
        text = datetime.now().strftime("%d-%m-%Y, %H:%M:%S").encode()
        s.sendto(text, address)
    else:
        text = f"messaggio non valido"
        s.sendto(text, address)