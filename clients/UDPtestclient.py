#!/usr/bin/python3
import socket
import sys

def writeFile(fileName, fileData):
    assert isinstance(fileName, str)
    assert isinstance(fileData, dict)

    with open(fileName, 'wb') as file:
        for data in fileData:
            file.write(data)

def main():
    if(len(sys.argv) < 3):
        print(f'Usage: {sys.argv[0]} server-addr file-name\n')
        exit()
    
    port = 2248
    addr = socket.gethostbyname(sys.argv[1])
    fileRequested = sys.argv[2]

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((addr, port))
    client.send(fileRequested.encode('utf-8'))

    response = client.recv(2048).decode()
    if(response == 'File not found'):
        print('Server failed to find file!')
        client.close()
        exit()
    else:
        print(f'Server found file, packets to be recieved: {response}')
        seq = 1
        fileData = {}

    client.close()
