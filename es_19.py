import random

def dado(nome_file):
    tav=[[]]

    A=[random.randint(0, 6) for _ in range(10)]
    B=[random.randint(0, 6) for _ in range(10)]
    atmp=0
    btmp=0

    file = open(nome_file, "w")
    for k in range(0, 10):
        file.write(f"{A[k]}, {B[k]}\n")
    
    for a, b in zip(A, B):
        file.write(f"{a}, {b}\n")

    file.close()

dado("dado.txt")