import socket

my_address = ("192.168.1.112", 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(my_address)
print("server acceso")

def main():
    diz = {}
    while True:
        text_received, address = s.recvfrom(20000)
        text = text_received.decode()
        if text[0] == '?':
            diz[text[1:]] = address
            print(f"connesso {text[1:]}")
        else:
            name, message = text.split(';')

            s.sendto(message.encode(), diz[name])

if __name__ == "__main__":
    main()