#!/usr/bin/python3
import socket
import sys

port = 12345

if(len(sys.argv) < 3):
    print('Usage: client server-name file-name')
    exit()
addr = str(sys.argv[1])
transferFile = str(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((addr, port))
client.close()