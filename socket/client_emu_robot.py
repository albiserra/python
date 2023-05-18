import socket

server_address = ("127.0.0.1", 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    s.connect(server_address)

    while(True):
        string = input("Inserire il messaggio")
        string = string.encode()
        s.sendall(string)

if __name__ == "__main__":
    main()