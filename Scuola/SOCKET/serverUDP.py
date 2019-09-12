"""
socket() non bloccante
blind() non bloccante
recvfrom() bloccante
sendto() non bloccante
close() non bloccante
"""
import socket as sck
HOST = "0.0.0.0"
PORT = 5432

close_string = "close"
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
  data, client_address = s.recvfrom(4096)
  print("client %s %s" % (client_address, data.decode()))
  if(data.decode() == close_string):
    break
  s.sendto(data, client_address)

s.close()