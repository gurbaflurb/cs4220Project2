#!/usr/bin/python3
import socket
import sys

port = 2248

if(len(sys.argv) < 3):
    print(f'Usage: {sys.argv[0]} server-addr file-name')
    exit()
addr = str(sys.argv[1])
transferFile = str(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((addr, port))

client.send(transferFile.encode('utf-8'))

response = client.recv(1024).decode()
if(response == 'File not found'):
    print('Server failed to find file!')
    client.close()
    exit()

file = open(transferFile, 'wb')
while(True):
    data = client.recv(1024)
    while(True):
        file.write(data)
        data = client.recv(1024)

file.close()
client.close()