import socket
from threading import Thread

server_address = ("192.168.1.112", 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class thread_ricezione(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            text_received, _ = s.recvfrom(20000)
            print(f"\n{text_received.decode()}")
    

def main():
    nome=input("inserire il nome")
    text_init=f"?{nome}"
    s.sendto(text_init.encode(), server_address)
    receiver = thread_ricezione()
    receiver.start()

    while True:
        testo = input("inserisci il nome del destinatario;testo da inviare")
        s.sendto(testo.encode(), server_address)

if __name__ == "__main__":
    main()