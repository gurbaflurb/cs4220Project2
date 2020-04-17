#!/usr/bin/python3
import socket
import sys

port = 2248
addr = '0.0.0.0'

if(len(sys.argv) < 2):
    print(f'Usage: {sys.argv[0]} loss_probability\n')
    exit()

loss_chance = sys.argv[1]

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((addr, port))

while(True):
    data, client_conn = server.recvfrom(1024)
    try:
        file = open(data.decode(), 'rb')
        server.sendto(b'File Found!', client_conn)
        data = file.read(1024)
        while(True):
            server.sendto(data, client_conn)
            data = file.read(1024)
            if(data == b''):
                server.sendto(data, client_conn)
                break
        file.close()
    except:
        print('An error has occured!')
        server.sendto(b'File not found', client_conn)
    
    break # remove this line to make the server run forever
server.close()