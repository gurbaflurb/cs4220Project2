#!/usr/bin/python3
import socket
import sys

port = 2248

if(len(sys.argv) < 3):
    print(f'Usage: {sys.argv[0]} server-addr file-name')
    exit()
addr = str(sys.argv[1])
transferFile = str(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((addr, port))

client.send(transferFile.encode('utf-8'))

response = client.recv(1024).decode()
if(response == 'File not found'): # If the file was not found, print as such and quit
    print('Server failed to find file!')
    client.close()
    exit()
else:
    print(response) # Else print the servers response

file = open(transferFile, 'wb') # Open a file to write as binary
data = client.recv(1024) # Receive the first 1024 bytes of data from server
while(True): # Infinite loop for the server to send data
    file.write(data) # Write the sent data to the file opened
    data = client.recv(1024) # Receive the next 1024 bytes of data
    if(data == b''): # Check if the server is sending null strings
        print('File downloaded!') # If so print the server is done and break out of the loop
        break

file.close() # Close the file and the connection
client.close()