#!/usr/bin/python3
import socket
import sys
import pickle
from random import randint

def main():
    if(len(sys.argv) < 2):
        print(f'Usage: {sys.argv[0]} <loss_percent>\n')
        exit()

    loss_percent = int(sys.argv[1])
    port = 2248
    addr = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((addr, port))

    while True:
        data, client_conn = server.recvfrom(1024)
        try:
            with open(data.decode(), 'rb') as file:
                buffer = {}
                seq = 1
                while True:
                    packet_data = file.read(1024)
                    if(packet_data == b''):
                        break
                    else:
                        buffer[seq] = {'seq':seq, 'data':packet_data}
                        seq += 1
                print(f'Packets to be sent: {seq-1}')
                server.sendto(str((seq-1)).encode('utf-8'), client_conn)
                for i in range(1, seq):
                    rand = randint(0, 100)
                    if(rand < loss_percent):
                        continue
                    data = pickle.dumps(buffer[i])
                    server.sendto(data, client_conn)
                server.sendto(b'', client_conn)
        except:
            print('An error has occured')
            server.sendto(b'an error has occured', client_conn)
    server.close()

if __name__ == "__main__":
    main()