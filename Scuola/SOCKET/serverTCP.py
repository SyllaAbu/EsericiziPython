"""
Primitive:

socket() NON BLOCCANTE
bind() NON BLOCCANTE
listen() NON BLOCCANTE
accept() BLOCCANTE
srecv() BLOCCANTE
sendall() NON BLOCCANTE
close() NON BLOCCANTE

"""
import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

indirizzo = "0.0.0.0"
porta = 5432

s.bind((indirizzo, porta))

s.listen()

conn, addr = s.accept()
print("Connesso con" + str(conn))

while True:
    data = conn.recv(4096).decode()
    print("\n>client %s %s" % (addr, data))
    strToSend = input(">")
    strToSend.encode()
    if strToSend == "0":
        break
    s.sendall(strToSend)

conn.close()
s.close()