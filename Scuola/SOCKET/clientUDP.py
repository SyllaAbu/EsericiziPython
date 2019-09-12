"""
socket() non bloccante  cs
blind() non bloccante s
recvfrom() bloccante cs
sendto() non bloccante cs
close() non bloccante cs
"""
import socket as sck

server = "127.0.0.1"
porta = 5432
close_string = "close"
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

while True:
  msg = input("Inserisci messaggio: ")
  s.sendto(msg.encode(), (server, porta))
  if(msg == close_string):
    break
  data = s.recvfrom(4096)
  print("Server %s ha ricevuto %s" % (server, data))

s.close()