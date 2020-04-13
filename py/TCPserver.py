#!/usr/bin/python3
import socket

port = 12345
addr = '0.0.0.0'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr, port))
server.listen(1)
while(True):
    conn, addr = server.accept()
    conn.recv(4096)
    conn.close()