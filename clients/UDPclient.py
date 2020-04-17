#!/usr/bin/python3
import socket
import sys
from hashlib import md5

def writeFile(client, transferFile):
    file = open(transferFile, 'wb')
    data = client.recv(1024)
    while(True):
        file.write(data)
        data = client.recv(1024)
        if(data == b''):
            break

    file.close()

def getNewFileHash(fileName):
    hasher = md5()
    with open(fileName, 'rb') as file:
        hasher.update(file.read())
    return hasher.hexdigest()


def main():
    port = 2248

    if(len(sys.argv) < 3):
        print(f'Usage: {sys.argv[0]} server-addr file-name\n')
        exit()
    addr = socket.gethostbyname(sys.argv[1])
    transferFile = str(sys.argv[2])

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((addr, port))

    client.send(transferFile.encode('utf-8'))

    fileHash = client.recv(1024).decode()
    if(fileHash == 'File not found'):
        print('Server failed to find file!')
        client.close()
        exit()
    else:
        print(f'File found! MD5 Hash:{fileHash}')
        writeFile(client, transferFile)
        currentHash = getNewFileHash(transferFile)
            
        while(fileHash != currentHash):
            client.send(transferFile.encode('utf-8'))
            client.recv(1024)
            writeFile(client, transferFile)
            currentHash = getNewFileHash(transferFile)
        print('File downloaded!')
    client.close()

if __name__ == "__main__":
    main()