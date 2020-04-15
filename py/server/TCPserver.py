#!/usr/bin/python3
import socket

port = 2248
addr = '0.0.0.0'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr, port))
server.listen(1)
while(True):
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    try:
        print(f'Trying to open {data}')
        file = open(data, 'rb')
        data = file.read(1024)
        conn.send(b'Ayy ok :)')
        while(True):
            #print('In loop')
            conn.send(data)
            data = file.read(1024)
        file.close()
    except:
        print('error occured!')
        conn.send(b'File not found')
        conn.close()
    conn.close()
    break
server.close()