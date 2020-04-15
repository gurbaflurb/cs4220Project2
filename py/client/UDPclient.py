#!/usr/bin/python3
import socket
import sys

port = 2248

if(len(sys.argv) < 3):
    print(f'Usage: {sys.argv[0]} server-addr file-name')
    exit()
addr = str(sys.argv[1])
transferFile = str(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((addr, port))
client.send(b'This is some data')
print(client.recv(1024))
client.close()