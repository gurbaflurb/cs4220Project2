#!/usr/bin/python3
import socket

def main():
    port = 2248 # Set the port and address to listen on all inbound traffic
    addr = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set the server to be a server and bind the port specified
    server.bind((addr, port))
    server.listen(1) # Listen for inbound connections

    while(True): # Infinite loop for the connection received
        conn, addr = server.accept() # Accept an inbound connection
        data = conn.recv(1024).decode()
        try:
            print(f'Trying to open {data}')
            file = open(data, 'rb') # Try to open the file sent by the client in binary mode
            data = file.read(1024)
            conn.send(b'File found!')
            while(True): # Infinite loop until the file is finished being read
                conn.send(data) # Send the read in data to the client
                data = file.read(1024)
                if(not data): # Check if the data isn't real so it's at the end of the file
                    conn.close()
                    break
            file.close() # Close file
        except: # If an error occurs print that an error occured and send that the file couldnt be found and close the connection
            print('error occured!')
            conn.send(b'File not found')
            conn.close()
        conn.close()
        break # Remove this line to make the script run forever
    server.close()

if __name__ == "__main__":
    main()