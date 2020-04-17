#!/usr/bin/python3
import socket
import sys
from random import randint
from hashlib import md5

def getNewFileHash(fileName):
    hasher = md5()
    with open(fileName, 'rb') as file:
        hasher.update(file.read())
    return hasher.hexdigest()

def main():
    port = 2248
    addr = '0.0.0.0'

    if(len(sys.argv) < 2):
        print(f'Usage: {sys.argv[0]} <loss_percent>\n')
        exit()

    loss_chance = int(sys.argv[1])

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((addr, port))

    while(True):
        data, client_conn = server.recvfrom(1024)
        try: 
            fileHash = getNewFileHash(data.decode())
            server.sendto(fileHash.encode('utf-8'), client_conn)
            with open(data.decode(), 'rb') as file:
                while(True):
                    # Randomly drop packets
                    rand = randint(0,100)
                    if(rand < loss_chance):
                        data = file.read(1024)
                    data = file.read(1024)
                    if(data == b''):
                        server.sendto(b'', client_conn)
                        break
                    server.sendto(data, client_conn)
        except Exception as e:
            print(f'An error has occured!\n {e}')
            server.sendto(b'File not found', client_conn)

    server.close()

if __name__ == "__main__":
    main()