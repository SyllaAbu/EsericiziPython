"""
Primitive

socket() NON BLOCCANTE CS
bind() NON BLOCCANTE S
listen() NON BLOCCANTE S
accept() BLOCCANTE S
srecv() BLOCCANTE CS
sendall() NON BLOCCANTE CS
connect() NON BLOCCANTE C
close() NON BLOCCANTE CS

"""

import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

indirizzo = input("Indirizzo server: ")
porta = int(input("Porta server: "))

s.connect((indirizzo, porta))

strToSend = ""

while True:
    strToSend = input("\n>")
    if strToSend == "0":
        break
    s.sendall(strToSend.encode())
    data = s.recv(4096)
    print("Server %s" % data)

s.close()




