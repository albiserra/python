import socket
import random

PATH = 'lista_parole.txt'
file = open(PATH, 'r')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5000)
server.bind(server_address)
print("server acceso")

lines = file.readlines()
words = []
for w in lines:
    words.append(w[:-1])

word = random.choice(words)
print(f'è stata estratta la parola: {word}')

while True:
    word_received, address = server.recvfrom(4096)
    word_received = word_received.decode()
    print(f'{address}: {word_received}')

    if len(word) > len(word_received):
        word_received += '_' * (len(word) - len(word_received))

    if word_received == word:
        server.sendto('Hai vinto!'.encode(), address)
        #print('Hai vinto!')
        break
    
    solution = ''
    for (x, y) in zip(word_received, word):
        if x != y:
            solution += '_'
        else:
            solution += x
    
    # print(solution)
    server.sendto(solution.encode(), address)

server.close()