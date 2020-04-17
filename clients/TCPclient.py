#!/usr/bin/python3
import socket
import sys

def main():
    port = 2248 # Specify the port for the client

    if(len(sys.argv) < 3): # Check to make sure enough arguments were supplied
        print(f'Usage: {sys.argv[0]} server-addr file-name\n')
        exit()
        
    addr = socket.gethostbyname(sys.argv[1])
    transferFile = str(sys.argv[2])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a client socket and connect to the server provided
    client.connect((addr, port))

    client.send(transferFile.encode('utf-8')) # Send the server the name of the file requested

    response = client.recv(1024).decode() # Get servers response
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

if __name__ == "__main__":
    main()