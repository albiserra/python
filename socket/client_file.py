import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5000)

file = "./prova.txt"

with open(file, "rb") as f:
    file_data = f.read

s.sendto(file_data, server_address)