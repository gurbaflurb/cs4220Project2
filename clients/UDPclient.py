#!/usr/bin/python3
import socket
import sys
import pickle

def writeFile(fileName, fileData, totalPackets):
    assert isinstance(fileName, str)
    assert isinstance(fileData, dict)
    assert isinstance(totalPackets, int)

    with open(fileName, 'wb') as file:
        for i in range(1, totalPackets+1):
            file.write(fileData[i])

def main():
    if(len(sys.argv) < 3):
        print(f'Usage: {sys.argv[0]} server-addr file-name\n')
        exit()
    
    port = 2248
    addr = socket.gethostbyname(sys.argv[1])
    fileRequested = sys.argv[2]
    is_buffer_filled = False

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((addr, port))
    client.send(fileRequested.encode('utf-8'))

    response = client.recv(2048).decode()
    if(response == 'File not found'):
        print('Server failed to find file!')
        client.close()
        exit()
    else:
        print(f'Server found file, packets to be recieved: {response}')
        fileData = {}
        while not is_buffer_filled:
            data = client.recv(2048)
            if(data == b''):
                is_buffer_filled = True
                for i in range(1, int(response)+1):
                    if (i not in fileData):
                        print(f'Missing Packet(s) {i}')
                        is_buffer_filled = False
                if(not is_buffer_filled):
                    print('Re-requesting file and saving what we got!')
                    client.send(fileRequested.encode('utf-8'))
                    response = client.recv(2048).decode()
                else:
                    break
            else:
                tempDict = pickle.loads(data)
                fileData[tempDict['seq']] = tempDict['data']
        writeFile(fileRequested, fileData, int(response))
        
    client.close()

if __name__ == "__main__":
    main()