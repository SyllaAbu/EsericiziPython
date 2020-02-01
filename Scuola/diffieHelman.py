import socket as sck
from random import randint

N = 9973
g = 1567

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

indirizzo = "0.0.0.0"
porta = 8084

s.bind((indirizzo, porta))
print('Listening...')

s.listen()

conn, addr = s.accept()
print("Connesso con" + str(conn))

# def isPrime(n):
# return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


# N = input('Inserisci un numero N primo')
# while not isPrime(N):
#     N = input('Inserisci un numero N primo')
#
# g = input(f'Inserisci un numero g tra 1 e {N}')
# while 1 < g < N:
#     g = input(f'Inserisci un numero g tra 1 e {N}')


data = conn.recv(4096).decode()
A = data
b = 200 # randint(1, N)
B = (g ** b) % N
print(B)
print("\n>client %s %s" % (addr, data))
conn.sendall(str(B).encode())
print(A)
K = (int(A) ** b) % N
print(K)

conn.close()
s.close()



