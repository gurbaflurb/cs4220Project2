#!/usr/bin/python3
import socket
import sys

def writeFile(client):
    file = open(transferFile, 'wb')
    data = client.recv(1024)
    while(True):
        file.write(data)
        data = client.recv(1024)
        if(data == b''):
            break

    file.close()

port = 2248

if(len(sys.argv) < 3):
    print(f'Usage: {sys.argv[0]} server-addr file-name\n')
    exit()
addr = socket.gethostbyname(sys.argv[1])
transferFile = str(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((addr, port))

client.send(transferFile.encode('utf-8'))

response = client.recv(1024).decode()
if(response == 'File not found'):
    print('Server failed to find file!')
    client.close()
    exit()
else:
    print(response)
    writeFile(client)
    for i in range(10):
        client.send(transferFile.encode('utf-8'))
        client.recv(1024)
        writeFile(client)
    print('File downloaded!')
client.close()