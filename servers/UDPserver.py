#!/usr/bin/python3
import socket

port = 2248
addr = '0.0.0.0'

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((addr, port))
while(True):
    data = server.recv(1024)
    server.send(data)
    server.close()
    break
server.close()